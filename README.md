1. OBJECTIVE:
The goal of this project is to create and deploy an end-to-end fraud detection system that replicates actual digital payment behavior using artificially generated transaction data.
This evaluation assesses the capacity to:

- Describe a practical machine learning issue.
- Create accurate synthetic data
- Create significant behavioral characteristics.
- Select and use appropriate machine learning techniques.
- Correctly assess models for data that is unbalanced.
- Clearly and intuitively describe the model's predictions.

2. PROBLEM STATEMENT:
Every day, digital payment platforms handle a huge volume of transactions. Since fraudulent transactions are uncommon but expensive, identifying them is crucial. Real fraud datasets are frequently unavailable due to security and privacy issues. Thus, a realistic fraud detection pipeline is simulated in this project by:

- Creating fake transaction information
- Including realistic fraud patterns
- Identifying fraudulent transactions through machine learning model training and evaluation
- Building a system that can consistently identify suspicious transactions while still being understandable and useful is the aim.

3. CREATION OF SYNTHETIC DATASET
3.1 Overview of the Dataset
To mimic transaction behavior in the real world, a synthetic dataset was created. Among the entities were:

- Users (accounts)
- Transactions with Merchants
- Fields for transactions:
- transaction_id
- user_id
- merchant_id
- amount, payment method, location, timestamp, and device ID
- is_fraud (label)

3.2 Features of the Dataset
15,000 transactions in total
Rate of fraud: == 3% (unbalanced)
Time-ordered: Transactions are produced in the order they occur.
Non-random fraud: Behavioral patterns are followed by fraud labels
In order to replicate a real-time payment system, transaction amounts have a right-skewed distribution and timestamps advance in a realistic manner.


4. FRAUD PATTERN DESIGN:
Fraud was intentionally injected using detectable and realistic behavioral patterns, rather than random labeling.

4.1 Fraud Patterns Introduced
- Transaction velocity = Multiple transactions in short time = Bot attacks 
- Amount spikes = Sudden unusually high transaction = Account takeover
- Location inconsistency = Sudden location changes = Credential compromise
- Shared devices = Same device used by many users = Fraud rings
- Merchant abuse = Repeated transactions with same merchant = Fake  merchants

4.2 Why These Patterns Are Realistic
In real payment systems, fraud is usually behavior-driven and often involves reuse of infrastructure (devices, merchants, accounts). These patterns reflect common tactics used by fraudsters and create meaningful signals for detection.


5. FEATURE ENGINEERING(FE):
Raw transaction fields alone are insufficient for fraud detection. Therefore, multiple behavioral and relational features were engineered.

Features
- User transaction count --> Captures transaction frequency
- User average amount -->	Baseline spending behavior
- Amount deviation	--> Detects abnormal spending
- Device user count	--> Identifies shared devices
- Encoded categorical variables	--> Enables ML compatibility


6. MODEL DEVELOPMENT:
6.1 Baseline Model Selection
Random Forest classifier:
- Strong performance on tabular data
- Ability to capture non-linear patterns
- Robustness to noise and outliers
- Built-in feature importance for explainability
- Class imbalance was handled using balanced class weights.

6.2 Graph-Based 
To capture relationship-driven fraud, a graph-based approach is taken.
Graph Construction

- Nodes: Users, Devices, Merchants
- Edges: Transactions linking these entities

Graph Features Added
- Device graph degree
- Merchant graph degree


7. EVALUATION OF MODEL:
7.1 Metrics Used
- Precision
- Recall
- F1-score
- ROC-curve
- Confusion matrix


8. FINAL RESULTS/ OUTCOMES:

- Behavioral features significantly improve fraud detection
- Graph-based features enhance detection of coordinated fraud
- Time-aware modeling prevents data leakage
- Simple models with strong features outperform complex approaches


9. CONCLUSION:
This project demonstrates a clean, explainable, and realistic fraud detection pipeline, emphasizing strong ML fundamentals. By combining behavioral features with graph-based reasoning, the system effectively identifies both individual and organized fraud patterns while remaining interpretable and practical.