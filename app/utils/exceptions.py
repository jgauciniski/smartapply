class SmartApplyError(Exception):
    """Base exception for all SmartApply errors"""
    pass

class AnalysisError(SmartApplyError):
    """Raised when LLM analysis fails after retries"""
    pass

class InvalidInputError(SmartApplyError):
    """Raised when resume or job description input is invalid"""
    pass