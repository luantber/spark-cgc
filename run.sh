./sbin/start-master.sh --host 127.0.0.1 &>log0.txt &  
./bin/spark-class org.apache.spark.deploy.worker.Worker spark://127.0.0.1:7077 -c 1 -m 1400M &>log1.txt &  
./bin/spark-class org.apache.spark.deploy.worker.Worker spark://127.0.0.1:7077 -c 1 -m 1400M &>log2.txt & 
./bin/spark-submit  run-example --master spark://127.0.0.1:7077 SparkPageRank web-Google.txt 100

