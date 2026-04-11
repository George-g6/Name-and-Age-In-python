import yt_dlp
import os

def download_youtube_video(url, output_path='downloads'):
    """
    Download a YouTube video using yt-dlp.

    Args:
        url (str): The YouTube URL to download
        output_path (str): Directory to save the video (default: 'downloads')
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'best',  # Download best quality
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            print("Download completed!")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def main():
    print("YouTube Downloader")
    print("==================")
    print("Paste YouTube URLs (one per line). Type 'done' when finished.")

    urls = []
    while True:
        url = input("Enter URL: ").strip()
        if url.lower() == 'done':
            break
        if url:
            urls.append(url)

    if not urls:
        print("No URLs provided. Exiting.")
        return

    print(f"\nDownloading {len(urls)} video(s)...\n")

    for url in urls:
        download_youtube_video(url)

    print("\nAll downloads completed!")

if __name__ == "__main__":
    main()