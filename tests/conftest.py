"""Pytest configuration for Structure-Flow Calculus tests."""

import sys
from pathlib import Path

# Ensure src/ is on the path for test discovery
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
