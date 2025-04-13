"""
Base class for all data sources
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class DataSource(ABC):
    """Abstract base class for all data sources"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
    
    @abstractmethod
    def connect(self) -> bool:
        """Establish connection to the data source"""
        pass
    
    @abstractmethod
    def fetch_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch data from the source"""
        pass
    
    @abstractmethod
    def validate_credentials(self) -> bool:
        """Validate API credentials"""
        pass 