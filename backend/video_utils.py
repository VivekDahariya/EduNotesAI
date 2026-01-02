import yt_dlp
import os

def download_video(youtube_url, output_dir='temp/downloads'):
    """
    Downloads a YouTube video in the best available format (mp4).
    Returns the path to the downloaded file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            file_path = ydl.prepare_filename(info)
            print(f"Successfully downloaded: {file_path}")
            return file_path
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

if __name__ == "__main__":
    # Test block to verify it works independently
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    download_video(test_url)