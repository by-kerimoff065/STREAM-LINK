import yt_dlp
import os
import json

def get_youtube_hls_url(video_url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info['url']  # HLS URL-i qaytarır

def main():
    # Config faylını yüklə
    with open("config.json", "r") as f:
        config = json.load(f)

    channels = config["channels"]
    for channel in channels:
        try:
            url = channel["url"]
            if "youtube.com" in url:
                hls_url = get_youtube_hls_url(url)
                print(f"HLS URL for {channel['slug']}: {hls_url}")
                # Burada HLS URL-i ilə lazım olan əməliyyatları edin
            else:
                print(f"Skipping non-YouTube URL: {url}")
        except Exception as e:
            print(f"Error processing channel {channel['slug']}: {e}")

if __name__ == "__main__":
    main()
