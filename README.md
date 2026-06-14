# MLOps End-to-End Pipeline

An end-to-end MLOps pipeline using scikit-learn, Docker, GitHub Actions, and Kubernetes.

## Project Overview

This project demonstrates a complete MLOps workflow:
- **Model**: DecisionTreeClassifier trained on the Olivetti Faces dataset
- **CI/CD**: GitHub Actions automates training and testing on every push
- **Containerization**: Docker packages the Flask inference app
- **Orchestration**: Kubernetes runs 3 replicas with a NodePort service

## Repository Structure

```
├── train.py                          # Train and save the model
├── test.py                           # Evaluate saved model accuracy
├── app.py                            # Flask web application (docker_cicd branch)
├── Dockerfile                        # Container build instructions (docker_cicd branch)
├── requirements.txt                  # Python dependencies
├── k8s/
│   ├── deployment.yaml               # Kubernetes Deployment (3 replicas)
│   └── service.yaml                  # Kubernetes NodePort Service
└── .github/workflows/ci.yml          # GitHub Actions CI/CD workflow
```

## Branches

| Branch | Purpose |
|--------|---------|
| `main` | Initial setup — README and .gitignore |
| `dev` | Model development — train.py, test.py, CI workflow |
| `docker_cicd` | Docker + Kubernetes deployment |

## Quick Start

### Train & Test Locally
```bash
pip install -r requirements.txt
python train.py      # Trains model → savedmodel.pth
python test.py       # Prints test accuracy
```

### Docker
```bash
docker build -t olivetti-faces-app .
docker run -p 5000:5000 olivetti-faces-app
# Open http://localhost:5000
```

### Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods        # Verify 3 replicas running
```

## Dataset

The [Olivetti Faces dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html) contains 400 grayscale face images (64×64 pixels) of 40 subjects (10 images each).

## CI/CD Pipeline

On every `push` to the `dev` branch, GitHub Actions:
1. Checks out the repository
2. Sets up Python and installs dependencies
3. Runs `train.py` to generate `savedmodel.pth`
4. Runs `test.py` to display test accuracy
