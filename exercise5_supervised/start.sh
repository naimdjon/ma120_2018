#!/bin/bash

docker run  --name scikit --rm -p 8888:8888 -v $(pwd):/code  -d smizy/scikit-learn && \
sleep 2 && \
docker logs scikit

