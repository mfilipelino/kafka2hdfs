# config


class BaseConfig(object):
    interval_seconds = 60
    topics = ['topic-test']
    kairos = {
        "metadata.broker.list": "broker-1:9092,broker-2.b2w:9092,broker-3.b2w:9092",
        "auto.offset.reset": "smallest"
    }


class DevConfig(BaseConfig):
    app_name = 'kafka2hdfs-dev'
    checkpoint_directory = '/user/mfilipelino/checkpoint/'
    # hdfs
    directory_out = '/user/mfilipelino/files/{timestamp}'


