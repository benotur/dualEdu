#!/bin/bash

mkdir 2025/{januar/{ZIL,SISL},februar/{ZIL,SISL},marec/{ZIL,SISL},april/{ZIL,SISL},maj/{ZIL,SISL},jun/{ZIL,SISL},jul/{ZIL,SISL},august/{ZIL,SISL},september/{ZIL,SISL},oktober/{ZIL,SISL},november/{ZIL,SISL},december/{ZIL,SISL}}

for month in januar februar marec april maj jun jul august september oktober november december; do
for sub in ZIL SISL; do
echo "Moje Poznamky" > 2025/$month/$sub/poznamky.txt
done
done
