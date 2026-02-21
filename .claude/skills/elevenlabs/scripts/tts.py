#!/usr/bin/env python3
import argparse, os, requests, json
def get_key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if k: return k
    with open(os.path.expanduser("~/.openclaw/openclaw.json")) as f:
        return json.load(f)["skills"]["entries"]["elevenlabs"]["apiKey"]
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text", required=True); p.add_argument("--output", required=True); p.add_argument("--voice", default="LQbs67CHbe7cOBfXGskQ")
    a = p.parse_args()
    r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{a.voice}",
        headers={"xi-api-key": get_key(), "Content-Type": "application/json"},
        json={"text": a.text, "model_id": "eleven_multilingual_v2", "voice_settings": {"stability": 0.6, "similarity_boost": 0.8, "style": 0.4, "use_speaker_boost": True}}, stream=True)
    if r.status_code != 200: print(f"Error {r.status_code}: {r.text[:500]}"); return
    with open(a.output, "wb") as f:
        for chunk in r.iter_content(1024): f.write(chunk)
    print(f"Saved: {a.output} ({os.path.getsize(a.output)/1024:.0f} KB)")
if __name__ == "__main__": main()
