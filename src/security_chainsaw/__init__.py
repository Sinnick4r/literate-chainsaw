"""
Security Chainsaw: Security Audit CLI
Package entry-point, version and primary exports.
"""
__version__ = "0.1.0"

from .scanner import CodeScanner
from .patcher import PatchGenerator