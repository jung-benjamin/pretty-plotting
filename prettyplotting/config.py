#! /usr/bin/env python3
"""Configuration for prettyplotting."""

import tomllib
from pathlib import Path


def load_config():
    """Load the configuration from prettyplotting.toml."""
    config_files = [
        Path("prettyplotting.toml"),
        Path("config/prettyplotting.toml")
    ]
    for config_file in config_files:
        if config_file.exists():
            with open(config_file, "rb") as f:
                cfg = tomllib.load(f)
            return cfg
    return {}
