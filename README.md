# Fraud Detection System

An end-to-end machine learning system for detecting fraudulent transactions in digital payment platforms using synthetic transaction data and behavioral pattern analysis.

## 🎯 Project Overview

This project demonstrates a complete fraud detection pipeline that:
- Generates realistic synthetic transaction data with authentic behavioral patterns
- Engineers meaningful features from raw transaction data
- Trains machine learning models (Random Forest and Graph-based approaches)
- Evaluates models on imbalanced datasets using appropriate metrics
- Provides interpretable fraud predictions

**Key Statistics:**
- 15,000 synthetic transactions
- 3% fraud rate (imbalanced dataset)
- 5 distinct fraud patterns incorporated
- Multiple feature engineering techniques applied

## 📊 Dataset & Fraud Patterns

### Synthetic Dataset
The project creates a realistic transaction dataset with:
- **Users/Accounts**: Multiple user profiles with varying transaction behaviors
- **Merchants**: Different merchant categories and transaction preferences
- **Fields**: transaction_id, user_id, merchant_id, amount, payment_method, location, timestamp, device_id, is_fraud
- **Distribution**: Time-ordered, right-skewed transaction amounts, realistic timestamps

### Fraud Patterns Injected
1. **Transaction Velocity**: Multiple transactions in short timeframe (bot attacks)
2. **Amount Spikes**: Sudden unusually high transactions (account takeover)
3. **Location Inconsistency**: Rapid location changes (credential compromise)
4. **Device Abuse**: Same device used by multiple users (fraud rings)
5. **Merchant Abuse**: Repeated transactions with suspicious merchants (fake merchants)

These patterns are behavioral-driven and reflect real-world fraud tactics.

## 🔧 Feature Engineering

Raw transaction fields are enhanced with:
- **User transaction count**: Transaction frequency per user
- **User average amount**: Baseline spending behavior
- **Amount deviation**: Detection of abnormal spending patterns
- **Device user count**: Identification of shared devices
- **Graph metrics**: Device and merchant network degrees
- **Categorical encoding**: One-hot encoding for payment methods and merchants

## 🤖 Models

### Random Forest Classifier
- Non-linear pattern capture
- Robust to noise and outliers
- Built-in feature importance
- Balanced class weights to handle imbalance

### Graph-Based Approach
- **Nodes**: Users, Devices, Merchants
- **Edges**: Transactions linking entities
- Captures coordinated fraud patterns
- Structural anomaly detection

## 📈 Evaluation Metrics

- **Precision**: True positive rate among predicted frauds
- **Recall**: Fraud detection rate
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Model discrimination ability
- **Confusion Matrix**: Detailed classification breakdown

## 📁 Project Structure

```
fraud-detection/
├── main/
│   └── fraud_detection.ipynb          # Main analysis and modeling notebook
├── src/
│   ├── data_generation.py             # Synthetic data generation
│   ├── fraud_patterns.py              # Fraud pattern injection logic
│   ├── feature_engineering.py         # Feature creation and transformation
│   ├── model.py                       # Model training and prediction
│   ├── graph.py                       # Graph-based feature engineering
│   ├── evaluation.py                  # Model evaluation and metrics
│   └── __init__.py
├── data/
│   ├── raw/
│   │   └── transactions_raw.csv       # Generated synthetic transactions
│   └── processed/
│       └── transactions_features.csv  # Feature-engineered dataset
├── results/                            # Model outputs and visualizations
├── requirements.txt                    # Python dependencies
└── README.md                          # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/fraud-detection.git
cd fraud-detection
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Project

1. **Generate synthetic data and train models:**
   - Open `main/fraud_detection.ipynb` in Jupyter Notebook/Lab
   - Run all cells to execute the complete pipeline

2. **Key outputs:**
   - `data/raw/transactions_raw.csv`: Generated synthetic transactions
   - `data/processed/transactions_features.csv`: Feature-engineered data
   - Model performance metrics and visualizations in the notebook

## 📚 Key Components

### `src/data_generation.py`
Generates synthetic transaction data with realistic patterns:
- User and merchant creation
- Transaction amount distribution
- Timestamp generation
- Random fraud assignment

### `src/fraud_patterns.py`
Injects realistic fraud patterns:
- Velocity-based fraud
- Amount spike detection
- Location anomalies
- Device sharing patterns
- Merchant abuse scenarios

### `src/feature_engineering.py`
Creates behavioral features from raw data:
- Aggregation features (counts, averages)
- Statistical features (deviations, z-scores)
- Categorical encoding
- Temporal features

### `src/model.py`
Model training and evaluation:
- Random Forest classifier setup
- Hyperparameter tuning
- Cross-validation
- Prediction generation

### `src/graph.py`
Graph-based feature engineering:
- Network construction
- Graph degree calculation
- Community detection (optional)

### `src/evaluation.py`
Comprehensive model evaluation:
- Classification metrics
- ROC-AUC calculations
- Confusion matrix generation
- Performance visualization

## 📊 Results & Findings

- **Behavioral features** significantly improve fraud detection performance
- **Graph-based features** enhance detection of coordinated fraud patterns
- **Time-aware modeling** prevents data leakage and ensures realistic evaluation
- **Balanced metrics** (F1-score, precision-recall) are crucial for imbalanced datasets

## 🔍 Model Interpretability

The model provides:
- Feature importance scores from Random Forest
- Clear patterns in SHAP values for individual predictions
- Behavioral signatures for different fraud types
- Decision thresholds for fraud classification

## 💡 Future Improvements

- Real-time fraud scoring pipeline
- Deep learning models (Neural Networks, LSTMs)
- Ensemble methods combining multiple models
- Adversarial fraud pattern generation
- Production deployment with API

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Your Name - Your Email/GitHub Profile

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or feedback, please open an issue in the repository.

---

**Note**: This project uses synthetic data for demonstration purposes. In production environments, ensure compliance with data privacy regulations and security best practices.
