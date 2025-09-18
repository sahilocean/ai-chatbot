#!/usr/bin/env python3
"""
Setup script for Anti-LLM Resume Testing System
"""

from setuptools import setup, find_packages
import os

# Read README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="anti-llm-resume-system",
    version="2.0.0",
    author="Anti-LLM Development Team",
    author_email="dev@anti-llm-system.com",
    description="Comprehensive LLM-resistant resume evaluation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anti-llm/resume-testing-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
        ],
        "web": [
            "flask>=2.0.0",
            "fastapi>=0.70.0",
            "uvicorn>=0.15.0",
        ],
        "advanced-nlp": [
            "transformers>=4.12.0",
            "torch>=1.9.0",
            "tensorflow>=2.6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "anti-llm-resume=main_application:main",
            "anti-llm-test=tests.test_framework:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json"],
    },
    keywords=[
        "llm-detection",
        "resume-screening", 
        "artificial-intelligence",
        "behavioral-analysis",
        "text-analysis",
        "hiring-tools",
        "fraud-detection",
        "authentication"
    ],
    project_urls={
        "Bug Reports": "https://github.com/anti-llm/resume-testing-system/issues",
        "Source": "https://github.com/anti-llm/resume-testing-system",
        "Documentation": "https://anti-llm-resume-system.readthedocs.io/",
    },
)