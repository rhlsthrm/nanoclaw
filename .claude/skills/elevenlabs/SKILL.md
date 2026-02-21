---
name: elevenlabs
description: Generate voiceovers and background music via ElevenLabs API. Use for Karma Chronicles video production or any TTS/music needs.
---

# ElevenLabs (Voice + Music)

## API Key
```bash
export ELEVENLABS_API_KEY=$(cat ~/.openclaw/openclaw.json | python3 -c "import sys,json; print(json.load(sys.stdin)['skills']['entries']['elevenlabs']['apiKey'])")
```

## Generate Voiceover
```bash
python3 /Users/rahul/nanoclaw/.claude/skills/elevenlabs/scripts/tts.py \
  --text "Narration text" --output /path/to/output.mp3 --voice LQbs67CHbe7cOBfXGskQ
```
Voices: Aaditya K (LQbs67CHbe7cOBfXGskQ), Viraj (3Dfn3iRttMKWMoZ2tEFU), Rudra (tTZ0TVc9Q1bbWngiduLK)

## Generate Music
```bash
python3 /Users/rahul/nanoclaw/.claude/skills/elevenlabs/scripts/music.py \
  --prompt "Epic Indian orchestral, no vocals" --output /path/to/music.mp3 --duration 75000
```
