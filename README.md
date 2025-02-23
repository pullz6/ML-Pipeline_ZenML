# ML-Pipeline_ZenML

This is starting project to understand how to deploy a simple project with Zenml and MlFlow, locally. 
---

## Table of Contents

1. [Project Overview](https://www.notion.so/readme-md-Template-in-Github-12c81ba51b198002bc79e96f749cafd6?pvs=21)
2. [Installation](https://www.notion.so/readme-md-Template-in-Github-12c81ba51b198002bc79e96f749cafd6?pvs=21)
4. [Examples](https://www.notion.so/readme-md-Template-in-Github-12c81ba51b198002bc79e96f749cafd6?pvs=21)
5. [Project Structure](https://www.notion.so/readme-md-Template-in-Github-12c81ba51b198002bc79e96f749cafd6?pvs=21)
6. [Contributing](https://www.notion.so/readme-md-Template-in-Github-12c81ba51b198002bc79e96f749cafd6?pvs=21)
7. [Acknowledgments](https://www.notion.so/readme-md-Template-in-Github-12c81ba51b198002bc79e96f749cafd6?pvs=21)

---

## Project Overview

### About

Our objectives are the below:

- Deploying a simple model using Zenml and MLFlow. 
- Zenml is a framework that is relatively new and few functional tutorials are available. This repo intends to provide a template to deploy a simple model or a starting point. 
- Zenml, MLFlow, Sklearn and Pandas are mainly used, few other ancillary libraries are used as well. 

### Screenshots or Demos

Below screenshot of the logged model after pre-processing, training and testing steps completed with Zenml while integrating with MLFlow. 

![image](https://github.com/user-attachments/assets/05aaaed9-87ee-478a-8b2c-7dcc941e69ea)

## Installation

### Prerequisites

Below libraries needs to be installed in the virtual environment: 

1. Zenml
2. MLFlow
3. Pandas

### Instructions

While you can clone the repository, it would be helpful to watch this tutorial to better understand the process. 

When going through the tutorial there is an error towards at the model deployment stage. This error is fixed in this repository by removing the autologging and manually logging the model (this is in line 30 in model_train in the steps file), in addition to that few other changes was made to the run_development.py file. 

When running: 

1. pip install "zenml[server]"
2. export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
3. zenml up (if you want to deactivate it you can run zenml down)
4. run run_pipeline.py
5. python run_development.py --config deploy

If you ran into errors when deploying the model,please try the below: 
1. mlflow ui --port 5000 (if you can't see the mlflow dashboard, you can ran this code to see the code without using zenml)
2. model-deployer models delete <model_id> (if you have a duplicate of the model created, you can get the model id from both zenml and mlflow dashboards, replace it with the <model_id> and run to delete the model)  
   
```

---

## Project Structure

```bash
bash
Copy code
project-root/
│
├── src/                 # Source files
├── data/                # Sample datasets
├── notebooks/           # Jupyter notebooks
├── tests/               # Unit and integration tests
├── README.md            # Project documentation
└── requirements.txt     # Project dependencies

```

Provide brief explanations for each major directory/file if the structure is complex.


---

## Acknowledgments

Shout out to resources, libraries, people, or tutorials that helped you build the project.

---

