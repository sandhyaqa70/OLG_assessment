"""
Logging utility for test automation.
"""
import logging
import os
from datetime import datetime
from config.settings import LOG_DIR, LOG_LEVEL


class LoggerManager:
    """Manages logging for the test automation framework."""
    
    _loggers = {}
    
    @staticmethod
    def get_logger(name):
        """Get or create a logger instance."""
        if name not in LoggerManager._loggers:
            logger = logging.getLogger(name)
            logger.setLevel(LOG_LEVEL)
            
            # Create file handler with UTF-8 encoding
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = os.path.join(LOG_DIR, f"{name}_{timestamp}.log")
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(LOG_LEVEL)
            
            # Create console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(LOG_LEVEL)
            
            # Create formatter
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            
            LoggerManager._loggers[name] = logger
        
        return LoggerManager._loggers[name]
