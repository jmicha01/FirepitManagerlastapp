"""
Main Application Window
"""

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QTabWidget, QStatusBar, QMenuBar, QMenu, QToolBar)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon

from .components.component_manager import ComponentManagerWidget


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self, db_manager, config):
        super().__init__()
        self.db_manager = db_manager
        self.config = config
        
        self.setWindowTitle("?? Firepit Manager")
        self.setGeometry(100, 100, 1400, 900)
        
        self._setup_ui()
        self._setup_menubar()
        self._setup_toolbar()
        self._setup_statusbar()
    
    def _setup_ui(self):
        """Setup main UI"""
        # Central widget with tabs
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        # Tab widget
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Component Manager tab
        self.component_manager = ComponentManagerWidget(self.db_manager)
        self.tabs.addTab(self.component_manager, "?? Component Library")
        
        # Placeholder tabs (to be implemented)
        self.tabs.addTab(QWidget(), "?? Design Studio")
        self.tabs.addTab(QWidget(), "?? Rules Engine")
        self.tabs.addTab(QWidget(), "? Batch Compliance")
        self.tabs.addTab(QWidget(), "?? Product Dashboard")
    
    def _setup_menubar(self):
        """Setup menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        new_action = QAction("&New Design", self)
        file_menu.addAction(new_action)
        
        open_action = QAction("&Open Design", self)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("&Edit")
        
        # View menu
        view_menu = menubar.addMenu("&View")
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("&About", self)
        help_menu.addAction(about_action)
    
    def _setup_toolbar(self):
        """Setup toolbar"""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # Add toolbar actions
        new_component_action = QAction("New Component", self)
        toolbar.addAction(new_component_action)
        
        toolbar.addSeparator()
        
        new_design_action = QAction("New Design", self)
        toolbar.addAction(new_design_action)
    
    def _setup_statusbar(self):
        """Setup status bar"""
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        statusbar.showMessage("Ready")
