class BootstrapCommandInvalidError(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)

    self.message = '[ Error ] invalid bootstrap command(start or exit).'