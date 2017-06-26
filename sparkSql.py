
from pyspark.sql import SparkSession
from pyspark.sql import Row

import collections

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("SparkSQL").getOrCreate()

def mapper(line):
    fields = line.split(',')
    return Row(sc=int(fields[0]), division=str(fields[1]), yearmonth=int(fields[2]), tavg=float(fields[3]),
               tmin=float(fields[4]), tmax=float(fields[5]), pcp=float(fields[6]), pdsi=float(fields[7]),
                phdi=float(fields[8]),zndx=float(fields[9]), pmdi=float(fields[10]), cdd=float(fields[11]),
              hdd=float(fields[12]), sp01=float(fields[13]), sp02=float(fields[14]), sp03=float(fields[15]),
              sp06=float(fields[16]), sp09=float(fields[17]),sp12=float(fields[18]), sp24=float(fields[19]))

lines = spark.sparkContext.textFile("TexasTempNone.csv")
x = lines.map(mapper)

schemaPcP = spark.createDataFrame(x).cache()
schemaPcP.createOrReplaceTempView("x")

pcps = spark.sql("SELECT yearmonth, pcp FROM x ORDER BY pcp DESC ")

for pcp in pcps.collect():
  print(pcp)


spark.stop()
