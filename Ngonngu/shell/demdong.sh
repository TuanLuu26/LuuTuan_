#!/bin/bash
FILE="$HOME/LuuTuan_2400232/Sanpham/SP2/banggia.csv"
echo "So dong: $(wc -l < "$FILE")"
echo "So ky tu: $(wc -m < "$FILE")"
