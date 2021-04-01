# cis_baseline_csv
Transform CIS security baseline PDF documents into CSV files with all controls and titles. Use Python 3

### example output



### syntax

```
$ python3 cis_to_csv.py .\CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.0.pdf
```


### example

```
$ python3 cis_to_csv.py .\CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.0.pdf
```


### bulk example

```powershell
Get-ChildItem '..\CIS benchmarks\' -Filter *.pdf | ForEach-Object {
    python cis_to_csv.py ('..\CIS benchmarks\' + $_)
}
```
