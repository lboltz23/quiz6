from abc import ABC, abstractmethod
import logging

from google.auth import default as google_auth_default


from loguru import logger

class Logger:
    @abstractmethod
    def log(self, level, message):
        pass

class LoggingApplication:
    def __init__(self, logger: Logger):
        self.logger = logger

    def log_message(self, level, message):
        self.logger.log(level, message)   

class ConsoleLogger(Logger):
    def log(self, level, message):
        print(f"{level} {message}")
        
        
class LoguruLogger(Logger):
    def __init__(self):
        logger.add("app_log")

    def log(self,level, message):

        logger.info("info message")

class GoogleAuthLogger(Logger):
    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
    def log(self, level, message):
        _,_ = google_auth_default()
        print(f"[Google Auth] Logged message {message} to Google services")

    

def main():
    console = ConsoleLogger()
    otherlogger = LoguruLogger()
    
    application = LoggingApplication(console)

    application.log_message("INFO", "info message")
    application = LoggingApplication(otherlogger)
    application.log_message("INFO","info message")

    credentials_path = "path/to/credentials.json"

    # Create an instance of GoogleAuthLogger
    google_logger = GoogleAuthLogger(credentials_path)
    application = LoggingApplication(google_logger)
    # Log a message using GoogleAuthLogger
    application.log_message("INFO", "info message")
if __name__ == "__main__":
    main()