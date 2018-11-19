from sys import argv
from time import strftime
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from settings import get_config
config = None


def mapValues(element):
    return element[1]


def saveAsTextFile(element):

    timestamp = strftime("%Y-%m-%d_%H-%M-%S")

    element.repartition(1).saveAsTextFile(
        config.directory_out.format(timestamp=timestamp),
        'org.apache.hadoop.io.compress.GzipCodec'
    )
    return element


def run(sc, streaming_context):
    dstream = KafkaUtils.createDirectStream(
        streaming_context, config.topics, config.kairos)

    dstream.map(mapValues).foreachRDD(saveAsTextFile)

    streaming_context.start()
    streaming_context.awaitTermination()


def create_streaming_context(spark_context, checkpoint_directory, interval=60):
    streaming_context = StreamingContext(
        spark_context,
        interval
    )
    streaming_context.checkpoint(checkpoint_directory)
    return streaming_context


def create_spark_context(app_name):
    return SparkContext(appName=app_name)


if __name__ == "__main__":

    global config
    if len(argv) > 1:
        config = get_config(argv[1])
    else:
        config = get_config('dev')

    sc = create_spark_context(config.app_name)
    streaming_context = create_streaming_context(
        spark_context=sc,
        checkpoint_directory=config.checkpoint_directory,
        interval=config.interval_seconds
    )
    # manter sc pra ser compativel com sc do pyspark interativo
    run(sc, streaming_context)
