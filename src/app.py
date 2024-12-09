from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

app = Flask(__name__)

# Initialize SparkSession
spark = SparkSession.builder.appName("microservice").getOrCreate()

# Reduce log verbosity
spark.sparkContext.setLogLevel("WARN")

@app.route("/process", methods=["POST"])
def process_data():
    """
    Receive JSON data stream and return analysis results
    """
    try:
        data = request.get_json()
        # Create a temporary DataFrame
        df = spark.createDataFrame(data)
        # Perform simple data analysis
        result = df.groupBy("gender").agg(
            avg("salary").alias("average_salary"),
            count("*").alias("count")
        ).collect()
        # Convert results to JSON format
        result_json = [{"gender": row["gender"], "average_salary": row["average_salary"], "count": row["count"]} for row in result]
        return jsonify(result_json), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
