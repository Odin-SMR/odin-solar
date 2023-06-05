#!/bin/bash
export AWS_PROFILE="${AWS_PROFILE:-odin-cdk}"
pushd "$(git rev-parse --show-toplevel)/app/handler" > /dev/null
python download.py
popd > /dev/null
