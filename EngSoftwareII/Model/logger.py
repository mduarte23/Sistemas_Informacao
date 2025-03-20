import logging

class SingletonLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonLogger, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.logger = logging.getLogger("SingletonLogger")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
    
    def error(self, message):
        self.logger.error(message)

# Usage
logger = SingletonLogger().get_logger()
logger.info("This is a log message.")

