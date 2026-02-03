#!/usr/bin/env python3
"""
StemLooper CLI - Entry point

Usage:
    python stemlooper.py track.mp3 --stems 6 --bars 4

Or install as command:
    pip install -e .
    stemlooper track.mp3 --stems 6 --bars 4
"""

from cli.main import main

if __name__ == "__main__":
    main()
