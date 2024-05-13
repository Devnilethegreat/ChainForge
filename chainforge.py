# chainforge.py
"""
Main module for ChainForge application.
"""

import argparse
import logging
import os
import sys
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class ChainForgeCore:
    """Core processing class for ChainForge."""

    def __init__(self, threshold: float = 0.75, verbose: bool = False):
