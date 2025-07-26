# Define target folder and files
$folder = "C:\Users\Owner\Documents\PatMcD\1. Genealogy\McDonnellGitHubSite\Songs\FolkSongs"
$inputPath = Join-Path $folder "authors.json"
$outputPath = Join-Path $folder "authors-cleaned.json"

# Confirm paths are correct
Write-Host "Reading from: $inputPath"
Write-Host "Writing to:   $outputPath"

# Load input file (with error catch)
try {
    $rawAuthors = Get-Content $inputPath -Raw | ConvertFrom-Json
} catch {
    Write-Host "❌ ERROR reading $inputPath"
    pause
    exit
}

# Define known separators
$separators = @(", and ", " and ", ",", ";")

# Split names using separators
$allAuthors = @()
foreach ($entry in $rawAuthors) {
    $temp = @($entry)
    foreach ($sep in $separators) {
        $temp = $temp -replace $sep, "|"
    }
    $allAuthors += $temp -split "\|"
}

# Clean and sort list
$cleanAuthors = $allAuthors |
    ForEach-Object { $_.Trim() } |
    Where-Object { $_ -ne "" } |
    Sort-Object -Unique

# Output the result
$cleanAuthors | ConvertTo-Json -Depth 1 | Set-Content $outputPath -Encoding UTF8

Write-Host "`n✅ Created authors-cleaned.json with $($cleanAuthors.Count) entries."
pause
