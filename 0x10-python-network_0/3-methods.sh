#!/bin/bash
# Display HTTP methods the server of specified URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
