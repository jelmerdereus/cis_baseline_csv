# cis_baseline_csv
Transform CIS security baselines into CSV files with all controls and titles.

### requirements
Install pdfminer for it's CLI tool pdf2txt.py


### usage

```
first extract readable text from the first 50 pages
$ pdf2txt.py .\CIS_Red_Hat8.pdf -m 50 -t text -o CIS_Red_Hat8.pdf_extract.txt CIS_Red_Hat8.pdf

then use
$ python3 cis_to_csv.py .\CIS_benchmarks\CIS_Red_Hat8.pdf_extract.txt
```

### bulk example

###### Powershell
```powershell
Get-ChildItem '..\CIS benchmarks\' -Filter *.pdf_extract.txt | ForEach-Object {
  python3 cis_to_csv.py ('..\CIS_benchmarks\' + $_)
}
```

###### Bourne shell
```shell
for f in ./CIS_benchmarks/*_extract.txt; do
  python3 cis_to_csv.py $f
done
```
