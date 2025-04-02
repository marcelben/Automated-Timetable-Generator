from PyQt5 import QtWidgets
from components import Database as db
from containers import Main
import sys
import logging
import traceback
import os

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG for more detailed output
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),  # Log to file
        logging.StreamHandler()  # Also log to console
    ]
)
logger = logging.getLogger(__name__)

def check_environment():
    """Check if all required files and directories exist"""
    try:
        logger.info("Checking environment...")
        required_files = ['gas.db']
        for file in required_files:
            if not os.path.exists(file):
                logger.warning(f"Required file {file} not found")
                return False
        logger.info("Environment check passed")
        return True
    except Exception as e:
        logger.error(f"Error checking environment: {e}")
        return False

def main():
    try:
        logger.info("Starting application...")
        
        # Check environment
        if not check_environment():
            logger.error("Environment check failed")
            return 1

        # Initialize database
        if not db.checkSetup():
            logger.info("Initializing database...")
            try:
                db.setup()
                logger.info("Database initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize database: {e}")
                logger.error("Traceback:")
                logger.error(traceback.format_exc())
                return 1

        # Create Qt application
        logger.info("Creating Qt application...")
        app = QtWidgets.QApplication(sys.argv)
        
        # Create main window
        try:
            logger.info("Creating main window...")
            parent = QtWidgets.QMainWindow()
            logger.debug("Parent window created")
            
            logger.info("Initializing MainWindow...")
            main_window = Main.MainWindow(parent)
            logger.debug("MainWindow initialized")
            
            logger.info("Showing parent window...")
            parent.show()
            logger.info("Application window created successfully")
        except Exception as e:
            logger.error(f"Failed to create main window: {e}")
            logger.error("Traceback:")
            logger.error(traceback.format_exc())
            return 1

        # Run application
        logger.info("Starting application event loop")
        return app.exec_()

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        logger.error("Traceback:")
        logger.error(traceback.format_exc())
        return 1

if __name__ == '__main__':
    logger.info("Application starting...")
    exit_code = main()
    logger.info(f"Application exiting with code {exit_code}")
    sys.exit(exit_code)