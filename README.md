# Microservices

## Requirements:
- For this project, we'll need to have Docker and Kubernetes installed.
- Follow the official documentation to install it.

## Setting up the Kubernetes Cluster:
- After Docker and Kubernetes (I am using minikube) are installed we'll set up our cluster.
- For this project, we'll need Kafka and Spark. To install it in the most simplar manner one can use helm.
- Follow this links to install them into your kubernetes cluster.
    - <a href="https://github.com/bitnami/charts/tree/main/bitnami/kafka"> Kafka</a>
    - <a href="https://github.com/bitnami/charts/tree/main/bitnami/spark"> Spark</a> 

- After everything is set up use `kubectl get all` to see all the things that are running on your kubernetes cluster.
- It should look like this:

- After Kafka and Spark are successfully installed you're now good to go.

## Get started:
- Now you can start creating kafka topics, write spark-jobs as per your requirements.
- You can find all the jobs written inside `src` directory.
- Bitnami image specifications are inside `images` directory.
- Sample data are placed inside `data` directory. They are named according to their topic for which they're used.
- Execute command inside the pods terminal.

```bash
# To execute a spark job
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 [PATH_TO_FILE]
```