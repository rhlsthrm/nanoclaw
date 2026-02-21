# Karma Chronicles - TODO

## Channel Info
- YouTube Studio: https://studio.youtube.com/channel/UCleFL9xwvhLMva_FW-KF-vA
- Handle: @KarmaChroniclesHD
- Launched: 2026-02-21
- First video: Samudra Manthan (Short)

## Content Queue

| # | Story | Status | Hook |
|---|-------|--------|------|
| 1 | Samudra Manthan | ✅ Published | "The gods were dying..." |
| 2 | Shiva vs Andhaka | 🔲 Todo | "Shiva killed his own son..." |
| 3 | Why Ganesha Has an Elephant Head | 🔲 Todo | "Shiva beheaded his own child" |
| 4 | Mohini and the Nectar (Part 2) | 🔲 Todo | "The demons were tricked..." |
| 5 | Karna: The Greatest Warrior Nobody Wanted | 🔲 Todo | "He was thrown in a river as a baby" |
| 6 | Why Is Shiva's Throat Blue? | 🔲 Todo | "He swallowed poison to save the universe" |

## Production Pipeline
1. Script (Claude) → `scripts/{name}.md`
2. Images (Gemini) → `images/v2/{name}/`
3. Voice (ElevenLabs TTS, Aaditya K) → `audio/{name}-narration.mp3`
4. Music (ElevenLabs Music) → `audio/{name}-music.mp3`
5. Assembly (FFmpeg, 59s, 1080x1920) → `output/{name}-SHORT-FINAL.mp4`
6. Upload to YouTube

## Style
- Visual: See STYLE-GUIDE.md (illustrated, Amar Chitra Katha + anime)
- Writing: No em dashes, short punchy sentences, humanized copy
- Voice: Aaditya K (ElevenLabs, Indian dramatic narration)
- Music: Epic Indian orchestral, instrumental only

## Costs
- Images: ~$0 (Gemini free tier)
- Voice: ElevenLabs credits
- Music: ElevenLabs credits
- Total per video: ~$0.50-1.00

## Future Improvements
- [ ] Add subtitles (install ffmpeg with freetype or use Pillow)
- [ ] Ken Burns motion on stills (optimize zoompan performance)
- [ ] AI video clips for key moments (Kling/Veo when budget allows)
- [ ] Hindi dubbed versions for 2x audience
- [ ] Thumbnail generation with text overlays
