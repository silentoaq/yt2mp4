import yt_dlp
import keyboard

def download_video(url, format='best', output_format='bestvideo+bestaudio'):
    ydl_opts = {
        'format': format,
        'merge_output_format': output_format,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

while True:
    print("enter yt video url（Press esc to close):")
    url = input()
    if url.strip() == "":
        print("The URL cannot be empty, please re-enter it.")
        continue
    
    print("downloading...")
    download_video(url)
    print("downloaded")

    if keyboard.is_pressed('esc'):
        print("goodbye")
        break
