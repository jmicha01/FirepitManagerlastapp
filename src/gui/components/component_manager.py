"""
Component Manager Widget - Displays and manages components
"""

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                               QTableWidget, QTableWidgetItem, QHeaderView,
                               QLabel, QLineEdit, QComboBox, QMessageBox)
from PySide6.QtCore import Qt

from ..database.models import Component


class ComponentManagerWidget(QWidget):
    """Widget for managing firepit components"""
    
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        
        self._setup_ui()
        self._load_components()
    
    def _setup_ui(self):
        """Setup UI"""
        layout = QVBoxLayout(self)
        
        # Header
        header_layout = QHBoxLayout()
        title = QLabel("?? Component Library")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        # Filter
        filter_label = QLabel("Filter:")
        header_layout.addWidget(filter_label)
        
        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("Search components...")
        self.filter_input.textChanged.connect(self._filter_components)
        header_layout.addWidget(self.filter_input)
        
        # Category filter
        self.category_filter = QComboBox()
        self.category_filter.addItems(['All', 'Enclosure', 'Burner', 'Fuel', 'Safety', 'Decorative'])
        self.category_filter.currentTextChanged.connect(self._filter_components)
        header_layout.addWidget(self.category_filter)
        
        # Add button
        add_btn = QPushButton("? Add Component")
        add_btn.clicked.connect(self._add_component)
        header_layout.addWidget(add_btn)
        
        layout.addLayout(header_layout)
        
        # Components table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Category', 'Attributes', 'Actions', 'Delete'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        layout.addWidget(self.table)
    
    def _load_components(self):
        """Load components from database"""
        with self.db_manager.get_session() as session:
            components = session.query(Component).all()
            self._populate_table(components)
    
    def _populate_table(self, components):
        """Populate table with components"""
        self.table.setRowCount(0)
        
        for component in components:
            row = self.table.rowCount()
            self.table.insertRow(row)
            
            # ID
            self.table.setItem(row, 0, QTableWidgetItem(component.id))
            
            # Name
            self.table.setItem(row, 1, QTableWidgetItem(component.name))
            
            # Category
            self.table.setItem(row, 2, QTableWidgetItem(component.category.title()))
            
            # Attributes count
            attr_count = len(component.attributes)
            self.table.setItem(row, 3, QTableWidgetItem(f"{attr_count} attributes"))
            
            # Edit button
            edit_btn = QPushButton("?? Edit")
            edit_btn.clicked.connect(lambda checked, c=component: self._edit_component(c.id))
            self.table.setCellWidget(row, 4, edit_btn)
            
            # Delete button
            delete_btn = QPushButton("??? Delete")
            delete_btn.clicked.connect(lambda checked, c=component: self._delete_component(c.id))
            self.table.setCellWidget(row, 5, delete_btn)
    
    def _filter_components(self):
        """Filter components based on search and category"""
        search_text = self.filter_input.text().lower()
        category = self.category_filter.currentText().lower()
        
        with self.db_manager.get_session() as session:
            query = session.query(Component)
            
            if category != 'all':
                query = query.filter(Component.category == category)
            
            components = query.all()
            
            # Filter by search text
            if search_text:
                components = [c for c in components if search_text in c.name.lower()]
            
            self._populate_table(components)
    
    def _add_component(self):
        """Add new component"""
        QMessageBox.information(self, "Add Component", "Component creation dialog will be implemented next!")
    
    def _edit_component(self, component_id):
        """Edit component"""
        QMessageBox.information(self, "Edit Component", f"Edit dialog for {component_id} will be implemented next!")
    
    def _delete_component(self, component_id):
        """Delete component"""
        reply = QMessageBox.question(
            self, 
            "Delete Component",
            f"Are you sure you want to delete component {component_id}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            with self.db_manager.get_session() as session:
                component = session.query(Component).filter_by(id=component_id).first()
                if component:
                    session.delete(component)
                    session.commit()
            
            self._load_components()
            QMessageBox.information(self, "Success", "Component deleted successfully!")
