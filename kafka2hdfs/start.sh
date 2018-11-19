#!/bin/bash

PREFIX="/home/streamer/projetos/kafka2hdfs/"
VENDORS="/home/streamer/projetos/streamings/vendors"
PORT=$(( $RANDOM % 1000 + 40000 ))

spark-submit \
	--master yarn-client \
    	--driver-class-path /etc/hive/conf \
    	--conf spark.sql.hive.convertMetastoreParquet=false \
    	--conf spark.executor.memory=2g \
    	--conf spark.executor.extraJavaOptions="-XX:MaxPermSize=2048M" \
    	--conf spark.driver.memory=2g \
    	--conf spark.dynamicAllocation.initialExecutors=1 \
    	--conf spark.dynamicAllocation.minExecutors=1 \
    	--conf spark.dynamicAllocation.maxExecutors=2 \
		--conf spark.ui.port=${PORT} \
    	--jars ${VENDORS}/spark-streaming-kafka-assembly_2.10-1.6.1.jar \
	--queue juvenal \
    	${PREFIX}/kafka2hdfs.py $1
