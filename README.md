# Internship_Tasks
## Requirements:
Each task requires:
- Python
- Pandas
- Numpy
- Skicit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
# Task_1 Exploring and Visualizing Simple Dataset:
## Objective:
- The objective is to understand the dataset and perform exploratory Data Analysis.
- To perform basic visualizations to understand the relationship between different features.
## Approach:
- Used seaborn and matplotlib to visualize the features.
- Box plot, Scatter Plot and Hist Plot from seaborn library are used for visualizations to examine distributions and outliers, to study correlation and to analyze distribution respectively.
- Colors and labels have been added to make plots more interactive and visible.
## Results and Insights:
- Flowers whose petals are large are likely to have species as Iris-virginica and which have short length are iris-setosa.
- Iris-Virginica has a higher petal and sepal length than Iris-versicolor and Iris-setosa.
---
# Task_2 Credit Risk Prediction:
## Objective:
Predict whether a loan applicant is likely to default on a loan.
## Approach:
- Handle missing values in dataset.
- Train Logistic Regression Model for predicting the target feature Loan_Status.
- Evaluate model performance using accuracy, confusion matrix and classification report.
## Results and Insights:
- Model used is **Logistic Regressio**.
- Its accuracy is **0.788617**(78%).
- Some of the features have no importance in accordance to the target variable so they are removed from the model.
 ---
# Task_3 Customer Churn Prediction (Bank Customer):
## Objective:
Identify customers who are likely to leave the bank.
## Approach:
- Cleaned the dataset and drop un-necessary columns.
- Encoded categorical features using label encoder.
- Scaled the features using Standard Scaler.
- Train **Decision Tree Classifier** model as the target column (Exited) is discrete.
- Evaluated performance of the model.
- Analyze Feature Importance.
## Results and Insights:
- Some of the features like CustomerId, Surname, RowNumber are not influencing the target variable so they are dropped from the model.
- Model's Accuracy to predict target variable is **0.854**(85%).
---
# Task_4 Predicting Insurance Claim Amounts:
## Objective:
Estimate the medical insurance claim amount based on personal data.
## Approach:
- Identified missing values (no missing values).
- Exploratory Data Analysis.
- Train **Linear Regression** model to predict the target feature (continuous).
- Evaluate the model's performance using **Mean Absolute Error** and **Root Mean Squared Error**.
## Results and Insights:
-- The model's performance is evaluated using the Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) metrics.
- Mean Absolute Error is 4181.19 and Root Mean Squared Error is 5796.28. As these values are large so log transformation can be applied to the data to reduce the effect of outliers and improve the model's performance.
---
# Task_5 Personal Loan Acceptance Prediction:
## Objective:
Predict which customers are likely to accept a personal loan offer.
## Approach:
- First split the dataset named bank-full by ';' and replace with ',' and made a new file named bank_clean.
- Identified missing values.
- Exploratory Data Analysis.
- Made Visuals to analyze the feature distribution.
- Train **Logistic Regression** model to predict the target feature.
- Evaluate model's performance using Confusion Matrix, Accuracy and Classification Report.
## Results and Insights:
- It can be concluded that the customers having longer call duration with the bank are more likely to accept the offer to deposit money.
- The customer's job and income level also play a significant role in determining their likelihood of accepting the offer.
- The calls done during specific months like may results in higher probability to accept the offer.
- Model's accuracy is **0.894061**(89%)
---
