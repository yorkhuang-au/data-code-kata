#!/bin/bash
docker run --rm -v $(pwd)/src:/src -v $(pwd)/data:/data lfs_spark_docker "./create.sh"
