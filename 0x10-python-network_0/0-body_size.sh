#!/usr/bin/env bash
# script to print content length

curl -sI "$1" | grep "Content-Length:" | awk '{ print($2); }'
