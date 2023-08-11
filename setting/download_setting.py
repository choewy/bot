import re
import json

from math import isnan
from pathlib import Path

from setting.download_setting_error import \
  DownloadCountValueError, \
  DownloadCountRangeError, \
  DownloadUrlValueError, \
  DownloadFilenameValueError, \
  DownloadFlagValueError


class DownloadSetting:
    
    __DOWNLOAD_ASSETS_PATH = 'assets'
    __DOWNLOAD_SETTING_PATH = 'assets/downloads.json'


    def __init__(self) -> None:
        self.__targets = self.__load_download_setting_file()
        self.__count = self.__targets.__len__()

        if (self.__count == 0):
          self.__input_download_target_count()
          self.__input_download_targets()


    @property
    def targets(self) -> list:
       return self.__targets


    @property
    def count(self) -> int:
       return self.__count


    def __load_download_setting_file(self) -> list:
      Path(self.__DOWNLOAD_ASSETS_PATH).mkdir(parents=True, exist_ok=True)

      if (Path(self.__DOWNLOAD_SETTING_PATH).exists() == False):
         return []

      with open(self.__DOWNLOAD_SETTING_PATH, 'r', encoding='utf-8') as file:
          return json.loads(file.read())


    def __input_download_target_count(self) -> None:
        self.__count

        while self.__count < 1:
            val = input('input download count : ')

            try:
                count = int(val)

                if isnan(count):
                    raise DownloadCountValueError()
                
                if count < 1:
                    raise DownloadCountRangeError()
                
                self.__count = count
                
            except ValueError as e: 
              print(DownloadCountValueError().message)
                
            except DownloadCountValueError as e:
              print(e.message)    

            except DownloadCountRangeError as e:
              print(e.message)


    def __input_download_url(self) -> str:
      pattern = r'^https:\/\/(www\.|)youtube.com\/watch\?v\='

      while True:
        try:
          url = input('input youtube url : ')
          res = re.compile(pattern).match(url)

          if res is None:
            raise DownloadUrlValueError()
          
          return url
        
        except DownloadUrlValueError as e:
          print(e.message)


    def __input_download_output(self) -> bool:
      pattern = r'[\{\}\/?,;:|*~`!^\+<>@\#$%^\\\=\'\"]'

      while True:
        try:
          output = input('input save filename : ')
          res = re.compile(pattern).match(output)

          if res is not None:
               raise DownloadFilenameValueError()
          
          return output
        
        except DownloadFilenameValueError as e:
          print(e.message)

    def __input_download_flag(self, key='') -> str:
      while True:
        try:
          video = input(f"input {key}(true or false) : ")
          
          if video not in ['true', 'false']:
              raise DownloadFlagValueError()
          
          return video == 'true'
        
        except DownloadFlagValueError as e:
          print(e.message)


    def __input_download_targets(self) -> None:
      count = self.__count

      while count > 0:
          target = {
            "url": self.__input_download_url(),
            "output": self.__input_download_output(),
            "video": self.__input_download_flag('video'),
            "audio": self.__input_download_flag('audio')
          }

          self.__targets.append(target)
          count -= 1

      with open(self.__DOWNLOAD_SETTING_PATH, 'w', encoding='utf-8') as file:
          file.write(json.dumps(self.__targets, ensure_ascii=False, indent=2))

          
    


