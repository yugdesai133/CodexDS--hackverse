
import uuid
import chromadb
from chromadb.config import Settings
import yfinance as yf
import pandas as pd
from typing import Dict, Any, List

class FinancialIntelligenceEngine:
    def __init__(self, db_path: str = "./financial_chroma_db"):
        # Initialize Persistent ChromaDB client
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(
            name="financial_disclosures",
            metadata={"description": "SEBI filings, FII flows, transcripts, and financial reports"}
        )

    # ---------------------------------------------------------
    # 1. LIVE MARKET & OPTIONS CHAIN RETRIEVAL (Structured Data)
    # ---------------------------------------------------------
    def get_live_market_data(self, ticker_symbol: str) -> Dict[str, Any]:
        """
        Retrieves real-time price, previous close, volume, and options chain.
        NSE equities use '.NS' suffix (e.g., 'RELIANCE.NS', 'TCS.NS').
        """
        formatted_ticker = ticker_symbol if ticker_symbol.endswith(".NS") else f"{ticker_symbol}.NS"
        stock = yf.Ticker(formatted_ticker)

        try:
            fast_info = stock.fast_info
            current_price = fast_info.last_price
            prev_close = fast_info.previous_close
            volume = fast_info.last_volume

            # Calculate price change
            pct_change = ((current_price - prev_close) / prev_close) * 100 if prev_close else 0.0

            # Fetch nearest Options Chain data
            options_summary = {}
            if stock.options:
                nearest_expiry = stock.options[0]
                opt_chain = stock.option_chain(nearest_expiry)
                
                # Aggregate Put-Call Volume & Open Interest
                calls = opt_chain.calls
                puts = opt_chain.puts
                
                options_summary = {
                    "nearest_expiry": nearest_expiry,
                    "total_call_oi": int(calls['openInterest'].sum()) if 'openInterest' in calls else 0,
                    "total_put_oi": int(puts['openInterest'].sum()) if 'openInterest' in puts else 0,
                    "put_call_ratio": round(puts['openInterest'].sum() / calls['openInterest'].sum(), 2) if calls['openInterest'].sum() > 0 else 1.0,
                    "atm_call_iv": float(calls.iloc[0]['impliedVolatility']) if not calls.empty and 'impliedVolatility' in calls else 0.0
                }

            return {
                "status": "SUCCESS",
                "ticker": ticker_symbol,
                "current_price": round(current_price, 2),
                "previous_close": round(prev_close, 2),
                "volume": int(volume),
                "price_change_pct": round(pct_change, 2),
                "options_data": options_summary
            }

        except Exception as e:
            # Fallback degraded data state handling (Hackathon requirement)
            return {
                "status": "DEGRADED",
                "ticker": ticker_symbol,
                "error": str(e),
                "current_price": None,
                "previous_close": None,
                "volume": None,
                "options_data": None
            }

    # ---------------------------------------------------------
    # 2. DOCUMENT INGESTION TO VECTOR DB (SEBI, FII, Transcripts)
    # ---------------------------------------------------------
    def ingest_document(self, ticker: str, doc_type: str, content: str, source_title: str, date: str):
        """
        Chunks and stores disclosures, transcripts, and reports into ChromaDB.
        doc_type: 'SEBI_FILING', 'EARNINGS_TRANSCRIPT', 'FII_FLOW', 'QUARTERLY_PL'
        """
        doc_id = str(uuid.uuid4())
        self.collection.upsert(
            ids=[doc_id],
            documents=[content],
            metadatas=[{
                "ticker": ticker.upper(),
                "doc_type": doc_type,
                "source_title": source_title,
                "date": date
            }]
        )
        return doc_id

    # ---------------------------------------------------------
    # 3. SEMANTIC VECTOR RETRIEVAL (RAG Engine)
    # ---------------------------------------------------------
    def retrieve_disclosures(self, ticker: str, query: str, doc_type: str = None, n_results: int = 3) -> List[Dict[str, Any]]:
        """
        Performs semantic similarity search filtered by ticker and optional document type.
        """
        where_filter = {"ticker": ticker.upper()}
        if doc_type:
            where_filter = {
                "$and": [
                    {"ticker": {"$eq": ticker.upper()}},
                    {"doc_type": {"$eq": doc_type}}
                ]
            }

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_filter
        )

        retrieved_items = []
        if results and results["documents"] and results["documents"][0]:
            for i in range(len(results["documents"][0])):
                retrieved_items.append({
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i] if "distances" in results else None
                })
        return retrieved_items


# =========================================================
# TEST RUN & DEMO PIPELINE
# =========================================================
if __name__ == "__main__":
    engine = FinancialIntelligenceEngine()

    print("--- 1. Testing Live NSE Market & Options Data ---")
    live_feed = engine.get_live_market_data("RELIANCE")
    print(live_feed)

    print("\n--- 2. Ingesting Financial Reports into ChromaDB ---")
    # Ingesting sample Quarterly P&L Report
    engine.ingest_document(
        ticker="RELIANCE",
        doc_type="QUARTERLY_PL",
        content="Reliance Q3 consolidated net profit rose 11% YoY to INR 19,641 crore. EBITDA margin expanded by 90 bps due to strong retail and telecom growth.",
        source_title="Q3 FY26 Financial Statement",
        date="2026-01-20"
    )

    # Ingesting sample SEBI Regulatory Filing
    engine.ingest_document(
        ticker="RELIANCE",
        doc_type="SEBI_FILING",
        content="SEBI Disclosure Regulation 30: Company announces strategic joint venture in green hydrogen infrastructure with capital expenditure of INR 12,000 crore.",
        source_title="SEBI Reg-30 Material Disclosure",
        date="2026-02-14"
    )

    # Ingesting sample FII Flow Disclosure
    engine.ingest_document(
        ticker="RELIANCE",
        doc_type="FII_FLOW",
        content="Foreign Institutional Investors (FII) net purchased INR 1,420 crore of equity in the energy and consumer retail sectors over the last 5 trading sessions.",
        source_title="NSE FII/DII Net Flow Sheet",
        date="2026-02-28"
    )

    print("\n--- 3. Testing Semantic RAG Retrieval ---")
    query_text = "What is the capital expenditure and green energy expansion plan?"
    results = engine.retrieve_disclosures(ticker="RELIANCE", query=query_text, n_results=2)

    for item in results:
        print(f"Source: {item['metadata']['source_title']} ({item['metadata']['doc_type']})")
        print(f"Snippet: {item['content']}")
        print(f"Distance Score: {item['distance']}\n")