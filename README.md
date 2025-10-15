# testazurefunc

A Terraform-based implementation for provisioning an Azure Function App with a simple echo function implemented in Python.

## Overview

This repository contains:
- **Terraform Infrastructure**: Provisions Azure resources (Resource Group, Storage Account, App Service Plan, Function App)
- **Python Azure Function**: A simple echo function that returns the input data back to the caller

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) >= 1.0
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- Azure subscription
- Python 3.9+

## Project Structure

```
.
├── main.tf                  # Main Terraform configuration
├── variables.tf             # Terraform variables
├── provider.tf              # Azure provider configuration
├── pyfunc.py               # Python echo function reference implementation
├── EchoFunction/           # Azure Function directory
│   ├── __init__.py         # Function implementation
│   └── function.json       # Function binding configuration
├── host.json               # Azure Functions runtime configuration
└── requirements.txt        # Python dependencies
```

## Usage

### 1. Authenticate with Azure

```bash
az login
```

### 2. Initialize Terraform

```bash
terraform init
```

### 3. Review the Terraform Plan

```bash
terraform plan
```

### 4. Deploy the Infrastructure

```bash
terraform apply
```

### 5. Test the Echo Function

After deployment, you can test the function using curl:

```bash
# Using query parameters
curl "https://<function-app-name>.azurewebsites.net/api/EchoFunction?name=test&message=hello"

# Using POST with JSON body
curl -X POST "https://<function-app-name>.azurewebsites.net/api/EchoFunction" \
  -H "Content-Type: application/json" \
  -d '{"data": "Hello, Azure Functions!"}'
```

### 6. Clean Up Resources

```bash
terraform destroy
```

## Configuration

You can customize the deployment by modifying variables in `variables.tf` or by creating a `terraform.tfvars` file:

```hcl
resource_group_name   = "my-resource-group"
location              = "West US"
function_app_name     = "my-function-app"
storage_account_name  = "myfuncstorageacct"
app_service_plan_name = "my-app-service-plan"
```

## Echo Function

The echo function accepts:
- **GET requests** with query parameters (`name`, `message`)
- **POST requests** with JSON body

It returns the input data back to the caller with a success message.
