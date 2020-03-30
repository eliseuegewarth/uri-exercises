#!/bin/bash
./auto_commit.sh
mkdir -p "$1" && ${EDITOR} "$1/$1.py";