import argparse
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_filename", help="Input CSV filename", type=str)
    parser.add_argument("masked_csv_folder", help="Masked CSV folder", type=str)
    args = parser.parse_args()

    print(args)
    csv_filename = args.csv_filename
    spark = SparkSession.builder.master('local[*]').appName("processCSV").getOrCreate()

    df_masked = spark.read.csv(csv_filename, header=True)\
        .withColumn('first_name', F.md5('first_name'))\
        .withColumn('last_name', F.md5('last_name'))\
        .withColumn('address', F.md5('address'))

    df_masked.write.mode('overwrite').csv(args.masked_csv_folder, header=False)
    spark.stop()

if __name__ == '__main__':
    main()