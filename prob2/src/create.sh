#!/bin/bash
# roughly 20G csv
python create.py /data/tmp_org 328662900

echo "first_name,last_name,address,birth_date" > /data/org.csv
cat /data/tmp_org/*.csv >> /data/org.csv
