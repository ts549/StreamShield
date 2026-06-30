$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$version = "1.9.3"
$zip = Join-Path $here "mediamtx.zip"
$exe = Join-Path $here "mediamtx.exe"

if (-not (Test-Path $exe)) {
    $url = "https://github.com/bluenviron/mediamtx/releases/download/v$version/mediamtx_v${version}_windows_amd64.zip"
    Write-Host "Downloading MediaMTX v$version..."
    Invoke-WebRequest -Uri $url -OutFile $zip
    Expand-Archive -Path $zip -DestinationPath $here -Force
    Remove-Item $zip
}

& $exe (Join-Path $here "mediamtx.yml")
