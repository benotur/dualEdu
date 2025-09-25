#!/bin/bash

months=(januar februar marec april maj jun jul august september oktober november december)
subs=(ZIL SISL)

for month in "${months[@]}"; do
    for sub in "${subs[@]}"; do
        mkdir -p "2025/$month/$sub"
        echo "Moje Poznamky" > "2025/$month/$sub/poznamky.txt"
    done
done
