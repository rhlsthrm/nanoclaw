---
name: gemini-image-gen
description: Generate images via Google Gemini API. Use for Karma Chronicles artwork or any image generation.
---

# Gemini Image Generation

## API Key
```bash
export GEMINI_API_KEY=$(cat ~/.openclaw/openclaw.json | python3 -c "import sys,json; print(json.load(sys.stdin)['skills']['entries']['nano-banana-pro']['apiKey'])")
```

## Generate
```bash
GEMINI_API_KEY=$GEMINI_API_KEY uv run /Users/rahul/nanoclaw/.claude/skills/gemini-image-gen/scripts/generate.py \
  --prompt "description" --filename output.png --resolution 1K
```

## Karma Chronicles Style Suffix (append to every prompt)
```
vibrant digital illustration style, Indian comic book art, anime-inspired,
bold saturated colors, dramatic composition, ornate details,
Amar Chitra Katha meets modern fantasy anime, stylized not photorealistic
```
