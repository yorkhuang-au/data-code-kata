import argparse
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_folder", help="CSV folder to be created", type=str)
    parser.add_argument("record_count", help="Record count.", type=int)
    args = parser.parse_args()

    print(args)
    csv_folder = args.csv_folder
    rec_cnt = int(args.record_count)
    print(rec_cnt)
    partition_cnt = int(rec_cnt / 16433100) + 1

    spark = SparkSession.builder.master('local[*]').appName("CreateCSV").getOrCreate()

    df_org = spark.range(1, rec_cnt, numPartitions=partition_cnt)\
        .withColumn('first_name', F.substring(F.md5(F.rand().cast('string')), 1, 10))\
        .withColumn('last_name', F.substring(F.md5(F.rand().cast('string')), 1, 10))\
        .withColumn('address', F.md5(F.rand().cast('string')))\
        .withColumn('birth_date', F.expr("date_add(to_date('1900-01-01'), cast(rand()*360*120 as int))"))\
        .drop('id')

    df_org.write.mode('overwrite').csv(csv_folder, header=False)
    spark.stop()

if __name__ == '__main__':
    main()