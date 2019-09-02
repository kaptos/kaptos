"""Kaptos configuration module."""

import appdirs
import toml

config = toml.load(f"{appdirs.user_config_dir('kaptos')}/config.toml")
