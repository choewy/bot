import json
import math

from yt_dlp import YoutubeDL
from pathlib import Path

from setting import DownloadSetting
from downloader import Downloader

ASSET_VIDEO_PATH = "assets/video"
ASSET_AUDIO_PATH = "assets/audio"


def initialize_asset_directory() -> None:
    paths = [ASSET_VIDEO_PATH, ASSET_AUDIO_PATH]

    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)


def download_youtube_video(url: str, filename) -> None:
    ydl_opts = {
        "format": "bestvideo[height<=1080][ext=mp4]",
        "outtmpl": f"{ASSET_VIDEO_PATH}/{filename}",
        "retries": 10,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)


def download_youtube_audio(url: str, filename: str) -> None: 
    ydl_opts = {
        "outtmpl": f"{ASSET_AUDIO_PATH}/{filename}",
        "format": "bestaudio/best",
        "extract_audio": True,
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    download_setting = DownloadSetting()
    downloader = Downloader()

    for target in download_setting.targets:
        downloader.download(target)
