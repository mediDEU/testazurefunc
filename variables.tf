variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-azure-function-test"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "East US"
}

variable "storage_account_name" {
  description = "Name of the storage account"
  type        = string
  default     = "stfunctest"
}

variable "app_service_plan_name" {
  description = "Name of the app service plan"
  type        = string
  default     = "asp-function-test"
}

variable "function_app_name" {
  description = "Name of the function app"
  type        = string
  default     = "func-echo-test"
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default = {
    Environment = "Development"
    Project     = "Azure Function Test"
  }
}
