#!/bin/bash
export AWS_PROFILE="${AWS_PROFILE:-odin-cdk}"
pushd "$(git rev-parse --show-toplevel)/app/handler" > /dev/null
python -m handler_modules.download
popd > /dev/null
