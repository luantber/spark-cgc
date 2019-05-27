import org.apache.spark.sql.SparkSession

object SimpleApp {
  def main(args: Array[String]) {
    val logFile = "ratings27.csv" // Should be some file on your system
    val spark = SparkSession.builder.appName("Simple Application").getOrCreate()
    val logData = spark.read.textFile(logFile).cache()
    val numAs = logData.filter(line => line.contains("1")).count()
    val numBs = logData.filter(line => line.contains("2")).count()
    println(s"Lines with 1: $numAs, Lines with 2: $numBs")
    spark.stop()
  }
}



// $ YOUR_SPARK_HOME/bin/spark-submit \
//   --class "SimpleApp" \
//   --master local[4] \
//   target/scala-2.12/simple-project_2.12-1.0.jar