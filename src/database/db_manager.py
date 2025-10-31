"""
Database Manager - Handles all database operations
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from .models import Base, Component, Design, Rule, Standard
import json
from datetime import datetime


class DatabaseManager:
    """Manages database connections and operations"""
    
    def __init__(self, database_path: str):
        self.database_path = Path(database_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create engine
        self.engine = create_engine(f'sqlite:///{self.database_path}')
        
        # Create session factory
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def initialize_database(self):
        """Create all tables and add sample data if database is empty"""
        Base.metadata.create_all(self.engine)
        
        # Check if database is empty
        with self.get_session() as session:
            if session.query(Component).count() == 0:
                self._add_sample_data(session)
    
    def get_session(self) -> Session:
        """Get a new database session"""
        return self.SessionLocal()
    
    def _add_sample_data(self, session: Session):
        """Add sample components and data"""
        
        # Sample components
        sample_components = [
            Component(
                id='granite_block_001',
                name='Granite Block',
                category='enclosure',
                attributes_json=json.dumps({
                    'dimensions': {'name': 'dimensions', 'type': 'text', 'required': True},
                    'weight_lbs': {'name': 'weight_lbs', 'type': 'number', 'required': True},
                    'max_temperature': {'name': 'max_temperature', 'type': 'number', 'required': True},
                    'cost': {'name': 'cost', 'type': 'number', 'required': True}
                }),
                values_json=json.dumps({
                    'dimensions': '5x10x7 inches',
                    'weight_lbs': 25,
                    'max_temperature': 2000,
                    'cost': 12.50
                })
            ),
            Component(
                id='venturi_burner_001',
                name='Venturi Burner',
                category='burner',
                attributes_json=json.dumps({
                    'btu_output': {'name': 'btu_output', 'type': 'number', 'required': True},
                    'fuel_type': {'name': 'fuel_type', 'type': 'text', 'required': True},
                    'material': {'name': 'material', 'type': 'text', 'required': True},
                    'cost': {'name': 'cost', 'type': 'number', 'required': True}
                }),
                values_json=json.dumps({
                    'btu_output': 50000,
                    'fuel_type': 'natural_gas',
                    'material': 'stainless_steel',
                    'cost': 89.99
                })
            ),
            Component(
                id='natural_gas_001',
                name='Natural Gas System',
                category='fuel',
                attributes_json=json.dumps({
                    'pressure': {'name': 'pressure', 'type': 'text', 'required': True},
                    'connection': {'name': 'connection', 'type': 'text', 'required': True},
                    'cost': {'name': 'cost', 'type': 'number', 'required': True}
                }),
                values_json=json.dumps({
                    'pressure': '7 inches WC',
                    'connection': '1/2 inch NPT',
                    'cost': 45.00
                })
            )
        ]
        
        for component in sample_components:
            session.add(component)
        
        session.commit()
        print("? Sample data added to database")
