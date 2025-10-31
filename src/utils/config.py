"""
Configuration Manager
"""

import configparser
from pathlib import Path


class Config:
    """Manages application configuration"""
    
    def __init__(self, config_file='config.ini'):
        self.config_file = Path(config_file)
        self.config = configparser.ConfigParser()
        
        if self.config_file.exists():
            self.config.read(self.config_file)
        else:
            self._create_default_config()
    
    def _create_default_config(self):
        """Create default configuration"""
        self.config['Database'] = {
            'database_path': 'data/firepit_manager.db',
            'backup_enabled': 'true',
            'backup_interval_days': '7'
        }
        
        self.config['Application'] = {
            'app_name': 'Firepit Manager',
            'version': '1.0.0',
            'theme': 'default'
        }
        
        with open(self.config_file, 'w') as f:
            self.config.write(f)
    
    def get_database_path(self):
        """Get database file path"""
        return self.config.get('Database', 'database_path', fallback='data/firepit_manager.db')
    
    def get(self, section, key, fallback=None):
        """Get configuration value"""
        return self.config.get(section, key, fallback=fallback)
