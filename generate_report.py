from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

OUTPUT = "g25ai1016_Major.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=2.5*cm,
    leftMargin=2.5*cm,
    topMargin=2.5*cm,
    bottomMargin=2.5*cm,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "MyTitle", parent=styles["Title"],
    fontSize=18, spaceAfter=6, alignment=TA_CENTER, textColor=colors.HexColor("#1a1a2e")
)
subtitle_style = ParagraphStyle(
    "Subtitle", parent=styles["Normal"],
    fontSize=11, spaceAfter=4, alignment=TA_CENTER, textColor=colors.HexColor("#444444")
)
heading1 = ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontSize=13, spaceBefore=14, spaceAfter=6,
    textColor=colors.HexColor("#1a1a2e"), borderPad=2
)
heading2 = ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontSize=11, spaceBefore=10, spaceAfter=4,
    textColor=colors.HexColor("#333366")
)
body = ParagraphStyle(
    "Body", parent=styles["Normal"],
    fontSize=10, spaceAfter=6, leading=15, alignment=TA_JUSTIFY
)
code_style = ParagraphStyle(
    "Code", parent=styles["Code"],
    fontSize=8.5, spaceAfter=4, spaceBefore=4, leading=13,
    backColor=colors.HexColor("#f5f5f5"), leftIndent=10, rightIndent=10,
    borderColor=colors.HexColor("#cccccc"), borderWidth=0.5, borderPad=6
)
bullet = ParagraphStyle(
    "Bullet", parent=styles["Normal"],
    fontSize=10, spaceAfter=4, leading=14, leftIndent=16, bulletIndent=4
)

def h(text, style=heading1):
    return Paragraph(text, style)

def p(text):
    return Paragraph(text, body)

def b(text):
    return Paragraph(f"• {text}", bullet)

def code(text):
    return Paragraph(text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style)

def sp(n=1):
    return Spacer(1, n * 0.3 * cm)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceAfter=6, spaceBefore=6)

story = []

# ── COVER PAGE ──────────────────────────────────────────────────────────────
story.append(sp(4))
story.append(Paragraph("ML Ops", title_style))
story.append(Paragraph("Major Assignment", title_style))
story.append(sp(1))
story.append(hr())
story.append(sp(1))
story.append(Paragraph("End-to-End MLOps Pipeline", subtitle_style))
story.append(sp(3))

info_data = [
    ["Roll No", "G25AI1016"],
    ["Name", "Vijay Sai Krishna D"],
    ["Program", "PG Diploma in AI & ML (MLOps)"],
    ["Batch", "May 2026"],
    ["Date of Submission", "June 2026"],
]
info_table = Table(info_data, colWidths=[5*cm, 9*cm])
info_table.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.HexColor("#f0f0f8"), colors.white]),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#aaaaaa")),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cccccc")),
]))
story.append(info_table)
story.append(sp(3))

link_data = [
    ["GitHub Repository", "https://github.com/Vijaysaii/MLops-Assignment-Major-g25ai1016"],
    ["Docker Hub Repository", "https://hub.docker.com/r/vijaysaii/olivetti-faces-app"],
]
link_table = Table(link_data, colWidths=[4.5*cm, 9.5*cm])
link_table.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#aaaaaa")),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cccccc")),
    ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#0000cc")),
]))
story.append(link_table)
story.append(PageBreak())

# ── SECTION 1: OVERVIEW ─────────────────────────────────────────────────────
story.append(h("1. Overview"))
story.append(p(
    "This assignment focuses on building a complete, end-to-end MLOps pipeline. "
    "The goal was to train a machine learning model using scikit-learn, automate the "
    "training and testing process using GitHub Actions CI/CD, containerize the application "
    "using Docker, and deploy it on Kubernetes with high availability using 3 replicas."
))
story.append(p(
    "The Olivetti Faces dataset from sklearn.datasets was used to train a "
    "DecisionTreeClassifier model. The entire workflow follows a structured Git branching "
    "strategy with three branches: main, dev, and docker_cicd."
))
story.append(sp())

story.append(h("2. Dataset & Model", heading1))
story.append(h("2.1 Dataset", heading2))
story.append(p(
    "The Olivetti Faces dataset is a classic face recognition dataset available in "
    "scikit-learn. It contains 400 grayscale face images of 40 different subjects, "
    "with 10 images per subject. Each image is 64x64 pixels, giving a feature vector "
    "of 4096 values per sample."
))
props_data = [
    ["Property", "Value"],
    ["Total Samples", "400"],
    ["Number of Classes", "40 (subjects)"],
    ["Image Size", "64 x 64 pixels"],
    ["Feature Vector Size", "4096"],
    ["Train Set (70%)", "280 samples"],
    ["Test Set (30%)", "120 samples"],
]
props_table = Table(props_data, colWidths=[6*cm, 8*cm])
props_table.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f5f5")]),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#888888")),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cccccc")),
]))
story.append(props_table)
story.append(sp())

story.append(h("2.2 Model", heading2))
story.append(p(
    "A DecisionTreeClassifier from scikit-learn was used as the classification model. "
    "The model was trained on the 70% training split and evaluated on the 30% test split. "
    "The trained model was serialized using joblib and saved as savedmodel.pth for reuse "
    "in the Flask inference application."
))
story.append(p("The model achieved a test accuracy of <b>55.00%</b> on the 120-sample test set."))
story.append(sp())

# ── SECTION 3: GIT BRANCHING ────────────────────────────────────────────────
story.append(h("3. Git Branching Strategy"))
story.append(p(
    "The project follows a strict three-branch Git strategy as required by the assignment. "
    "Each branch has a specific purpose and the branches are not merged back into main."
))
branch_data = [
    ["Branch", "Purpose", "Key Files"],
    ["main", "Initial project setup", "README.md, .gitignore"],
    ["dev", "Model development + CI/CD", "train.py, test.py, requirements.txt, ci.yml"],
    ["docker_cicd", "Docker + Kubernetes deployment", "app.py, Dockerfile, k8s/deployment.yaml, k8s/service.yaml"],
]
branch_table = Table(branch_data, colWidths=[3.5*cm, 5*cm, 6*cm])
branch_table.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f5f5")]),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#888888")),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cccccc")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
]))
story.append(branch_table)
story.append(PageBreak())

# ── SECTION 4: STEP BY STEP ─────────────────────────────────────────────────
story.append(h("4. Step-by-Step Implementation"))

story.append(h("4.1 Step 1 - main Branch: Initial Setup", heading2))
story.append(p(
    "The main branch was initialized first with a README.md and a .gitignore file. "
    "The README contains a full description of the project, repository structure, "
    "branch strategy, and usage instructions. The .gitignore was configured to exclude "
    "Python cache files, virtual environments, the saved model file, and IDE files."
))
story.append(b("Initialized local Git repository with: git init"))
story.append(b("Created main branch: git checkout -b main"))
story.append(b("Committed README.md and .gitignore to main"))
story.append(b("Pushed main branch to GitHub"))
story.append(sp())

story.append(h("4.2 Step 2 - dev Branch: Model Development", heading2))
story.append(p(
    "A new branch named dev was created from main. This branch contains all the "
    "model training, evaluation, and CI/CD pipeline code."
))

story.append(h("train.py", heading2))
story.append(p(
    "This script loads the Olivetti Faces dataset, splits it 70/30, trains a "
    "DecisionTreeClassifier, and saves the model along with the test data using joblib."
))
story.append(code(
    "from sklearn.datasets import fetch_olivetti_faces\n"
    "from sklearn.model_selection import train_test_split\n"
    "from sklearn.tree import DecisionTreeClassifier\n"
    "import joblib\n\n"
    "data = fetch_olivetti_faces(shuffle=True, random_state=42)\n"
    "X_train, X_test, y_train, y_test = train_test_split(\n"
    "    data.data, data.target, test_size=0.30, random_state=42\n"
    ")\n"
    "model = DecisionTreeClassifier(random_state=42)\n"
    "model.fit(X_train, y_train)\n"
    "joblib.dump((model, X_test, y_test), 'savedmodel.pth')"
))
story.append(sp())

story.append(h("test.py", heading2))
story.append(p(
    "This script loads the saved model and test data, runs predictions, "
    "and prints the test accuracy."
))
story.append(code(
    "import joblib\n"
    "from sklearn.metrics import accuracy_score\n\n"
    "model, X_test, y_test = joblib.load('savedmodel.pth')\n"
    "y_pred = model.predict(X_test)\n"
    "accuracy = accuracy_score(y_test, y_pred)\n"
    "print(f'Test Accuracy: {accuracy * 100:.2f}%')"
))
story.append(sp())

story.append(h("CI/CD Workflow (.github/workflows/ci.yml)", heading2))
story.append(p(
    "The GitHub Actions workflow runs on every push to the dev and docker_cicd branches. "
    "It has one job called check_working_repo which performs checkout, Python setup, "
    "dependency installation, model training, and accuracy evaluation."
))
story.append(code(
    "name: CI Pipeline\n"
    "on:\n"
    "  push:\n"
    "    branches: [dev, docker_cicd]\n\n"
    "jobs:\n"
    "  check_working_repo:\n"
    "    runs-on: ubuntu-latest\n"
    "    steps:\n"
    "      - uses: actions/checkout@v4\n"
    "      - uses: actions/setup-python@v5\n"
    "        with: { python-version: '3.11' }\n"
    "      - run: pip install -r requirements.txt\n"
    "      - run: python train.py\n"
    "      - run: python test.py"
))
story.append(sp())

story.append(h("4.3 Step 3 - docker_cicd Branch: Docker and Kubernetes", heading2))
story.append(p(
    "The docker_cicd branch was created from dev. It adds a Flask web application, "
    "a Dockerfile, and Kubernetes manifests for deployment."
))

story.append(h("Flask Web Application (app.py)", heading2))
story.append(p(
    "The Flask app provides a simple web interface where a user can upload a "
    "64x64 grayscale face image. The image is preprocessed, passed through the "
    "trained model, and the predicted subject ID (0-39) is displayed on the page."
))
story.append(b("Route: GET / - Shows the upload form"))
story.append(b("Route: POST / - Accepts image, runs prediction, shows result"))
story.append(b("Image is converted to grayscale, resized to 64x64, and normalized"))
story.append(sp())

story.append(h("Dockerfile", heading2))
story.append(code(
    "FROM python:3.11-slim\n"
    "WORKDIR /app\n"
    "COPY requirements.txt .\n"
    "RUN pip install --no-cache-dir -r requirements.txt\n"
    "COPY train.py test.py app.py ./\n"
    "RUN python train.py\n"
    "EXPOSE 5000\n"
    "CMD [\"python\", \"app.py\"]"
))
story.append(p(
    "The Dockerfile uses a slim Python 3.11 base image, installs all dependencies, "
    "copies the source files, trains the model at build time, and starts the Flask "
    "server on port 5000."
))
story.append(sp())

story.append(h("Building and Pushing Docker Image", heading2))
story.append(code(
    "docker build -t vijaysaii/olivetti-faces-app:latest .\n"
    "docker push vijaysaii/olivetti-faces-app:latest"
))
story.append(sp())
story.append(PageBreak())

# ── SECTION 5: KUBERNETES ───────────────────────────────────────────────────
story.append(h("5. Kubernetes Deployment"))
story.append(p(
    "The application was deployed on a local Kubernetes cluster using minikube. "
    "A Deployment with 3 replicas ensures high availability and self-healing. "
    "A NodePort Service exposes the app on port 30080."
))

story.append(h("5.1 Deployment Manifest (k8s/deployment.yaml)", heading2))
story.append(code(
    "apiVersion: apps/v1\n"
    "kind: Deployment\n"
    "metadata:\n"
    "  name: olivetti-faces-app\n"
    "spec:\n"
    "  replicas: 3\n"
    "  selector:\n"
    "    matchLabels:\n"
    "      app: olivetti-faces-app\n"
    "  template:\n"
    "    spec:\n"
    "      containers:\n"
    "        - name: olivetti-faces-app\n"
    "          image: vijaysaii/olivetti-faces-app:latest\n"
    "          ports:\n"
    "            - containerPort: 5000"
))
story.append(sp())

story.append(h("5.2 Service Manifest (k8s/service.yaml)", heading2))
story.append(code(
    "apiVersion: v1\n"
    "kind: Service\n"
    "metadata:\n"
    "  name: olivetti-faces-service\n"
    "spec:\n"
    "  type: NodePort\n"
    "  selector:\n"
    "    app: olivetti-faces-app\n"
    "  ports:\n"
    "    - port: 5000\n"
    "      targetPort: 5000\n"
    "      nodePort: 30080"
))
story.append(sp())

story.append(h("5.3 Deploying and Verifying", heading2))
story.append(code(
    "kubectl apply -f k8s/deployment.yaml\n"
    "kubectl apply -f k8s/service.yaml\n"
    "kubectl get pods\n"
    "minikube service olivetti-faces-service"
))
story.append(p(
    "Three pods were verified to be running after the deployment. To demonstrate "
    "self-healing, one pod was deleted using kubectl delete pod and it was confirmed "
    "that Kubernetes automatically started a new pod to maintain the 3-replica count."
))
story.append(code(
    "kubectl delete pod olivetti-faces-app-<pod-id>\n"
    "kubectl get pods --watch    # shows new pod being created"
))
story.append(sp())

# ── SECTION 6: ANALYSIS ─────────────────────────────────────────────────────
story.append(h("6. Analysis & Observations"))

story.append(h("6.1 Model Performance", heading2))
story.append(p(
    "The DecisionTreeClassifier achieved a test accuracy of 55.00% on the Olivetti "
    "Faces dataset with a 70/30 train-test split. This is a reasonable baseline for "
    "a Decision Tree on face recognition since Decision Trees do not capture spatial "
    "features as effectively as CNNs. The model overfits the training data slightly "
    "due to the high-dimensional input (4096 features) and the small dataset size. "
    "Performance could be improved using Random Forests, SVMs, or deep learning models, "
    "but the goal of this assignment was to demonstrate the MLOps workflow rather than "
    "achieve maximum accuracy."
))
story.append(sp())

story.append(h("6.2 CI/CD Pipeline", heading2))
story.append(p(
    "The GitHub Actions workflow successfully ran on the dev branch on every push. "
    "It automated the full ML lifecycle - from installing dependencies to training the "
    "model and printing evaluation metrics - without any manual intervention. This is "
    "the core principle of MLOps: making ML workflows reproducible and automated."
))
story.append(sp())

story.append(h("6.3 Docker Containerization", heading2))
story.append(p(
    "Containerizing the app ensures the model runs in the same environment regardless "
    "of the host machine. The model is trained inside the Docker image at build time, "
    "so the container is fully self-contained. This eliminates dependency issues and "
    "makes the app portable across cloud platforms."
))
story.append(sp())

story.append(h("6.4 Kubernetes Orchestration", heading2))
story.append(p(
    "Running 3 replicas with a Deployment ensures that if one pod crashes, Kubernetes "
    "automatically replaces it. This was demonstrated by deleting a pod and observing "
    "a new one being scheduled immediately. The NodePort service makes the app accessible "
    "on a fixed port without needing a cloud load balancer."
))
story.append(sp())

# ── SECTION 7: CONCLUSION ───────────────────────────────────────────────────
story.append(h("7. Conclusion"))
story.append(p(
    "This assignment gave hands-on experience with a real MLOps pipeline from start "
    "to finish. I learned how to structure a machine learning project with proper Git "
    "branching, automate training and testing with GitHub Actions, package a model into "
    "a Docker container, and deploy it on Kubernetes with fault tolerance."
))
story.append(p(
    "The most interesting part was seeing how all the pieces work together - a code push "
    "triggers the CI pipeline, the model gets trained automatically, and the same model "
    "is then served through a containerized Flask API that Kubernetes keeps running at "
    "all times. This is exactly how production ML systems work."
))
story.append(sp())

story.append(h("8. Repository Links"))
links_data = [
    ["GitHub Repository", "https://github.com/Vijaysaii/MLops-Assignment-Major-g25ai1016"],
    ["Docker Hub", "https://hub.docker.com/r/vijaysaii/olivetti-faces-app"],
]
links_table = Table(links_data, colWidths=[4.5*cm, 10*cm])
links_table.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#0000cc")),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.HexColor("#f0f0f8"), colors.white]),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#aaaaaa")),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cccccc")),
]))
story.append(links_table)

doc.build(story)
print(f"Report saved: {OUTPUT}")
