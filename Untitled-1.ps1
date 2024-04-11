$environmentUrl = 'https://orgc25b23b3.api.crm.dynamics.com/' # change this
## Login if not already logged in
if ($null -eq (Get-AzTenant -ErrorAction SilentlyContinue)) {
   Connect-AzAccount | Out-Null
}
# Get an access token
$token = (Get-AzAccessToken -ResourceUrl $environmentUrl).Token
# Common headers
$baseHeaders = @{
   'Authorization'    = 'Bearer ' + $token
   'Accept'           = 'application/json'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}
# Invoke WhoAmI Function
Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Method Get -Headers $baseHeaders
| ConvertTo-Json
