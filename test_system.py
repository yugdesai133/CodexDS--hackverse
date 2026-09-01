
import sys
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def run_tests():
    print("=" * 60)
    print("🚀 STARTING FININTEL FULL-SYSTEM INTEGRATION TEST")
    print("=" * 60)

    # 1. Health Check & Root Endpoints
    print("\n[TEST 1] Testing Backend Connectivity...")
    try:
        res = requests.get(f"{BASE_URL}/docs", timeout=3)
        assert res.status_code == 200
        print("  ✅ Backend is ONLINE and responding on port 8000.")
    except Exception as e:
        print(f"  ❌ FAILED: Could not reach backend at {BASE_URL}. Ensure uvicorn is running.")
        print(f"     Error details: {e}")
        sys.exit(1)

    # 2. Register Conservative Investor
    print("\n[TEST 2] Testing User Registration (Conservative Profile)...")
    user_conservative_payload = {
        "name": "Test Conservative User",
        "age": 45,
        "invested_amount": 250000.0,
        "investment_goal": "LONG_TERM",
        "risk_tolerance": "CONSERVATIVE",
        "market_experience": "BEGINNER"
    }
    res_cons = requests.post(f"{BASE_URL}/api/users", json=user_conservative_payload)
    assert res_cons.status_code == 201, f"Expected 201, got {res_cons.status_code}: {res_cons.text}"
    user_cons_data = res_cons.json()
    cons_id = user_cons_data["user_id"]
    print(f"  ✅ Created Conservative User: ID = {cons_id}")

    # 3. Register Aggressive Investor
    print("\n[TEST 3] Testing User Registration (Aggressive Profile)...")
    user_aggressive_payload = {
        "name": "Test Aggressive Trader",
        "age": 28,
        "invested_amount": 100000.0,
        "investment_goal": "SHORT_TERM",
        "risk_tolerance": "AGGRESSIVE",
        "market_experience": "ADVANCED"
    }
    res_agg = requests.post(f"{BASE_URL}/api/users", json=user_aggressive_payload)
    assert res_agg.status_code == 201, f"Expected 201, got {res_agg.status_code}: {res_agg.text}"
    user_agg_data = res_agg.json()
    agg_id = user_agg_data["user_id"]
    print(f"  ✅ Created Aggressive User: ID = {agg_id}")

    # 4. Fetch Users List
    print("\n[TEST 4] Testing User Fetch & Database Persistence...")
    res_list = requests.get(f"{BASE_URL}/api/users")
    assert res_list.status_code == 200
    users_list = res_list.json()
    assert any(u["user_id"] == cons_id for u in users_list)
    assert any(u["user_id"] == agg_id for u in users_list)
    print(f"  ✅ Database confirmed persistence: Found {len(users_list)} registered users.")

    # 5. Multi-Agent Reasoning Test (Conservative User)
    print("\n[TEST 5] Testing Multi-Agent Analysis for Conservative User...")
    res_analyze_cons = requests.post(f"{BASE_URL}/api/analyze", json={
        "user_id": cons_id,
        "ticker": "RELIANCE.NS"
    })
    assert res_analyze_cons.status_code == 200
    out_cons = res_analyze_cons.json()
    print(f"  ✅ Action Synthesized: {out_cons['action']}")
    print(f"     Technical Trace : {out_cons['reasoning_chain']['technical_agent']}")
    print(f"     Fundamental RAG : {out_cons['reasoning_chain']['fundamental_agent']}")
    print(f"     Sentiment Trace : {out_cons['reasoning_chain']['sentiment_agent']}")
    assert "ACCUMULATE" in out_cons["action"] or "BUY" in out_cons["action"]

    # 6. Multi-Agent Reasoning Test (Aggressive User Profile Adaptation)
    print("\n[TEST 6] Testing Profile Adaptation (Aggressive User on Same Ticker)...")
    res_analyze_agg = requests.post(f"{BASE_URL}/api/analyze", json={
        "user_id": agg_id,
        "ticker": "RELIANCE.NS"
    })
    assert res_analyze_agg.status_code == 200
    out_agg = res_analyze_agg.json()
    print(f"  ✅ Action Synthesized: {out_agg['action']}")
    print(f"     Strategy Aligned: {out_agg['strategy_fit']}")
    
    # Verify outputs adapt to user profiles
    assert out_cons["action"] != out_agg["action"], "Profile adaptation failure: Both profiles received identical advice!"
    print("  ✅ Profile Adaptivity Verified: Outputs adapt based on user risk tolerance.")

    # 7. Execution Logs & Audit Trail
    print("\n[TEST 7] Testing Audit Telemetry & Logging...")
    res_logs = requests.get(f"{BASE_URL}/api/logs")
    assert res_logs.status_code == 200
    logs = res_logs.json()
    assert len(logs) >= 2
    latest_log = logs[0]
    print(f"  ✅ Audit Log Verified: Session ID '{latest_log['log_id']}' recorded with latency {latest_log['agent_latency_ms']} ms.")

    print("\n" + "=" * 60)
    print("🎉 ALL 7 SYSTEM TESTS PASSED! YOUR CODE IS PRODUCTION-READY.")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()