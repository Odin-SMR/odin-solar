#!/usr/bin/env python3

import aws_cdk as cdk

from app.app_stack import OdinSolarStack


app = cdk.App()
OdinSolarStack(app, "OdinSolar")

app.synth()
