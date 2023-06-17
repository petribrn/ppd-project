#!/bin/bash

pushd counters/docker

docker build --no-cache -t python-text-processor .

popd

pushd text-processor/docker

docker build --no-cache -t python-word-counter .

popd
