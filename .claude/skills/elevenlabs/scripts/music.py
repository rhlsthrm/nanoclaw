#!/usr/bin/env python3
import argparse, os, requests, json
def get_key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if k: return k
    with open(os.path.expanduser("~/.openclaw/openclaw.json")) as f:
        return json.load(f)["skills"]["entries"]["elevenlabs"]["apiKey"]
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True); p.add_argument("--output", required=True); p.add_argument("--duration", type=int, default=75000)
    a = p.parse_args()
    r = requests.post("https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128",
        headers={"xi-api-key": get_key(), "Content-Type": "application/json"},
        json={"prompt": a.prompt, "music_length_ms": a.duration, "model_id": "music_v1"})
    if r.status_code != 200: print(f"Error {r.status_code}: {r.text[:500]}"); return
    with open(a.output, "wb") as f: f.write(r.content)
    print(f"Saved: {a.output} ({os.path.getsize(a.output)/1024:.0f} KB)")
if __name__ == "__main__": main()
