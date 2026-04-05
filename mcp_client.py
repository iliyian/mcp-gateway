import requests
from dotenv import dotenv_values

env = dotenv_values('.env')
TOKEN = env.get('AUTH_TOKEN', '')
BASE_URL = 'http://127.0.0.1:6000'
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

INIT_PARAMS = {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "test", "version": "0.1.0"}
}

def call(path, method, params=None, req_id=1, timeout=120):
    url = f'{BASE_URL}/{path}'
    payload = {"jsonrpc": "2.0", "id": req_id, "method": method}
    if params is not None:
        payload["params"] = params
    resp = requests.post(url, json=payload, headers=HEADERS, timeout=timeout)
    print(f"[{method}] 状态码: {resp.status_code}")
    print(f"[{method}] 响应: {resp.text[:1000]}")
    print()
    return resp.json() if resp.text else {}
