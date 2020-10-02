Add-Type -AssemblyName System.Windows.Forms

while ($true)
{
  $x = get-random -maximum 1000 -minimum 0
  $y = get-random -maximum 1000 -minimum 0
  $time = get-random -maximum 10 -minimum 0
  [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
  Start-Sleep -Seconds $time
}