"""MCP 代理测试：playwright + context7"""
from mcp_client import call, INIT_PARAMS

# ==========================================
# Playwright
# ==========================================
print("=== [Playwright] 1. Initialize ===")
call("playwright", "initialize", INIT_PARAMS, req_id=1)

print("=== [Playwright] 2. tools/list（检查 dummy 注入）===")
result = call("playwright", "tools/list", {}, req_id=2)
for tool in result.get("result", {}).get("tools", []):
    schema = tool.get("inputSchema", {})
    print(f"  {tool['name']}: required={schema.get('required', [])}, has_dummy={'dummy' in schema.get('properties', {})}")
print()

print("=== [Playwright] 3. Navigate ===")
call("playwright", "tools/call", {
    "name": "browser_navigate",
    "arguments": {"url": "https://iliyian.com"}
}, req_id=3)

print("=== [Playwright] 4. 模拟 Gemini: browser_snapshot(dummy='') ===")
call("playwright", "tools/call", {
    "name": "browser_snapshot",
    "arguments": {"dummy": ""}
}, req_id=4)

# ==========================================
# Context7
# ==========================================
print("=== [Context7] 1. Initialize ===")
call("context7", "initialize", INIT_PARAMS, req_id=1)

print("=== [Context7] 2. tools/list ===")
call("context7", "tools/list", {}, req_id=2)

print("=== [Context7] 3. resolve-library-id ===")
call("context7", "tools/call", {
    "name": "resolve-library-id",
    "arguments": {"libraryName": "playwright"}
}, req_id=3)
