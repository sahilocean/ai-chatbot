"""
Anti-LLM Resume Testing System
=============================

A comprehensive system designed to detect and prevent LLMs from successfully 
passing resume screening processes through sophisticated multi-layered analysis.

This system employs advanced techniques including:
- Behavioral pattern analysis
- Interactive challenge generation  
- LLM fingerprinting and detection
- Temporal consistency validation
- Emotional authenticity assessment
- Adversarial resistance mechanisms

Version: 2.0.0
Author: Anti-LLM Development Team
License: MIT
"""

__version__ = "2.0.0"
__author__ = "Anti-LLM Development Team"
__license__ = "MIT"

# Main system components
from .main_application import AntiLLMResumeSystem

# Core analysis modules
try:
    from .core.anti_llm_resume_tester import AntiLLMResumeTester, ResumeAnalysisResult
    from .advanced.behavioral_analysis import AdvancedBehavioralAnalyzer, BehavioralSignature
    from .interactive.challenge_generator import AdaptiveChallengeGenerator
    from .detection.llm_fingerprinting import AdvancedLLMDetector, LLMFingerprint
except ImportError:
    # Handle cases where modules might not be available
    pass

# Testing framework
try:
    from .tests.test_framework import ComprehensiveTestFramework
except ImportError:
    pass

__all__ = [
    "AntiLLMResumeSystem",
    "AntiLLMResumeTester", 
    "ResumeAnalysisResult",
    "AdvancedBehavioralAnalyzer",
    "BehavioralSignature", 
    "AdaptiveChallengeGenerator",
    "AdvancedLLMDetector",
    "LLMFingerprint",
    "ComprehensiveTestFramework"
]