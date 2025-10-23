import datetime
from typing import Any

from aws_cdk import (
    BundlingOptions,
    CfnOutput,
    DockerImage,
    Duration,
    Stack,
    Tags,
    aws_apigatewayv2 as apigatewayv2,
    aws_apigatewayv2_integrations as apigatewayv2_integrations,
    aws_lambda as _lambda,
    aws_logs as logs,
)
from constructs import Construct


class SimpleLambdaStack(Stack):
    """CDK Stack for Simple Lambda with API Gateway."""

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Generate version based on deployment time
        deployment_time = datetime.datetime.now(datetime.timezone.utc)
        version = deployment_time.strftime("%Y.%m.%d.%H%M")

        # Create Lambda function with bundled dependencies
        lambda_function = _lambda.Function(
            self,
            "SimpleLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="app.handler.handler",
            code=_lambda.Code.from_asset(
                "../",
                bundling=BundlingOptions(
                    image=DockerImage.from_registry("python:3.13-slim"),
                    command=[
                        # Run pip install commands in a bash script
                        "bash",
                        "-c",
                        # Exit the script if any command fails (set -e)
                        "set -e; \
                        pip install --no-cache-dir --target /asset-output --platform linux_x86_64 --only-binary=:all: . --group lambda; \
                        cp -r app /asset-output",
                    ],
                ),
            ),
            memory_size=128,
            timeout=Duration.seconds(30),
            environment={
                "VERSION": version,
            },
            log_group=logs.LogGroup(
                self,
                "SimpleLambdaLogGroup",
                log_group_name="/aws/lambda/SimpleLambdaFunction",
                retention=logs.RetentionDays.ONE_WEEK,
            ),
            description=f"Simple Hello World Lambda function with external dependencies (v{version})",
        )

        # Create HTTP API Gateway
        http_api = apigatewayv2.HttpApi(
            self,
            "SimpleLambdaApi",
            description="API Gateway for Simple Lambda",
            cors_preflight=apigatewayv2.CorsPreflightOptions(
                allow_origins=["*"],
                allow_methods=[
                    apigatewayv2.CorsHttpMethod.GET,
                    apigatewayv2.CorsHttpMethod.POST,
                ],
                allow_headers=["Content-Type"],
            ),
        )

        # Create Lambda integration
        lambda_integration = apigatewayv2_integrations.HttpLambdaIntegration(
            "LambdaIntegration", lambda_function
        )

        # # Add route to the API
        # http_api.add_routes(
        #     path="/hello",
        #     methods=[apigatewayv2.HttpMethod.GET, apigatewayv2.HttpMethod.POST],
        #     integration=lambda_integration,
        # )

        # # Add root route
        # http_api.add_routes(
        #     path="/",
        #     methods=[apigatewayv2.HttpMethod.GET],
        #     integration=lambda_integration,
        # )

        # Add routes - catch all for FastAPI routing
        http_api.add_routes(
            path="/{proxy+}",
            methods=[apigatewayv2.HttpMethod.ANY],
            integration=lambda_integration,
        )

        # Output the API Gateway URL and version
        CfnOutput(
            self, "ApiUrl", value=http_api.url or "", description="API Gateway URL"
        )
        CfnOutput(self, "Version", value=str(version), description="Deployed version")

        # Add tags to all resources for easy identification and cleanup
        Tags.of(self).add("Environment", "test")
        Tags.of(self).add("Project", "super-cool-simple-api")
        Tags.of(self).add("Identifier", "2025.10.16.test")
        Tags.of(self).add("CreatedBy", "cdk")
