#!/bin/bash

docker run --rm -v $(pwd)/src:/src -v $(pwd)/data:/data lfs_docker "python" "parse.py" "/data/spec.json" "/data/my.data" "/data/my.csv"
