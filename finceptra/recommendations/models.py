"""
Data models for investment recommendations
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class AssetClass(str, Enum):
    EQUITIES = "equities"
    BONDS = "bonds"
    COMMODITIES = "commodities"
    CRYPTO = "crypto"
    REAL_ESTATE = "real_estate"

class InvestmentRecommendation(BaseModel):
    """Model for investment recommendations"""
    
    asset_class: AssetClass
    symbol: str
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    risk_level: RiskLevel
    expected_return: float
    time_horizon: str
    rationale: str
    supporting_data: List[dict] = Field(default_factory=list)

class RiskProfile(BaseModel):
    """Model for investor risk profile"""
    
    risk_tolerance: RiskLevel
    investment_horizon: str
    financial_goals: List[str]
    constraints: Optional[List[str]] = None
    current_portfolio: Optional[dict] = None 