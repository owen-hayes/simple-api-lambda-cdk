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
    'SimpleLambdaStack01',
    lambda_id='SimpleLambdaFunction01',
    lambda_description='lambda_description01',
    api_id='SimpleLambdaApi01',
    api_description='api_description01',
    env=cdk.Environment(
        account=app.node.try_get_context("account"),
        region=app.node.try_get_context("region"),
    ),
)

app.synth()
