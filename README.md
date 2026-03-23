# ✈ AeroInsight — UAE Aerospace Predictive Maintenance Analytics

> **Data-Driven Decision Making Dashboard** | Built for the UAE & GCC Aerospace MRO Sector

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

---

## Overview

AeroInsight is an end-to-end analytics dashboard that analyses survey responses from 2,000 aerospace professionals across the UAE & GCC, applying four machine learning techniques to drive data-driven decisions for a predictive maintenance IoT platform.

---

## Algorithms Implemented

| Tab | Algorithm | Goal |
|-----|-----------|------|
| 🤖 Classification | Random Forest, Gradient Boosting, Logistic Regression | Predict whether a customer is a Hot / Warm / Exploring / Not Interested lead |
| 🔵 Clustering | K-Means + PCA | Segment customers into actionable personas for discount & bundle targeting |
| 🔗 Association Rules | Apriori (mlxtend) | Discover product bundle associations, feature co-selections, cross-sell signals |
| 📈 Regression | Gradient Boosting, Ridge, Lasso, Linear | Predict annual spend and budget per aircraft for pricing strategy |

---

## Classification Metrics
- Accuracy, Precision, Recall, F1-Score (weighted)
- ROC Curve with AUC (One-vs-Rest per class)
- Confusion Matrix
- Feature Importance / Coefficients

## Association Rule Metrics
- Support, Confidence, Lift
- Lift Heatmap, Support vs Confidence scatter
- Top rules by Lift and Confidence

---

## Project Structure

```
├── app.py                                  # Main Streamlit application
├── uae_aerospace_survey_2000_respondents.csv  # Synthetic dataset (2000 rows, 89 cols)
├── requirements.txt                        # Python dependencies
└── README.md                               # This file
```

---

## Local Setup

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/aeroinsight.git
cd aeroinsight

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## Deploy on Streamlit Cloud

1. Push all files to a **public GitHub repository** (no sub-folders — all files in root)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app**
4. Select your repo, branch (`main`), and set **Main file path** to `app.py`
5. Click **Deploy** — done!

---

## Dataset

The dataset is a **synthetic survey** of 2,000 UAE aerospace professionals generated with persona-stratified sampling across 5 customer archetypes:

- Tech-Forward Carrier (22%)
- Budget Regional Operator (28%)
- Enterprise Full-Service (18%)
- Risk-Averse Traditional (20%)
- Defence / Government (12%)

Realistic noise (~8% answer flips, 5% straight-liners) and outliers (~3% budget outliers, ~2% contradictory respondents) have been injected to mimic real-world survey data.

---

## Built By
**Aakash** — AeroInsight Predictive Maintenance Platform · UAE Aerospace Sector
