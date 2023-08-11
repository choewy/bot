from bootstrap.bootstrap_error import BootstrapCommandInvalidError

class Bootstrap:
  
  @staticmethod
  def run() -> None:
    while True:
      try:
        command = input('command(start | exit) : ')

        if command not in ["start", "exit"]:
          raise BootstrapCommandInvalidError()
        
        return command
      except BootstrapCommandInvalidError as e:
        print(e.message)
