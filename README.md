# cis_baseline_csv
Transform CIS security baselines into CSV files with all controls and titles.


### syntax

```
first extract readable text from the first 50 pages
$ pdf2txt.py .\CIS_Red_Hat8.pdf -m 50 -t text -o CIS_Red_Hat8.pdf_extract.txt CIS_Red_Hat8.pdf

then use
$ python3 cis_to_csv.py .\CIS_Red_Hat8.pdf_extract.txt
```


### example

```
$ python3 cis_to_csv.py .\CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.0.pdf
```


### bulk example

```powershell
Get-ChildItem '..\CIS benchmarks\' -Filter *.pdf | ForEach-Object {
    python3 cis_to_csv.py ('..\CIS benchmarks\' + $_)
}
```


### example output
```
done! saved results in ./..\CIS benchmarks\text_versions\CIS_Microsoft_Windows.pdf_extract.csv
```
