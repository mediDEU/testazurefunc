output "function_app_name" {
  description = "Name of the Azure Function App"
  value       = azurerm_linux_function_app.function.name
}

output "function_app_default_hostname" {
  description = "Default hostname of the Azure Function App"
  value       = azurerm_linux_function_app.function.default_hostname
}

output "function_app_id" {
  description = "ID of the Azure Function App"
  value       = azurerm_linux_function_app.function.id
}

output "resource_group_name" {
  description = "Name of the resource group"
  value       = azurerm_resource_group.rg.name
}
