# Path to your HTML file
$htmlPath = "Tracks.html"

# Output path
$outputPath = "authors.json"

# Read the full HTML content as one string
$htmlContent = Get-Content $htmlPath -Raw

# Extract data-author values using a broader regex
$authors = [regex]::Matches($htmlContent, 'data-author\s*=\s*"(.*?)"') | ForEach-Object {
    $_.Groups[1].Value.Trim()
}

# Remove duplicates, sort alphabetically
$uniqueAuthors = $authors | Sort-Object -Unique

# Output to JSON
$uniqueAuthors | ConvertTo-Json -Depth 1 | Set-Content $outputPath -Encoding UTF8

Write-Host "Extracted $($uniqueAuthors.Count) unique authors to $outputPath"
