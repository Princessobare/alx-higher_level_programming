#!/bin/bash
# Sends JSON POST request to URL with specified JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
