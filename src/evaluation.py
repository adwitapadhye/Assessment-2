import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    classification_metrics,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)
import os


def evaluate_model(model, X_test, y_test, save_dir="results"):
    os.makedirs(save_dir, exist_ok=True)

    # Prediction
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]


# Classification metrices
    print("\nClassification metrics:\n")
    print(classification_metrics(
        y_test,
        y_pred,
        target_names=["Legitimate", "Fraud"]
    ))

    
 # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",          
        xticklabels=["Legitimate", "Fraud"],
        yticklabels=["Legitimate", "Fraud"]
    )

    plt.title("Confusion Matrix – Fraud Detection")
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")

    plt.tight_layout()
    plt.savefig(f"{save_dir}/confusion_matrix.png", dpi=300)
    plt.show()


# ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_auc = roc_auc_score(y_test, y_prob)

    plt.figure(figsize=(7, 6))
    plt.plot(
        fpr,
        tpr,
        label=f"ROC Curve (AUC = {roc_auc:.3f})",
        linewidth=2
    )
    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        color="gray",
        label="Random Guess"
    )

    plt.title("ROC Curve – Fraud Detection")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(f"{save_dir}/roc_curve.png", dpi=300)
    plt.show()

    print(f"\nROC-AUC Score: {roc_auc:.4f}")
