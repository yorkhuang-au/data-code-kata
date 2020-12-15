#!/bin/bash
python process.py /data/org.csv /data/tmp_masked

echo "first_name,last_name,address,birth_date" > /data/masked.csv
cat /data/tmp_masked/*.csv >> /data/masked.csv