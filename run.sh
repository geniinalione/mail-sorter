#!/bin/bash

if [ -d "data/inbox" ]; then
    echo "start mail-sorter"
    python3 -m mailsorter.pipeline
    echo "end mail-sorter"
else
    echo "There is no data/inbox directory"
    exit 1
fi