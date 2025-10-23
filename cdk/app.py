#!/usr/bin/env python3
"""
CDK App entry point for Simple Lambda deployment.
"""

import aws_cdk as cdk
from cdk.stack import SimpleLambdaStack


app = cdk.App()

# Create the stack
SimpleLambdaStack(
    app,
    "SimpleLambdaStack",
    description="Simple Lambda function with API Gateway",
    env=cdk.Environment(
        account=app.node.try_get_context("account"),
        region=app.node.try_get_context("region"),
    ),
)

app.synth()
