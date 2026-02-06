
# CSCN8010 Practical Lab 1: Predictive Maintenance with Linear Regression-Based Alerts

**Student:** Lohith Reddy Danda

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run the Notebook](#how-to-run-the-notebook)
- [SQL Database Setup (Neon)](#sql-database-setup-neon)
- [Project Workflow](#project-workflow)
- [Live Alert Monitoring](#live-alert-monitoring)
- [Results](#results)
- [Conclusion](#conclusion)

---

## Project Overview
- Data cleaning and preprocessing  
- Linear regression modeling for each axis  
- Residual analysis  
- Manual thresholding (MinC, MaxC, T)  
- Alert and error detection  
- Streaming simulation (row‑by‑row real‑time processing)  
- Event logging (start time, end time, duration)  
- Visualizations for model performance  
- Cloud database integration using Neon PostgreSQL  

---

## Features
- Complete data cleaning and preprocessing pipeline  
- Linear regression models for all robot axes  
- Residual-based anomaly detection  
- Manual thresholding using MinC, MaxC, and T values  
- Real-time streaming simulation (row-by-row processing)  
- Live alert monitoring with alert/error summaries  
- Event logging with start time, end time, and duration  
- Cloud database integration using Neon PostgreSQL  
- Visualizations for model performance and anomaly patterns  
- Fully reproducible Jupyter notebook workflow  

---

## Project Structure
| Path / File | Description |
|-------------|-------------|
| **data** | Folder containing all datasets |
| alerts_log.csv | Logged alerts from streaming simulation |
| RMBR4-2_export_test.csv | Raw robot test dataset |
| test_data_synthetic.csv | Synthetic test dataset |
| **notebooks** | Jupyter notebooks for analysis |
| analysis.ipynb | Full pipeline: cleaning → regression → alerts → SQL → plots |
| **src** | Source code modules |
| \_\_init\_\_.py | Package initializer |
| alerts.py | Alert & error classification logic |
| plots.py | Visualization functions |
| regression.py | Linear regression + residual calculations |
| streaming_sim.py | Real‑time streaming simulation |
| thresholds.py | MinC, MaxC, T threshold definitions |

---

## Installation

Create and activate a virtual environment:

```
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

Install dependencies:

```
pip install -r requirements.txt
```

Includes:
pandas
numpy 
matplotlib
scikit‑learn
sqlalchemy
psycopg2‑binary
jupyter
python‑dotenv

---

## How to Run the Notebook

Start Jupyter:

```
jupyter notebook
```

Open:

```
notebooks/analysis.ipynb
```

Run all cells to reproduce:

- data cleaning  
- regression modeling  
- thresholding  
- alert/error detection  
- streaming simulation  
- event logging  
- SQL integration  
- visualizations  

---

## SQL Database Setup (Neon)

Create a `.env` file in the project root:

```
DB_USER=neondb_owner
DB_PASS=npg_sKSDrw13nUGf
DB_HOST=ep-patient-dream-ai8yymm5-pooler.c-4.us-east-1.aws.neon.tech
DB_NAME=neondb
```

Ensure `.env` is **not** committed to GitHub.

Load environment variables in the notebook:

```python
from dotenv import load_dotenv
import os

load_dotenv()
```

The notebook will automatically connect to your Neon PostgreSQL database.

---

## Project Workflow
- Load raw robot current data  
- Clean and preprocess  
- Fit linear regression models  
- Compute residuals  
- Apply MinC, MaxC, T thresholds  
- Detect alerts and errors  
- Simulate real‑time streaming  
- Log events (start, end, duration)  
- Store and load data from Neon SQL  
- Generate visualizations  

---

## Live Alert Monitoring

Live alert is a simple monitoring step that checks whether each axis is behaving normally while the data is running. For every sensor reading, the actual value is compared with the model’s predicted value. If the difference is slightly higher than expected, it is marked as an **alert**, and if the difference is much higher, it becomes an **error**. Each axis receives a short summary showing how many alerts and errors occurred, along with the timing of the first and last abnormal events. This provides a quick, readable snapshot of the machine’s behavior without overwhelming output.

---

## Results
- Regression models successfully captured expected current behavior  
- Residuals revealed abnormal patterns  
- Alerts and errors were detected correctly  
- Streaming simulation behaved like a real robot controller  
- Event logging captured accurate start/end times  
- SQL integration worked smoothly  
- Visualizations confirmed the anomaly detection pipeline  

---

## Conclusion
This project demonstrates a complete predictive maintenance pipeline for a multi‑axis robotic system. It includes data cleaning, regression modeling, thresholding, real‑time simulation, event logging, SQL integration, and visualizations. The system is fully reproducible and ready for deployment or further research.




