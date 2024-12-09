import logging
from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

# Initialize Flask app
app = Flask(__name__)

# Initialize SparkSession
spark = SparkSession.builder.appName("microservice").getOrCreate()

# Reduce Spark log verbosity
spark.sparkContext.setLogLevel("WARN")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()  # Log to console
    ]
)
logger = logging.getLogger(__name__)

@app.route("/process", methods=["POST"])
def process_data():
    """
    Receive JSON data stream and return analysis results
    """
    try:
        logger.info("Received request to /process")
        data = request.get_json()
        logger.info(f"Request data: {data}")

        # Create temporary DataFrame
        df = spark.createDataFrame(data)

        # Perform simple data analysis
        result = df.groupBy("gender").agg(
            avg("salary").alias("average_salary"),
            count("*").alias("count")
        ).collect()

        # Convert results to JSON format
        result_json = [{"gender": row["gender"], "average_salary": row["average_salary"], "count": row["count"]} for row in result]
        logger.info(f"Analysis results: {result_json}")

        return jsonify(result_json), 200
    except Exception as e:
        logger.error(f"Error during processing: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    logger.info("Starting Flask app on port 5000")
    app.run(host="0.0.0.0", port=5000)
