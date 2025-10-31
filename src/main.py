"""
Firepit Manager - Main Application Entry Point
Professional firepit design and configuration management system
"""

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from gui.main_window import MainWindow
from database.db_manager import DatabaseManager
from utils.config import Config


def main():
    """Initialize and run the application"""
    
    # Set high DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Firepit Manager")
    app.setOrganizationName("FirepitForge")
    
    # Initialize configuration
    config = Config()
    
    # Initialize database
    db_manager = DatabaseManager(config.get_database_path())
    db_manager.initialize_database()
    
    # Create and show main window
    window = MainWindow(db_manager, config)
    window.show()
    
    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
