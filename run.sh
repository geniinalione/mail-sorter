#!/bin/bash

if [ -d "data/inbox" ]; then
    echo "start mail-sorter"

    if command -v python3 >/dev/null 2>&1; then
        PY=python3
    elif command -v py >/dev/null 2>&1; then
        PY=py
    else
        PY=python
    fi

    "$PY" -m mailsorter.pipeline
    echo "end mail-sorter"
else
    echo "There is no data/inbox directory"
    exit 1
fi