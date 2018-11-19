import json

from pyspark import SparkContext
from pyspark.sql import HiveContext
from pyspark.sql import Row

def mapRow(element):

    data = json.loads(element)
    return Row(
        id = data.get('id'),
        col1 = data.get('col1')
    )

def run(sc, hc):

    exemplo = [dict(id='123', col1='value1'), dict(id='124', col1='value2')]
    exemplo_json_list = map(lambda element: json.dumps(element), exemplo)

    rdd = sc.parallelize(exemplo_json_list)

    rdd = rdd.map(mapRow)

    dataFrame = hc.createDataFrame(rdd).select('id', 'col1')

    nameHiveTable = 'teste.test_mineiro_table'

    dataFrame.repartition(1).write.saveAsTable(nameHiveTable, mode="append")


def create_context():
    # Creates the Spark context
    sc = SparkContext(appName="hdfs2hive-test")

    # Creates the Hive context
    hiveContext = HiveContext(sc)
    hiveContext.setConf('hive.exec.dynamic.partition.mode', 'nonstrict')
    return sc, hiveContext


if __name__ == "__main__":
    sc, hc = create_context()
    run(sc, hc)

