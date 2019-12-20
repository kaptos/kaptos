#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Kaptos - SimpleHTTPServer

Project:
    Kaptos

Changelog:
    See CHANGELOG.md

Todo:
    See TODO.md

Notes:
    None

.. document private functions
"""

# /////////////////////////////////////////////////////////////////////////////
# Kaptos Simple HTTP Server
# Author: VA7EXE <58346471+VA7EXE@users.noreply.github.com>
# /////////////////////////////////////////////////////////////////////////////

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
### Builtins
import http.server
import socketserver
import os

os.chdir("kaptos")

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving Kaptos development UI at port", PORT)
    httpd.serve_forever()