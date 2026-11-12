# Predicting Internship Selection Outcomes — NextGenLearners Week 4 Capstone

A beginner-friendly, end-to-end machine learning project that prepares applicant records, trains a Logistic Regression model, and presents honest, non-technical insights on internship selection.

## 1. Objective
To combine data cleaning and preparation from Weeks 1–3 with supervised machine learning (Logistic Regression) to identify which applicant features are associated with internship selection, while honestly evaluating limitations and fairness risks.

## 2. Dataset Description
The baseline dataset (`applicants_cleaned.csv`, 76 applicant records from Week 1) includes `Applicant Name`, `Email`, `Phone`, `Domain Applied`, `University`, `Application Date`, and `Status` (`29 Selected`, `28 Rejected`, `19 Under Review`). It is extended with four simulated behavioral features:
* `num_skills_listed` (integer, 1–8)
* `has_portfolio` (Yes/No)
* `prior_hackathon_participation` (Yes/No)
* `statement_quality_score` (integer, 1–10)

> **Honesty Note:** The four behavioral features above were **simulated** using `np.random.seed(42)` for reproducibility, as real behavioral metrics were not collected in the original Week 1 dataset.

## 3. Method
1. **Cleaning & Filtering:** Removed the 19 `"Under Review"` records without a final decision, leaving 57 confirmed records (`1` = Selected, `0` = Rejected).
2. **Feature Preparation:** Converted `Yes`/`No` columns to `1`/`0`, one-hot encoded `Domain Applied` (`drop_first=True`), and excluded identifiers (`Applicant Name`, `Email`, `Phone`, `Application Date`) as well as `University`.
3. **Train/Test Split & Training:** Split the 57 rows 80/20 (`45` training, `12` testing, `random_state=42`) and trained a `LogisticRegression` model.
4. **Evaluation:** Evaluated unseen test predictions using Accuracy, Precision, Recall, and a Confusion Matrix.

## 4. Key Results
* **Accuracy:** `25.00%` (3 out of 12 test applicants predicted correctly).
* **Precision:** `33.33%` (1 out of 3 predicted Selected applicants was actually Selected).
* **Recall:** `12.50%` (1 out of 8 actually Selected applicants was caught).
* **Top Sample Features:** `Domain Applied_Data Science` (`+0.66`) and `has_portfolio` (`+0.46`) had the highest positive coefficients in this simulated sample.

## 5. How to Run the Notebook
1. Download `Week4_Capstone_Madhumitha.ipynb` and `applicants_cleaned.csv` from the `week4-capstone/` folder.
2. Open the notebook in **Google Colab**.
3. Upload `applicants_cleaned.csv` to the Colab session files panel.
4. Click **Runtime > Run All** to execute every cell top to bottom.

## 6. Recorded Walkthrough
- [Watch the 2–3 Minute Walkthrough Video Here](https://drive.google.com/file/d/1LJnmrF-BKwFiFLPn-fi9qxA__4n7nAnr/view?usp=sharing)
