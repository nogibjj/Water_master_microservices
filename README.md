[![CI Pipeline](https://github.com/nogibjj/Water_master_microservices/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Water_master_microservices/actions/workflows/ci.yml)
# Microservices for Kafka and Spark Stream Processing

## Overview

This project implements a comprehensive microservices-based architecture for stream processing using Apache Kafka and Apache Spark. The microservice processes JSON-based data streams in real-time, enabling analysis and transformations, such as salary aggregation and gender distribution analysis. Key highlights of the project include containerization with Docker, deployment with Kubernetes, integration of Serverless Framework for Infrastructure as Code (IaC), and a robust CI/CD pipeline to ensure code quality and automated testing.

The main functionalities of the project are:
- Real-time ingestion and transformation of JSON data using Kafka and Spark.
- Statistical analysis of data streams, such as calculating average salaries and counting records by gender or birth month.
- Flask-based RESTful API that interacts with the Spark data pipeline.
- Performance benchmarking with Locust to evaluate scalability and reliability.

The microservices are optimized for portability, scalability, and monitoring, with emphasis on distributed data pipelines for high-throughput applications.

## Features

- **Real-time Data Stream Processing**: Uses Apache Spark and Kafka to process and analyze large-scale streaming data.
- **Microservices Architecture**: Developed with Flask for seamless interaction with data pipelines.
- **Containerization**: Dockerized microservices ensure portability and environment consistency.
- **Infrastructure as Code**: Utilizes Serverless Framework for cloud resource provisioning and management.
- **Load Testing**: Comprehensive performance benchmarking with Locust.
- **Continuous Integration/Continuous Delivery**: Automated CI/CD pipeline ensures deployment reliability.

## Requirements

1. **Install Docker**:
   - Follow the [Docker installation guide](https://docs.docker.com/get-docker/).
2. **Install Kubernetes**:
   - Follow the [Kubernetes installation guide](https://kubernetes.io/docs/tasks/tools/).
3. **Install Helm**:
   - Kafka: [Bitnami Kafka Chart](https://github.com/bitnami/charts/tree/main/bitnami/kafka)
   - Spark: [Bitnami Spark Chart](https://github.com/bitnami/charts/tree/main/bitnami/spark)
4. **Install Locust for Load Testing**:
   ```bash
   pip install locust
   ```

## How to Run

### Setting up the Kubernetes Cluster

1. **Start Minikube**:
   ```bash
   minikube start
   ```
2. **Deploy Kafka and Spark using Helm**:
   ```bash
   helm repo add bitnami https://charts.bitnami.com/bitnami
   helm install kafka bitnami/kafka
   helm install spark bitnami/spark
   ```
3. **Verify Deployment**:
   ```bash
   kubectl get all
   ```

### Running the Microservices

1. **Build the Docker Image**:
   ```bash
   docker build -t microservice .
   ```
2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 microservice
   ```
3. **Test the Flask API**:
   ```bash
   curl -X POST http://localhost:5000/process \
        -H "Content-Type: application/json" \
        -d '[{"id": 1, "gender": "M", "salary": 5000}, {"id": 2, "gender": "F", "salary": 6000}]'
   ```

## Load Testing

### Performance Observations

**Test Details:**
- Users: 100 concurrent users.
- Ramp-up Rate: 10 users per second.
- Test Duration: 1 minute.

**Results:**
- Total Requests: 634
- Average Latency: 8091ms
- Minimum Latency: 4912ms
- Maximum Latency: 16845ms
- Median Latency: 7600ms

**Key Issues Identified:**
1. **High Latency**: The average latency remains above 8000ms, with some requests exceeding 16000ms.
2. **Limited Throughput**: The system failed to achieve the target of 10,000 requests per second. The peak throughput was approximately 15.6 requests/second.

**Potential Bottlenecks:**
- Spark Job Overhead: Processing large JSON objects in Spark introduces additional latency.
- Kafka Configuration: Suboptimal broker settings may limit message throughput.
- Flask API: Single-threaded Flask may not handle high concurrency effectively.

**Future Improvements:**
- Optimize Spark jobs by caching intermediate results or partitioning data more effectively.
- Improve Kafka broker configurations (e.g., increase replication factor and partitions).
- Replace Flask with a more scalable framework like FastAPI or deploy Flask with Gunicorn.
- Implement distributed caching (e.g., Redis) to reduce repeated computations.

## Infrastructure as Code (IaC)

This project utilizes the **Serverless Framework** for managing cloud infrastructure resources. The framework simplifies the provisioning of services like Kafka topics and AWS Lambda functions, ensuring consistent deployments.

## Quantitative Assessment

| Metric              | Value                |
|---------------------|----------------------|
| Total Requests      | 634                 |
| Average Latency     | 8091ms              |
| Minimum Latency     | 4912ms              |
| Maximum Latency     | 16845ms             |
| Median Latency      | 7600ms              |
| Error Rate          | 0% (0 failures)     |

## Architectural Diagram

*Insert diagram here.*

## Demo Video

[Click here to view the demo video.](https://youtu.be/x2pgzh_cPSs)

## AI Pair Programming Tools Used

1. **GitHub Copilot**:
   - Suggested efficient ways to integrate Spark and Kafka.
   - Streamlined the development of RESTful API endpoints.
2. **TabNine**:
   - Provided intelligent autocompletions for Spark transformations and Flask code.
   - Enhanced the quality of code structure and SQL-like operations.

## Project Features vs. Rubric Mapping

| Feature/Code Component          | Rubric Requirement                          |
|---------------------------------|---------------------------------------------|
| Flask API (src/app.py)          | Microservice Implementation                |
| Dockerfile                      | Containerization with Distroless           |
| Logging (src/app.py)            | Use of Logging                              |
| Locust Load Testing             | Successful Load Test                        |
| Spark Scripts (e.g., count_gender.py) | Data Engineering                         |
| Serverless Framework            | Infrastructure as Code                     |
| GitHub Actions Workflow (.github/workflows/ci.yml) | CI/CD Setup                        |
| README.md                       | Comprehensive Documentation                |
| Architectural Diagram           | Clear Architecture Representation          |
| .devcontainer Config            | GitHub/GitLab Configurations               |

## Directory Structure

```
project-root/
│
├── .devcontainer/             # Docker configuration for GitHub Codespaces
│   ├── Dockerfile
│   ├── devcontainer.json
│
├── src/                       # Source code for microservices
│   ├── app.py                 # Flask API for data processing
│   ├── load_test.py           # Locust script for load testing
│   ├── count_gender.py        # Spark job: Count records by gender
│   ├── count_month.py         # Spark job: Count records by birth month
│   ├── final_analysis.py      # Spark job: Comprehensive analysis
│   ├── read_emp_data.py       # Spark job: Read employee data
│   ├── read_json_from_topic.py # Spark job: Read data from Kafka
│
├── data/                      # Sample data for testing
│   ├── emp_data.json
│   ├── json_topic.json
│
├── images/                    # Helm chart specifications for Kafka and Spark
│   ├── kafka.yml
│   ├── spark.yml
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── Commands.md                # Commands documentation
```
