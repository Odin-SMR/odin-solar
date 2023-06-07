#!/bin/bash
pushd $(git rev-parse --show-toplevel) > /dev/null
pip install -U pip-tools
# build runtime requirements
pip-compile -q \
    requirements.in \
    --resolver=backtracking
# build development requirements
pip-compile -q \
    requirements-dev.in \
    requirements.txt \
    -o requirements-dev.txt \
    --resolver=backtracking
popd > /dev/null