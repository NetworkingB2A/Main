
setting up a home lab
- input a payment method  
  - need a Credit card 
    - access this under billing profile > payment methods
    - cost management + billing | billing account | billing profile | payment methods
- create a new subscription
- create a resouce group
  - decide where you want your resource group to reside
- create a vnet
  - I will start by creating a very basic one with no NSG or bastionhost, ect
  - assign a network to the vnet
- create a subnet
  - you can assign this subnet to the vnet
  - you can only create a subnet inside a vnet ( as far as i know)
  - peering to hub
  - I have created 3 vnets

Terraform
- install terraform
- install azure cli on host
  - https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
  - 
- login to azure on vm
  - ➜  terraform training git:(main) ✗ az login
    A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is    available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
    ^C%                                                                                                                                                                                        
    ➜  terraform training git:(main) ✗ az login --use-device-code 
    To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code RNM7DFMNH to authenticate.
    
    Things i need to look up
    - what is a gateway subnet?
      - really only used if you want to connect on prem
      - vpn gateway or express route
    - securing devices to the internet