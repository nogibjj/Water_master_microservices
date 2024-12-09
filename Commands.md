### 1. Running Kafka Producer
```bash
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test
```
### Running Kafka Consumer
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test
```

<hr>

### 2. Running Kafka Key-Value Pair Producer and execute Spark-job to Consume the topic

- Producer
```bash
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test_topic --property "parse.key=true" --property "key.separator=:"
```

- Execute Spark Job
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /tmp/read_test_stream.py
```

### 3. Other commands

- List Kafka Topics
```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

- Copy files from local to Kubernetes
```bash
kubectl cp [SOURCE_PATH] my-release-spark-worker-0:/tmp
```