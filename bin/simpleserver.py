#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////////////////////////////
# Kaptos Simple HTTP Server
# /////////////////////////////////////////////////////////////////////////////

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
### Builtins
import http.server
import socketserver
import os
import sys

os.chdir("kaptos")

try:
    PORT = int(sys.argv[1])
except ValueError:
    PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving Kaptos development UI at port", PORT)
    httpd.serve_forever()
