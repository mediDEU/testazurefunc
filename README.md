# Azure Function App with Terraform

This repository contains a Terraform-based implementation for provisioning an Azure Function App with a simple Python echo function.

## Overview

The project deploys the following Azure resources:
- Resource Group
- Storage Account
- App Service Plan (Consumption/Linux)
- Linux Function App with Python 3.11 runtime

## Function Implementation

### EchoFunction
A simple HTTP-triggered function that echoes back the message sent to it.

**Endpoint:** `/api/EchoFunction`

**Parameters:**
- `message` (query string or JSON body): The message to echo back

**Example Usage:**
```bash
# Query string
curl "https://<function-app-name>.azurewebsites.net/api/EchoFunction?message=Hello"

# JSON body
curl -X POST "https://<function-app-name>.azurewebsites.net/api/EchoFunction" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from JSON"}'
```

## Project Structure

```
.
├── main.tf              # Main Terraform configuration with Azure resources
├── variables.tf         # Variable definitions
├── provider.tf          # Provider configuration
├── outputs.tf           # Output definitions
├── host.json            # Azure Functions host configuration
├── requirements.txt     # Python dependencies
├── EchoFunction/
│   ├── pyfunc.py       # Python function implementation
│   └── function.json   # Function binding configuration
└── README.md           # This file
```

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) >= 1.0
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- Azure subscription

## Usage

### 1. Azure Authentication

```bash
az login
az account set --subscription "<your-subscription-id>"
```

### 2. Initialize Terraform

```bash
terraform init
```

### 3. Plan Deployment

```bash
terraform plan
```

### 4. Deploy Infrastructure

```bash
terraform apply
```

### 5. Deploy Function Code

After the infrastructure is deployed, you can deploy the function code using:

```bash
# Create a zip package
zip -r function.zip host.json requirements.txt EchoFunction/

# Deploy using Azure CLI
az functionapp deployment source config-zip \
  -g <resource-group-name> \
  -n <function-app-name> \
  --src function.zip
```

## Configuration

You can customize the deployment by modifying variables in `variables.tf` or by creating a `terraform.tfvars` file:

```hcl
resource_group_name   = "my-resource-group"
location              = "East US"
storage_account_name  = "mystorageaccount"
app_service_plan_name = "my-app-service-plan"
function_app_name     = "my-function-app"

tags = {
  Environment = "Production"
  Project     = "My Project"
}
```

## Outputs

After deployment, Terraform will output:
- `function_app_name`: Name of the deployed Function App
- `function_app_default_hostname`: Hostname to access the function
- `function_app_id`: Azure resource ID
- `resource_group_name`: Name of the resource group

## Clean Up

To destroy all resources:

```bash
terraform destroy
```

## License

MIT
