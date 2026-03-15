$lines = [System.IO.File]::ReadAllLines("c:\Users\akash\OneDrive\Desktop\dg pest control\index.html")
if ($lines[743] -match "Video Showcase") {
    $lines[743] = '            <div class="video-wrapper">
                <iframe src="https://www.youtube.com/embed/WN44wteu6rg" title="Pest Control Work 2" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen></iframe>
            </div>'
    [System.IO.File]::WriteAllLines("c:\Users\akash\OneDrive\Desktop\dg pest control\index.html", $lines)
    Write-Host "Success!"
} else {
    Write-Host "Line 744 does not match Video Showcase. Checking lines around 740-750:"
    for ($i=735; $i -lt 750; $i++) {
        if ($lines[$i] -match "Video Showcase") {
            Write-Host "Found at index $i :"
            Write-Host $lines[$i]
            $lines[$i] = '            <div class="video-wrapper">
                <iframe src="https://www.youtube.com/embed/WN44wteu6rg" title="Pest Control Work 2" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen></iframe>
            </div>'
            [System.IO.File]::WriteAllLines("c:\Users\akash\OneDrive\Desktop\dg pest control\index.html", $lines)
            Write-Host "Replaced at index $i successfully"
        }
    }
}
