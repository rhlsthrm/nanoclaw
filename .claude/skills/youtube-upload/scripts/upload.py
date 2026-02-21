#!/usr/bin/env python3
"""Upload video to YouTube via Data API v3."""
import argparse, json, os, sys
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

TOKEN_FILE = os.path.expanduser("~/.openclaw/youtube/token.json")

def get_youtube_service():
    with open(TOKEN_FILE) as f:
        token_data = json.load(f)
    
    creds = Credentials(
        token=token_data["token"],
        refresh_token=token_data["refresh_token"],
        token_uri=token_data["token_uri"],
        client_id=token_data["client_id"],
        client_secret=token_data["client_secret"],
        scopes=token_data["scopes"],
    )
    
    if creds.expired or not creds.valid:
        creds.refresh(Request())
        token_data["token"] = creds.token
        with open(TOKEN_FILE, "w") as f:
            json.dump(token_data, f, indent=2)
    
    return build("youtube", "v3", credentials=creds)

def upload(file_path, title, description, tags=None, category="22", privacy="public", is_short=False):
    youtube = get_youtube_service()
    
    if is_short and "#Shorts" not in title:
        title = title + " #Shorts"
    
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or [],
            "categoryId": category,  # 22 = People & Blogs
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": False,
        },
    }
    
    media = MediaFileUpload(file_path, chunksize=1024*1024, resumable=True)
    
    request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body=media,
    )
    
    print(f"Uploading {file_path}...")
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  {int(status.progress() * 100)}% uploaded")
    
    video_id = response["id"]
    print(f"✅ Upload complete!")
    print(f"Video ID: {video_id}")
    print(f"URL: https://youtube.com/shorts/{video_id}" if is_short else f"URL: https://youtube.com/watch?v={video_id}")
    return video_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", default="")
    parser.add_argument("--tags", default="")
    parser.add_argument("--privacy", default="public")
    parser.add_argument("--short", action="store_true")
    args = parser.parse_args()
    
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    upload(args.file, args.title, args.description, tags, privacy=args.privacy, is_short=args.short)
