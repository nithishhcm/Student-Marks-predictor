![Python](https://img.shields.io/badge/Python-3.x-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-purple)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
# 🎓 Student Marks Predictor (PostgreSQL + Scikit-Learn)

A clean, end-to-end Machine Learning regression pipeline built in Python that extracts relational data from a **PostgreSQL** database to predict student marks based on course load and study time allocation. 

This project demonstrates database connectivity via `psycopg2`, relational data parsing using `pandas`, and predictive analytics using `scikit-learn`.

---

## 🚀 Key Features

* **Relational Database Integration:** Connects seamlessly to a local or remote PostgreSQL instance using `psycopg2` to execute structured queries and stream records directly into a data science pipeline.
* **Predictive Regression Modeling:** Implements a Scikit-Learn `LinearRegression` model trained on quantitative student behavior vectors.
* **Feature Target Tracking:** Leverages dual input features—the total **number of courses** enrolled and the total **study time** invested—to accurately estimate final grade evaluations.
* **Performance Evaluation:** Utilizes Mean Absolute Error (MAE) metrics to check prediction accuracy against a dedicated testing subset split ($80/20$).

---

## 📊 Feature Matrix

The model evaluates student records using the following structural mapping:

| Input Feature | Data Type | Description |
| :--- | :--- | :--- |
| `number_courses` | Integer / Continuous | Total number of registered courses. |
| `time_study` | Float / Continuous | Total number of hours spent studying. |
| **`Marks` (Target)** | Float / Continuous | The final output grade or performance score to predict. |

---

## 🛠️ Local Installation & Setup

### Prerequisites
* **Python 3.8** or higher.
* **PostgreSQL Server** running locally or remotely.

### Step-by-Step Setup

1. **Clone the Repository:**
```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
   cd YOUR_REPOSITORY
