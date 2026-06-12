# Airline Reservation Platform

## Project Overview

The Airline Reservation Platform is a microservices-based application designed to manage airline bookings, payments, and ticket generation. The project demonstrates modern software development and DevOps practices by integrating containerization, CI/CD pipelines, Kubernetes orchestration, monitoring, and cloud deployment.

The platform is built using Python Flask microservices and MySQL, with deployment automated through Docker, Jenkins, Kubernetes, and AWS EC2.

---

## Architecture

The system consists of the following microservices:

### Booking Service

* Handles flight booking requests.
* Stores booking information in MySQL.
* Provides APIs to create and retrieve bookings.

### Payment Service

* Simulates payment processing.
* Provides payment-related APIs.

### Ticket Service

* Generates ticket information.
* Provides ticket-related APIs.

### Database

* MySQL database used to store booking records.

---

## System Architecture

User
↓
Booking Service
↓
MySQL Database

User
↓
Payment Service

User
↓
Ticket Service

CI/CD Flow:

GitHub
↓
Jenkins
↓
Docker Build
↓
Docker Containers
↓
Kubernetes Deployment
↓
AWS EC2 Deployment

Monitoring Flow:

Prometheus
↓
Grafana Dashboards

---

## Technology Stack

### Backend

* Python
* Flask
* REST APIs

### Database

* MySQL

### Containerization

* Docker
* Docker Compose

### CI/CD

* Jenkins

### Container Orchestration

* Kubernetes
* Deployments
* Services
* Ingress
* Secrets
* Persistent Volumes

### Monitoring

* Prometheus
* Grafana

### Cloud

* AWS EC2

---

## Key Features

* Microservices architecture
* RESTful APIs
* Containerized deployment
* Automated CI/CD pipeline
* Kubernetes orchestration
* Persistent database storage
* Secret management
* Monitoring and observability
* Cloud deployment on AWS

---

## Docker Deployment

Build and start all services:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

Stop services:

```bash
docker compose down
```

---

## Jenkins CI/CD Pipeline

The Jenkins pipeline performs:

1. Source code checkout from GitHub
2. Docker image build
3. Service validation
4. Deployment execution

Benefits:

* Automated builds
* Faster deployments
* Reduced manual effort
* Continuous integration workflow

---

## Kubernetes Deployment

The application was deployed to Kubernetes using:

### Deployments

* Booking Service Deployment
* Payment Service Deployment
* Ticket Service Deployment
* MySQL Deployment

### Services

* Internal service communication
* External access through NodePort

### Secrets

* Secure database credentials

### Persistent Volume Claims

* Database persistence across pod restarts

### Ingress

* Centralized routing for services

---

## Monitoring and Observability

Prometheus was integrated to collect cluster metrics.

Grafana dashboards were configured to monitor:

* CPU utilization
* Memory utilization
* Pod health
* Service status
* Cluster performance

---

## AWS EC2 Deployment

The platform was deployed on an AWS EC2 Ubuntu instance.

Deployment steps:

1. Launch EC2 instance
2. Configure Security Groups
3. Install Docker
4. Clone GitHub repository
5. Deploy using Docker Compose

Application services are exposed through public ports:

* Booking Service → Port 5000
* Payment Service → Port 5001
* Ticket Service → Port 5002

---

## Challenges Solved

During development and deployment, several real-world issues were addressed:

* Jenkins Docker socket permissions
* Docker installation inside Jenkins container
* Kubernetes ImagePullBackOff errors
* MySQL database connectivity issues
* Persistent storage configuration
* Ingress networking configuration
* AWS EC2 deployment troubleshooting

---

## Learning Outcomes

This project provided hands-on experience with:

* Microservices architecture
* Containerization
* CI/CD implementation
* Kubernetes administration
* Cloud deployment
* Infrastructure monitoring
* DevOps workflows

---

## Future Enhancements

* AWS RDS integration
* Terraform Infrastructure as Code
* HTTPS with SSL certificates
* Custom domain configuration
* GitHub Actions CI/CD
* Load balancing and auto-scaling

---

## Author

Payal Kunwar

Built as a practical DevOps and Cloud Engineering project to demonstrate end-to-end application deployment using modern cloud-native technologies.
