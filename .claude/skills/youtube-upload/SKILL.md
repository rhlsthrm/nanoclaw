---
name: youtube-upload
description: Upload videos to YouTube, list channel info, delete videos via YouTube Data API v3. Use when producing content for Karma Chronicles or any YouTube channel management.
---

# YouTube Upload

Upload videos directly to YouTube via the Data API v3.

## Upload a Video

```bash
python3 /Users/rahul/nanoclaw/.claude/skills/youtube-upload/scripts/upload.py \
  --file "/path/to/video.mp4" \
  --title "Video Title" \
  --description "Video description" \
  --tags "tag1,tag2,tag3" \
  --short
```

## Check Channel Stats

```bash
python3 /Users/rahul/nanoclaw/.claude/skills/youtube-upload/scripts/channel_info.py
```

## Auth
Token: `~/.openclaw/youtube/token.json` (auto-refreshes)
Client secret: `~/.openclaw/youtube/client_secret.json`

## Channel: Karma Chronicles (@KarmaChroniclesHD)
