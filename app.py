#!/usr/bin/env python3

from aws_cdk import core

from cdk_hack.cdk_hack_stack import CdkHackStack


app = core.App()
CdkHackStack(app, "cdk-hack", env=core.Environment(account="987092829714", region="us-west-2"))

app.synth()
