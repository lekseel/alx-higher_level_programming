#!/bin/bash
# a Bash script that sends a custom header variable
curl -s  "$1" -H "X-School-User-Id: 98"
