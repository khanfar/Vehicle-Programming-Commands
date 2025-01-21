import logging
import os
from datetime import datetime

class Logger:
    def __init__(self):
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        # Set up logging
        log_file = os.path.join('logs', f'keyprogrammer_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('KeyProgrammer')
        
    def info(self, message):
        """Log info message"""
        self.logger.info(message)
        
    def error(self, message):
        """Log error message"""
        self.logger.error(message)
        
    def warning(self, message):
        """Log warning message"""
        self.logger.warning(message)
        
    def debug(self, message):
        """Log debug message"""
        self.logger.debug(message)
