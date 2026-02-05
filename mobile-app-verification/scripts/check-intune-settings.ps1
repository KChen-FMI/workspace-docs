<#!
.SYNOPSIS
Read-only checks for Intune/Entra settings relevant to iOS Excel security.

.DESCRIPTION
- Lists iOS app protection policies and their data transfer settings
- Lists Conditional Access policies that require MFA and compliant devices

.NOTES
Requires Microsoft.Graph PowerShell modules and appropriate permissions.
#>

param(
  [string]$TenantId = ""
)

Write-Host "== Connect to Microsoft Graph ==" -ForegroundColor Cyan
if ($TenantId) {
  Connect-MgGraph -TenantId $TenantId -Scopes "Policy.Read.All","DeviceManagementApps.Read.All","DeviceManagementConfiguration.Read.All"
} else {
  Connect-MgGraph -Scopes "Policy.Read.All","DeviceManagementApps.Read.All","DeviceManagementConfiguration.Read.All"
}

Write-Host "\n== iOS App Protection Policies ==" -ForegroundColor Cyan
$policies = Get-MgDeviceAppManagementIosManagedAppProtection -All
$policies | Select-Object displayName, dataTransferLevel, managedBrowser, saveAsBlocked, allowCopyPaste, allowPrint, allowScreenCapture | Format-Table -AutoSize

Write-Host "\n== Conditional Access Policies (MFA + Compliant Device) ==" -ForegroundColor Cyan
$ca = Get-MgIdentityConditionalAccessPolicy -All
$ca | ForEach-Object {
  $mfa = ($_.GrantControls.BuiltInControls -contains "mfa")
  $compliant = ($_.GrantControls.BuiltInControls -contains "compliantDevice")
  if ($mfa -or $compliant) {
    [PSCustomObject]@{
      DisplayName = $_.DisplayName
      State = $_.State
      RequireMFA = $mfa
      RequireCompliantDevice = $compliant
    }
  }
} | Format-Table -AutoSize

Write-Host "\n== Done ==" -ForegroundColor Green
