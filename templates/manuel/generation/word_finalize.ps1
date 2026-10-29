param([string]$Src, [string]$Dst, [string]$Pdf)
# Ouvre le brouillon dans Word, actualise le sommaire et les champs, enregistre le .docx final et exporte le PDF.
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
$w.AutomationSecurity = 3
$w.Options.UpdateFieldsAtPrint = $false
try {
    $d = $w.Documents.Open($Src, $false, $false, $false)
    "ouvert : $($d.Paragraphs.Count) paragraphes, $($d.InlineShapes.Count) images"
    foreach ($t in $d.TablesOfContents) { $t.Update() }
    $d.Fields.Update() | Out-Null
    foreach ($t in $d.TablesOfContents) { $t.Update() }
    $d.Repaginate()
    "pages : $($d.ComputeStatistics(2))"
    $d.SaveAs2($Dst, 16)
    $d.ExportAsFixedFormat($Pdf, 17)
    $d.Close(0)
    "ok"
} finally {
    $w.Quit()
}
