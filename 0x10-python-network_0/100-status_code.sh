#!/bin/bash
# Sends GET request to specified URL and displays response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
