#!/usr/bin/env bash
# script to print content length

curl -s "$1" | wc -c
