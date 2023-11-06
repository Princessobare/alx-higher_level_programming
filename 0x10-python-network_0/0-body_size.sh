#!/bin/bash
# Get size of bite of HTTP response header for given URL.
curl -s "$1" | wc -c
