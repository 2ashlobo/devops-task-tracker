# DevOps Task Tracker

A containerized Python Flask web application with a complete DevOps pipeline — built as a portfolio project demonstrating CI/CD, containerization, orchestration, and infrastructure as code.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-D24939)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5)
![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC)

---

## Architecture

```
Developer → Git Push → Jenkins Pipeline
                          ├── Lint (flake8)
                          ├── Test (pytest)
                          ├── Build (Docker)
                          ├── Push (Docker Hub)
                          └── Deploy (Kubernetes)
```

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Flask** | Python web framework |
| **Docker** | Containerization |
| **Jenkins** | CI/CD pipeline |
| **Kubernetes** | Container orchestration |
| **Terraform** | Infrastructure as Code (AWS) |
| **pytest** | Unit testing |
| **flake8** | Code linting |
| **Gunicorn** | Production WSGI server |

## Project Structure

```
├── app/
│   ├── app.py                  # Flask application
│   └── templates/
│       └── index.html          # UI template
├── tests/
│   └── test_app.py             # Unit tests
├── k8s/
│   ├── deployment.yaml         # Kubernetes Deployment
│   └── service.yaml            # Kubernetes Service
├── terraform/
│   └── main.tf                 # AWS EC2 provisioning
├── Jenkinsfile                 # CI/CD pipeline definition
├── Dockerfile                  # Container image build
├── docker-compose.yml          # Local development
├── requirements.txt            # Python dependencies
└── README.md
```

## Quick Start

### Run Locally (Python)

```bash
pip install -r requirements.txt
python app/app.py
# Open http://localhost:5000
```

### Run with Docker

```bash
docker-compose up --build
# Open http://localhost:5000
```

### Run with Docker (manual)

```bash
docker build -t devops-task-tracker .
docker run -p 5000:5000 devops-task-tracker
```

## Testing

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

## Jenkins Pipeline Setup

1. **Install Jenkins** on your server or locally
2. **Install plugins**: Docker Pipeline, Kubernetes CLI
3. **Add credentials**: Go to Jenkins → Manage Credentials → Add `dockerhub-credentials` (Username/Password)
4. **Create pipeline job**: New Item → Pipeline → Point to your Git repo
5. **Build**: Jenkins will automatically run the `Jenkinsfile`

### Pipeline Stages

| Stage | Description |
|-------|-------------|
| Checkout | Pull latest code from Git |
| Lint | Run flake8 code quality checks |
| Test | Run pytest unit tests |
| Build | Build Docker image |
| Push | Push image to Docker Hub |
| Deploy | Apply Kubernetes manifests |

## Kubernetes Deployment

```bash
# Apply manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check status
kubectl get pods
kubectl get services
```

## Terraform (AWS EC2)

```bash
cd terraform

# Initialize
terraform init

# Preview changes
terraform plan -var="key_name=your-key-pair"

# Deploy
terraform apply -var="key_name=your-key-pair"

# Destroy when done
terraform destroy -var="key_name=your-key-pair"
```

## DevOps Skills Demonstrated

- **Containerization**: Multi-stage Docker builds, health checks, `.dockerignore`
- **CI/CD**: Jenkins declarative pipeline with 6 automated stages
- **Orchestration**: Kubernetes Deployments with rolling updates, resource limits, probes
- **IaC**: Terraform provisioning of AWS EC2 with security groups
- **Testing**: Automated unit tests with pytest
- **Code Quality**: Linting with flake8
- **Production**: Gunicorn WSGI server, environment variables

## License

MIT


deployed app on EC2 instance 
<img width="1918" height="1068" alt="image" src="https://github.com/user-attachments/assets/f1116375-3092-472a-ba96-d25fe12e41b0" />

