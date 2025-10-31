"""
Database Models using SQLAlchemy
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import json

Base = declarative_base()


class Component(Base):
    """Firepit component (stones, burners, materials, etc.)"""
    __tablename__ = 'components'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)  # enclosure, burner, fuel, safety, decorative
    attributes_json = Column(Text, nullable=False)  # JSON string of attribute definitions
    values_json = Column(Text, nullable=False)  # JSON string of attribute values
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    designs = relationship("DesignComponent", back_populates="component")
    
    @property
    def attributes(self):
        return json.loads(self.attributes_json)
    
    @attributes.setter
    def attributes(self, value):
        self.attributes_json = json.dumps(value)
    
    @property
    def values(self):
        return json.loads(self.values_json)
    
    @values.setter
    def values(self, value):
        self.values_json = json.dumps(value)


class Design(Base):
    """Firepit design configuration"""
    __tablename__ = 'designs'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    layout_json = Column(Text, nullable=False)  # JSON string of layout configuration
    metadata_json = Column(Text)  # Additional metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    components = relationship("DesignComponent", back_populates="design")
    compliance_results = relationship("ComplianceResult", back_populates="design")
    
    @property
    def layout(self):
        return json.loads(self.layout_json)
    
    @layout.setter
    def layout(self, value):
        self.layout_json = json.dumps(value)
    
    @property
    def metadata(self):
        return json.loads(self.metadata_json) if self.metadata_json else {}
    
    @metadata.setter
    def metadata(self, value):
        self.metadata_json = json.dumps(value)


class DesignComponent(Base):
    """Junction table for designs and components"""
    __tablename__ = 'design_components'
    
    id = Column(Integer, primary_key=True)
    design_id = Column(String, ForeignKey('designs.id'))
    component_id = Column(String, ForeignKey('components.id'))
    quantity = Column(Integer, default=1)
    position_json = Column(Text)  # JSON string for component position in design
    
    # Relationships
    design = relationship("Design", back_populates="components")
    component = relationship("Component", back_populates="designs")
    
    @property
    def position(self):
        return json.loads(self.position_json) if self.position_json else {}
    
    @position.setter
    def position(self, value):
        self.position_json = json.dumps(value)


class Rule(Base):
    """Business rules and compliance rules"""
    __tablename__ = 'rules'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)  # business, compliance, quality, etc.
    condition = Column(Text, nullable=False)
    action = Column(Text, nullable=False)
    priority = Column(String, default='medium')  # low, medium, high, critical
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Standard(Base):
    """Compliance standards and regulations"""
    __tablename__ = 'standards'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    version = Column(String)
    description = Column(Text)
    requirements_json = Column(Text, nullable=False)  # JSON string of requirements
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    @property
    def requirements(self):
        return json.loads(self.requirements_json)
    
    @requirements.setter
    def requirements(self, value):
        self.requirements_json = json.dumps(value)


class ComplianceResult(Base):
    """Results from batch compliance checking"""
    __tablename__ = 'compliance_results'
    
    id = Column(Integer, primary_key=True)
    design_id = Column(String, ForeignKey('designs.id'))
    standard_id = Column(String, ForeignKey('standards.id'))
    status = Column(String, nullable=False)  # pass, fail, warning
    violations_json = Column(Text)  # JSON string of violations
    checked_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    design = relationship("Design", back_populates="compliance_results")
    
    @property
    def violations(self):
        return json.loads(self.violations_json) if self.violations_json else []
    
    @violations.setter
    def violations(self, value):
        self.violations_json = json.dumps(value)


class Milestone(Base):
    """Product management milestones"""
    __tablename__ = 'milestones'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    phase = Column(String, nullable=False)
    completion_percentage = Column(Float, default=0.0)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String, default='not_started')  # not_started, in_progress, completed
    metadata_json = Column(Text)
    
    @property
    def metadata(self):
        return json.loads(self.metadata_json) if self.metadata_json else {}
    
    @metadata.setter
    def metadata(self, value):
        self.metadata_json = json.dumps(value)
