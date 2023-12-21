terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}
provider "azurerm" {
    subscription_id = var.subscripbtionID
    features {}
  
}

resource "azurerm_resource_group" "adam_lab_terraform_rg" {
    name                          = var.resourceGroupName
    location                      = var.location
#    provisioner "local-exec" {
#      command = "sleep 60"
#    }
}

resource "azurerm_virtual_network" "adam_lab_terraform_vnet" {
    name                          = var.vnet_name
    location                      = var.location
    resource_group_name           = var.resourceGroupName
    address_space                 = ["10.100.0.0/16"]
}

resource "azurerm_subnet" "adam_lab_terraform_10-100-100-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-100-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.100.0/24"]
  
}

resource "azurerm_subnet" "adam_lab_terraform_10-100-101-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-101-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.101.0/24"]
  
}

resource "azurerm_subnet" "adam_lab_terraform_10-100-102-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-102-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.102.0/24"]
  
}

resource "azurerm_subnet" "adam_lab_terraform_10-100-103-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-103-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.103.0/24"]
  
}

resource "azurerm_subnet" "adam_lab_terraform_10-100-104-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-104-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.104.0/24"]
  
}

resource "azurerm_subnet" "adam_lab_terraform_10-100-105-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-105-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.105.0/24"]
  
}
resource "azurerm_subnet" "adam_lab_terraform_10-100-106-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-106-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.106.0/24"]
  
}
resource "azurerm_subnet" "adam_lab_terraform_10-100-107-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-107-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.107.0/24"]
  
}
resource "azurerm_subnet" "adam_lab_terraform_10-100-108-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-108-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.108.0/24"]
  
}
resource "azurerm_subnet" "adam_lab_terraform_10-100-109-0-24-subnet" {
    name                         = "adam_lab_terraform_10-100-109-0-24-subnet"
    resource_group_name          = azurerm_resource_group.adam_lab_terraform_rg.name
    virtual_network_name         = azurerm_virtual_network.adam_lab_terraform_vnet.name
    address_prefixes             = [ "10.100.109.0/24"]
  
}