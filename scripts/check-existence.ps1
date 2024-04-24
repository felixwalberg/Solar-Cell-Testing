. .\scripts\Core.ps1
. .\scripts\TableOperations.ps1
. .\scripts\CommonFunctions.ps1

# Input from python script, if there are additional fields added, add to this list of arguments.
$sample_id = $args[0]
$table_name = $args[1]
# $sample_id = 'NiOx_dppp_3_14d_5R_102735'

Connect 'https://orgc25b23b3.api.crm.dynamics.com/'

Invoke-DataverseCommands {
    # Write-Host "Checking to see if: '$($sample_id)' exists in '$($table_name)'"

    $retrieveExistingSample = Get-Records `
      -setName $table_name `
      -query '?$select=cr69a_sampleid,cr69a_pce'
    
    $found = $false
    foreach ($sample in $retrieveExistingSample.value) {
        if($sample.cr69a_sampleid -eq $sample_id)
        {
            $found = $true
            Write-Host "Is sample: $($sample.cr69a_sampleid) $($sample.cr69a_pce) the correct sample?" `
        }
     }
    if($found -eq $false){
        Write-Host "Invalid"`
    }
    # if($retrieveExistingSample.cr69a_sampleid -eq $NULL) {
    #     Write-Host "Value does not exist in dataframe, fill out metadata before entering data."
    # }
    # else {
    #     Write-Host "Is sample: '$($retrieveExistingSample.cr69a_sampleid)' the correct sample?"
    # }
    
}
