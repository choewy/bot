from pathlib import Path
from yt_dlp import YoutubeDL


class Downloader:

    __ASSET_VIDEO_PATH = "assets/video"
    __ASSET_AUDIO_PATH = "assets/audio"


    def __init__(self) -> None:
        self.__initialize_asset_directory()


    def download(self, target: any) -> None:
        url = target["url"]
        output = target["output"]

        if target["video"]:
           with YoutubeDL(self.__get_ydl_video_options(output)) as ydl:
              ydl.download([url])

        if target["audio"]:
           with YoutubeDL(self.__get_ydl_audio_options(output)) as ydl:
              ydl.download([url])


    def __initialize_asset_directory(self) -> None:
      paths = [self.__ASSET_VIDEO_PATH, self.__ASSET_AUDIO_PATH]

      for path in paths:
          Path(path).mkdir(parents=True, exist_ok=True)


    def __get_ydl_video_options(self, filename: str) -> any:
      ext = ".mp4"

      if ext not in filename:
          filename += ext

      save_path = "/".join([self.__ASSET_VIDEO_PATH, filename])

      return {
        "outtmpl": save_path,
        "format": "bestvideo[height<=1080][ext=mp4]",
        "retries": 10,
      }


    def __get_ydl_audio_options(self, filename: str) -> any:
      ext = ".mp3"

      if ext not in filename:
          filename += ext

      save_path = "/".join([self.__ASSET_AUDIO_PATH, filename])

      return {
        "outtmpl": save_path,
        "format": "bestaudio/best",
        "extract_audio": True,
      }
