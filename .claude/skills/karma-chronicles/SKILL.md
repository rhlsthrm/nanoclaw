---
name: karma-chronicles
description: Produce and upload Karma Chronicles YouTube Shorts. Full pipeline from script to published video. Use when creating mythology videos or when scheduled tasks trigger production.
---

# Karma Chronicles Video Production

Channel: @KarmaChroniclesHD | Style: Illustrated Indian comic art | Voice: Aaditya K (ElevenLabs)

## Pipeline

### 1. Pick Story
Read `TODO.md` in this skill directory. Pick next 🔲 Todo. Never produce anything marked ✅.

### 2. Write Script (59s max, ~150-170 words)
- Strong hook in first 5 seconds
- No em dashes. Short punchy sentences.
- End with cliffhanger

### 3. Generate 9 Images
Use gemini-image-gen skill. Append to every prompt:
```
vibrant digital illustration style, Indian comic book art, anime-inspired,
bold saturated colors, dramatic composition, ornate details,
Amar Chitra Katha meets modern fantasy anime, stylized not photorealistic,
vertical 9:16 portrait composition, subject centered
```

### 4. Voiceover
```bash
python3 /Users/rahul/nanoclaw/.claude/skills/elevenlabs/scripts/tts.py \
  --text "SCRIPT" --output /tmp/kc/narration.mp3
```

### 5. Music
```bash
python3 /Users/rahul/nanoclaw/.claude/skills/elevenlabs/scripts/music.py \
  --prompt "Epic cinematic Indian orchestral, tabla sitar, no vocals, instrumental" \
  --output /tmp/kc/music.mp3 --duration 75000
```

### 6. Assemble
```bash
# Per image (adjust DUR for each)
ffmpeg -y -loop 1 -t DUR -i img.png \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,format=yuv420p" \
  -c:v libx264 -preset ultrafast -crf 23 -r 24 clip.mp4

# Concat
ls clips/*.mp4 | sort | while read f; do echo "file '$f'"; done > list.txt
ffmpeg -y -f concat -safe 0 -i list.txt -c copy video.mp4

# Mix audio
ffmpeg -y -i video.mp4 -i narration.mp3 -i music.mp3 \
  -filter_complex "[1:a]volume=1.0[v];[2:a]volume=0.2[m];[v][m]amix=inputs=2:duration=shortest[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest mixed.mp4

# Trim to 59s
ffmpeg -y -i mixed.mp4 -t 59 -c:v libx264 -preset fast -crf 23 -c:a aac FINAL.mp4
```

### 7. Upload
```bash
python3 /Users/rahul/nanoclaw/.claude/skills/youtube-upload/scripts/upload.py \
  --file FINAL.mp4 --title "TITLE" --description "DESC" \
  --tags "hindu mythology,indian mythology,karma chronicles,shorts" --short
```

### 8. Update TODO.md
Mark story ✅ Published with YouTube URL.

## Writing Rules
No em dashes. No AI vocab. Run all copy through humanizer patterns.
