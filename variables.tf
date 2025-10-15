variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-azure-function-app"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "East US"
}

variable "function_app_name" {
  description = "Name of the Azure Function App"
  type        = string
  default     = "func-echo-app"
}

variable "storage_account_name" {
  description = "Name of the storage account"
  type        = string
  default     = "stfuncecho"
}

variable "app_service_plan_name" {
  description = "Name of the App Service Plan"
  type        = string
  default     = "plan-function-app"
}
