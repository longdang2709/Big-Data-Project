
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularTemp")
sc = SparkContext(conf = conf)

lines = sc.textFile("TexasTempNone.csv")
temps = lines.map(lambda x: (float(x.split(',')[3]), 1))
tempCounts = temps.reduceByKey(lambda x, y: x + y)

flipped = tempCounts.map(lambda (x,y) : (y,x) )
sortedTemp = flipped.sortByKey()

results = sortedTemp.collect()

for result in results:
    print(result)