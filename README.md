# AI Cloud Support Assistant

AI-powered cloud support application built with **Terraform, Docker, Amazon ECS Fargate, Application Load Balancer (ALB), and Amazon Bedrock**.

This project demonstrates how to deploy a containerized AI application on AWS using Infrastructure as Code (Terraform). Users can submit AWS-related questions through a web interface and receive AI-generated responses powered by Amazon Bedrock.

## Project Overview

The application consists of:

- Flask-based web application
- Docker container
- Amazon ECR repository
- Amazon ECS Fargate service
- Application Load Balancer
- Amazon Bedrock integration
- Terraform-managed infrastructure
- IAM role-based authentication
- CloudWatch logging

## Architecture
User
   │
   ▼
Application Load Balancer
   │
   ▼
ECS Fargate Service
   │
   ▼
Docker Container (Flask Application)
   │
   ▼
Amazon Bedrock (Nova Lite)
   │
   ▼
AI Generated Response

## Architecture Diagram
                    ┌─────────────┐
                    │    User     │
                    └──────┬──────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ Application Load       │
              │ Balancer (ALB)         │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ ECS Fargate Service    │
              │ Flask Application      │
              └───────────┬────────────┘
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
 ┌──────────────────┐         ┌──────────────────┐
 │ IAM Task Role    │         │ CloudWatch Logs  │
 │ Bedrock Access   │         │ Monitoring       │
 └────────┬─────────┘         └──────────────────┘
          │
          ▼
 ┌──────────────────┐
 │ Amazon Bedrock   │
 │ Nova Lite Model  │
 └──────────────────┘

## AWS Services Used

# | Service | Purpose |
  | VPC | Networking |
  | Public Subnets | ALB deployment |
  | Security Groups | Traffic control |
  | IAM | Secure AWS access |
  | ECR | Container image storage |
  | ECS Fargate | Container orchestration |
  | Application Load Balancer | Traffic distribution |
  | CloudWatch Logs | Monitoring and troubleshooting |
  | Amazon Bedrock | AI inference |

## Technologies Used
- Terraform
- Docker
- Python
- Flask
- Linux
- AWS CLI
- Git
- GitHub

## Business Use Cases

### 1. Internal Cloud Support Assistant
Provides cloud support guidance for employees and junior engineers.

### 2. AWS Training Assistant
Helps learners understand AWS concepts and troubleshooting procedures.

### 3. Operations Knowledge Assistant
Acts as a self-service cloud support portal for common AWS issues.

# Infrastructure Deployment

## Initialize Terraform
bash
terraform init

## Validate Configuration
bash
terraform validate


## Review Changes
bash
terraform plan


## Deploy Infrastructure
bash
terraform apply

## Terraform Deployment Screenshot
<img width="820" height="464" alt="terraform plan" src="https://github.com/user-attachments/assets/7cde8d1d-5efb-4624-ba81-de9b04647744" />

# Container Deployment

## Build Docker Image
bash
docker build -t ai-cloud-support-assistant .

## Tag Image
bash
docker tag ai-cloud-support-assistant:latest <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/ai-cloud-support-assistant:latest

## Push Image
bash
docker push <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/ai-cloud-support-assistant:latest

## Docker Build Screenshot
<img width="820" height="464" alt="docker" src="https://github.com/user-attachments/assets/cc60e9e0-6f97-484f-97a6-24eff5a60e58" />

# ECS Deployment
The application is deployed on Amazon ECS Fargate and exposed through an Application Load Balancer.

### Components
- ECS Cluster
- ECS Service
- ECS Task Definition
- Fargate Tasks
- Application Load Balancer

## ECS Cluster Screenshot
<img width="960" height="504" alt="cluster" src="https://github.com/user-attachments/assets/d259c28b-4482-443b-95c0-1ec81ffce727" />

## ECS Service Screenshot
<img width="820" height="464" alt="ecs service" src="https://github.com/user-attachments/assets/7e971624-1a91-4105-81e1-54354cb0122b" />

## Running Tasks Screenshot
<img width="960" height="504" alt="task definition" src="https://github.com/user-attachments/assets/7dcd7ecb-38fe-46d2-acdd-460de83fa08f" />

# Application Load Balancer 
<img width="960" height="504" alt="load balancer (2)" src="https://github.com/user-attachments/assets/b82ff5f6-3076-4eff-9c4a-9c2b02529801" />

### IAM Role
<img width="960" height="504" alt="iam role" src="https://github.com/user-attachments/assets/5927cce9-7eb0-4b86-977e-5efdce13d856" />

# Application Demo
<img width="960" height="504" alt="app responding" src="https://github.com/user-attachments/assets/8d550d45-c0da-4c36-8180-1ced35fc416e" />

## CloudWatch Logs Screenshot
<img width="960" height="504" alt="cloudwatch logs" src="https://github.com/user-attachments/assets/3b9b5287-96ae-46de-b1b7-20263f3058c3" />

# Challenges Encountered

## Challenge 1: ECS Service Not Registering With Target Group

### Cause
Incorrect load balancer configuration.

### Resolution
Updated ECS service configuration to use the correct target group and container port.

## Challenge 2: Bedrock Authentication Failure

### Error
NoCredentialsError: Unable to locate credentials

### Cause
Container lacked permissions to access Amazon Bedrock.

### Resolution
Created an ECS Task Role and attached Bedrock permissions.

## Challenge 3: Docker Integration With WSL

### Cause
Docker was not available inside Ubuntu WSL.

### Resolution
Enabled Docker Desktop WSL integration.

# Lessons Learned
- Infrastructure as Code improves repeatability and consistency.
- ECS Task Roles provide secure authentication to AWS services.
- CloudWatch Logs simplify troubleshooting.
- Amazon Bedrock can be integrated into real-world cloud applications.
- ECS Fargate enables serverless container deployments without managing EC2 instances.

# Future Improvements
- Modern responsive UI
- Authentication and user management
- Chat history persistence
- RAG (Retrieval Augmented Generation) integration
- Custom domain and HTTPS
- CloudWatch dashboards and alerts
- Multi-model Bedrock support

# Repository Structure
ai-cloud-support-assistant/
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── screenshots/
│
└── README.md

# Skills Demonstrated

- AWS Infrastructure Design
- Terraform
- Docker
- Amazon ECS Fargate
- Application Load Balancer
- IAM
- Amazon Bedrock
- CloudWatch
- Linux
- Python
- Git & GitHub

# Author
**Mehrwan Hashmi**
AWS Certified Solutions Architect – Associate  
AWS Certified Cloud Practitioner
Cloud Engineering | AWS | Terraform | Docker | ECS | Bedrock | AI Applications
