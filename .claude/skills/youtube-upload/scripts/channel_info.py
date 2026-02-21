#!/usr/bin/env python3
import json, os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
TOKEN_FILE = os.path.expanduser("~/.openclaw/youtube/token.json")
with open(TOKEN_FILE) as f: td = json.load(f)
creds = Credentials(token=td["token"], refresh_token=td["refresh_token"], token_uri=td["token_uri"], client_id=td["client_id"], client_secret=td["client_secret"], scopes=td["scopes"])
if not creds.valid:
    creds.refresh(Request())
    td["token"] = creds.token
    with open(TOKEN_FILE, "w") as f: json.dump(td, f, indent=2)
yt = build("youtube", "v3", credentials=creds)
ch = yt.channels().list(part="snippet,statistics", mine=True).execute()
for c in ch.get("items", []):
    s = c["statistics"]
    print(f"Channel: {c['snippet']['title']}\nSubscribers: {s.get('subscriberCount','?')}\nVideos: {s.get('videoCount','?')}\nViews: {s.get('viewCount','?')}")
