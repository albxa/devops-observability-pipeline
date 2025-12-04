# DevOps Pipeline Project
A complete end-to-end DevOps project demonstrating modern deployment practices using containerized applications, continuous integration, and real-time monitoring. This project aims to simulate a production-like environment by building, deploying, and observing a Python-based web service with industry-standard tools.

## Features
- Containerized Python API: Lightweight FastAPI service packaged using Docker.
- Automated CI/CD Pipeline: GitLab CI/CD pipeline handling testing, building, pushing, and deploying the application.
- Service Monitoring: Integrated Prometheus metrics exporter and Grafana dashboard for real-time observability.
- Local & Remote Deployment: Easily reproducible environment using Docker Compose, deployable to an Ubuntu Linux VM.
- Modular Project Structure: Clearly separated components for API, monitoring, orchestration, and automation.
- Production-like Setup: Includes Linux systemd service management, reverse proxy option, and secure deployment practices.

## Technologies Used
- Backend: Python 3.11, FastAPI, Uvicorn
- Containerization: Docker, Docker Compose
- CI/CD: GitLab CI/CD
- Monitoring Stack: Prometheus, Grafana
- Infrastructure: Ubuntu Server 22.04 (VirtualBox VM)

Optional Tools:
- NGINX reverse proxy
- systemd for long-running services
- SSH for remote deployment automation

## Installation and Setup
### 1. Clone the Repository
git clone https://github.com/username/devops-python-docker-ci-monitoring
cd devops-python-docker-ci-monitoring

### 2. Local Development (Optional for Now)
To run the full stack locally:
docker compose up --build

### 3. VM Setup (In Progress)
A VirtualBox Ubuntu Server VM will be used as the deployment target.
Setup steps include:
- Installing Docker & Docker Compose
- Configuring SSH access
- Pulling images from registry
- Running the application via docker compose

## Project structure
```bash
/app
  main.py              → FastAPI application
  exporter.py          → Prometheus metrics
  Dockerfile           → Application container build
  requirements.txt     → Python dependencies

/prometheus
  prometheus.yml       → Scrape configuration

/grafana
  provisioning/
    dashboards/
      dashboard.json   → Initial Grafana dashboard

docker-compose.yml     → Local + production stack
.gitlab-ci.yml         → GitLab CI/CD pipeline
README.md              → Project documentation
```

## Deployment

### Local Deployment
```bash
docker compose up -d --build
```

Services will be accessible at:
- API: http://localhost:8000
- Metrics: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

### VM Deployment (Upcoming)
1. Push code to GitHub
2. GitHub Actions runs:
- test
- build Docker image
- push to GitHub Container Registry (GHCR)
- deploy to VM via SSH
3. Docker Compose restarts the service on the VM

## Monitoring Overview
- /metrics endpoint exposes custom metrics (request count, latency, uptime)
- Prometheus scrapes metrics at 5s intervals
- Grafana visualizes application health on a dashboard
- Additional panels planned:
  - Container CPU / Memory
  - Request duration
  - Status code distribution

## 📝 To-Do List (Active Development)
### Environment Setup
- [ ] Create GitHub repository
- [ ] Finalize README structure
- [ ] Install and configure Ubuntu VM
- [ ] Install Docker & Docker Compose
### Backend
- [ ] Scaffold FastAPI application
- [ ] Implement Prometheus metrics exporter
- [ ] Write unit tests
### Containerization
- [ ] Build Dockerfile
- [ ] Optimize Docker layers
### Monitoring
- [ ] Create Prometheus configuration
- [ ] Provision Grafana dashboard
### CI/CD
- [ ] Create GitLab CI/CD pipeline
- [ ] Implement test → build → push → deploy stages
### Deployment
- [ ] Set up remote deployment to VM
- [ ] Configure systemd service
- [ ] Add reverse proxy (optional)
