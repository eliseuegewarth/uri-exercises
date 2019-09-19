#!/bin/bash
./auto_commit.sh
mkdir -p "$1" && subl "$1/$1.py";