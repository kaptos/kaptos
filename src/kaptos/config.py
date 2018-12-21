"""Kaptos configuration module."""

import toml

from appdirs import user_config_dir

config = toml.load(f"{user_config_dir('kaptos')}/config.toml")
