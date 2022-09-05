import logging


class ColoredFormatter(logging.Formatter):
    # grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt: str):
        super().__init__()
        self.fmt = fmt
        self.formats = {
                # logging.DEBUG: self.grey + self.fmt + self.reset,
                logging.INFO:     self.blue + self.fmt + self.reset,
                logging.WARNING:  self.yellow + self.fmt + self.reset,
                logging.ERROR:    self.red + self.fmt + self.reset,
                logging.CRITICAL: self.bold_red + self.fmt + self.reset
                }

    def format(self, record):
        log_format = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_format, datefmt="%H:%M %p")
        return formatter.format(record)


class CustomLogger:
    def __init__(self):
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.INFO)
        stdout_handler.setFormatter(
                ColoredFormatter("%(levelname)s | %(asctime)s | %(message)s"))
        self.custom_logger = logging.getLogger(__name__)
        self.custom_logger.setLevel(logging.INFO)
        self.custom_logger.addHandler(stdout_handler)

    def info(self, message: str, function_name: str, file_name: str):
        self.custom_logger.info("FileName: %s | FunctionName: %s | Message: %s", file_name, function_name, message)

    def debug(self, message: str, function_name: str, file_name: str):
        self.custom_logger.debug("FileName: %s | FunctionName: %s | Message: %s", file_name, function_name, message)

    def warning(self, message: str, function_name: str, file_name: str):
        self.custom_logger.warning("FileName: %s | FunctionName: %s | Message: %s", file_name, function_name, message)

    def error(self, message: str, function_name: str, file_name: str):
        self.custom_logger.error("FileName: %s | FunctionName: %s | Message: %s", file_name, function_name, message,
                                 exc_info=True)

    def critical(self, message: str, function_name: str, file_name: str):
        self.custom_logger.critical("FileName: %s | FunctionName: %s | Message: %s", file_name, function_name, message,
                                    exc_info=True)


logger = CustomLogger()
