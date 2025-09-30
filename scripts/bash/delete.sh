#!/bin/bash

months=(januar februar marec april maj jun jul august september oktober november december)
subs=(ZIL SISL)

for month in "${months[@]}"; do
    for sub in "${subs[@]}"; do
        rm -f "2025/$month/$sub/poznamky.txt"
        rmdir "2025/$month/$sub"
    done
    rmdir "2025/$month"
done

rmdir "2025"

