# Simple API with Lambda and CDK

A FastAPI application deployed as an AWS Lambda function triggered by AWS API Gateway.

The API provides greeting endpoints and interactive documentation via Scalar UI. Infrastructure is defined as code using CDK for easy deployment and management.

You can easily run the API locally (`uv run dev`), which allows for a nice developer experience while creating and modifying endpoints.

## Project Structure

```text
simple-api-lambda-cdk/
├── app/                    # FastAPI application
│   ├── handler.py          # Lambda handler and dev server
│   ├── models/             # Pydantic models
│   ├── routes/             # API route definitions
│   │   ├── greetings/      # Greeting endpoints
│   │   ├── docs.py         # Scalar UI documentation
│   │   └── version.py      # Version endpoint
│   └── services/           # Business logic services
├── cdk/                    # AWS CDK infrastructure
│   ├── app.py              # CDK app entry point
│   ├── cdk.json            # CDK configuration
│   └── stack.py            # CDK stack definition
├── pyproject.toml          # Project dependencies (uv)
└── README.md               # This file
```

## Prerequisites

- Python 3.13+
- AWS CLI configured with appropriate credentials
- AWS CDK CLI installed (`npm install -g aws-cdk`)
- `uv` package manager
- Docker for bundling the lambda code and dependencies

## Setup

1. **Install dependencies:**

   ```bash
   uv sync
   ```

2. **Bootstrap CDK (if not already done):**

   ```bash
   cd cdk
   cdk bootstrap
   ```

## Development

### Running the Development Server

To run the API locally for development:

```bash
# Start the development server with auto-reload
uv run dev
```

The development server will be available at:

- **API**: <http://localhost:8000>
- **Interactive Documentation**: <http://localhost:8000/docs>

The development server includes:

- Auto-reload on code changes
- Interactive API documentation via Scalar UI
- All API endpoints available locally

## Deployment

1. **Deploy the stack:**

   ```bash
   cd cdk
   cdk deploy
   ```

2. **Get the API Gateway URL:**
   After deployment, the CDK will output the API Gateway URL. You can also find it in the AWS Console.

### Typical workflow

1. `cdk bootstrap` (once per account/region)
2. `cdk synth` → check template (optional)
3. `cdk diff` → review changes (optional)
4. `cdk deploy` → deploy and create resources on AWS
5. `cdk destroy` → tear down when needed

#### Use caution with `cdk destroy`

`cdk destroy` destroys the resources you've defined in your CDK stack.

This will permanently delete your Lambda function, API Gateway, and any other AWS resources created by the stack. Make sure you want to remove everything before running this command.

- Some resources like CloudWatch Logs may be retained for a period after deletion, and S3 buckets with data may require manual cleanup.

- If you remove resources from the CDK code and redeploy, those **resources will be left over** in AWS since CDK only manages resources explicitly defined in the current stack.
  - Use the AWS CLI or AWS Resource Explorer in the AWS console to make sure there are no leftover resources

## Testing

### Local Testing

When running the development server locally, you can test the API at <http://localhost:8000>.

### Deployed Testing

Once deployed, you can test the Lambda function by making HTTP requests to the API Gateway URL. The root endpoint (`/`) automatically redirects to the interactive documentation.

### API Documentation

For complete API documentation and interactive testing, visit the Scalar UI at:

- **Local**: <http://localhost:8000/docs>
- **Deployed**: <https://your-api-gateway-url/docs>

The Scalar UI provides:

- Interactive API documentation
- Request/response examples
- Try-it-out functionality for all endpoints
- Schema definitions and validation rules

## Cleanup

To remove all resources:

```bash
cd cdk
cdk destroy
```

## Architecture

- **Lambda Function**: Python 3.13 runtime, 128MB memory, 30-second timeout
- **API Gateway**: HTTP API with CORS enabled
- **FastAPI Application**: Modern Python web framework with automatic OpenAPI generation
- **Documentation**: Scalar UI for interactive API documentation
- **Routes**: Modular route structure with greeting endpoints and version information
- **Logging**: CloudWatch Logs with 1-week retention

## Features

The API includes:

- FastAPI framework with automatic OpenAPI/Swagger generation
- Interactive documentation via Scalar UI
- Modular route organization
- Pydantic models for request/response validation
- CORS headers for web browser compatibility
- Development server with auto-reload
- Version endpoint for API versioning
