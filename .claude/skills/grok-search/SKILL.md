---
name: grok-search
description: Search web and X/Twitter via xAI Grok API. Use for research, social monitoring, trending topics.
---

# Grok Search (xAI)

## API Key
```bash
export XAI_API_KEY=$(cat ~/.openclaw/openclaw.json | python3 -c "import sys,json; print(json.load(sys.stdin)['skills']['entries']['grok']['apiKey'])")
```

## Search X/Twitter
```bash
curl -s "https://api.x.ai/v1/chat/completions" \
  -H "Authorization: Bearer $XAI_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"grok-3","messages":[{"role":"user","content":"Search X for: QUERY"}],"tools":[{"type":"function","function":{"name":"search_x"}}]}'
```

## Search Web
Same but use `search_web` tool. Always use tools for fresh results.
