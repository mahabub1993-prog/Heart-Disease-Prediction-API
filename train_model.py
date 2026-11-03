import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    StratifiedKFold
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)


# STEP 1: Load Dataset
print("\n===== STEP 1: LOAD DATASET =====")

df = pd.read_csv("heart.csv")

print("Original Dataset Shape:", df.shape)


# STEP 2: Remove Duplicate Rows
print("\n===== STEP 2: DATA CLEANING =====")

feature_cols = [col for col in df.columns if col != "target"]

conflicts = df.groupby(feature_cols)["target"].nunique()

if (conflicts > 1).sum() > 0:
    raise ValueError("Conflicting target labels found.")

df = df.drop_duplicates().reset_index(drop=True)

print("Clean Dataset Shape:", df.shape)
print(df["target"].value_counts())


# STEP 3: Features and Target
print("\n===== STEP 3: DATA SPLITTING =====")

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))


# STEP 4: Random Forest Model
print("\n===== STEP 4: MODEL TRAINING =====")

pipeline = Pipeline([
    ("classifier", RandomForestClassifier(
        random_state=42,
        class_weight="balanced"
    ))
])

params = {
    "classifier__n_estimators": [100, 200, 300],
    "classifier__max_depth": [None, 5, 10, 15],
    "classifier__min_samples_split": [2, 5],
    "classifier__min_samples_leaf": [1, 2]
}

cv_strategy = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

grid = GridSearchCV(
    pipeline,
    params,
    cv=cv_strategy,
    scoring="accuracy",
    n_jobs=-1,
    verbose=1
)

grid.fit(X_train, y_train)

best_model = grid.best_estimator_

print("Best Parameters:", grid.best_params_)
print("Best CV Accuracy:", round(grid.best_score_ * 100, 2), "%")


# STEP 5: Model Evaluation
print("\n===== STEP 5: MODEL EVALUATION =====")

y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Test Accuracy:", round(accuracy * 100, 2), "%")
print("Precision:", round(precision_score(y_test, y_pred) * 100, 2), "%")
print("Recall:", round(recall_score(y_test, y_pred) * 100, 2), "%")
print("F1 Score:", round(f1_score(y_test, y_pred) * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# STEP 6: Save Model
print("\n===== STEP 6: SAVE MODEL =====")

Path("model").mkdir(exist_ok=True)

model_data = {
    "model": best_model,
    "features": X.columns.tolist(),
    "model_type": "Random Forest",
    "accuracy": accuracy,
    "cv_accuracy": grid.best_score_
}

joblib.dump(model_data, "model/heart_model.joblib")

print("Model Saved Successfully!")
print("Location: model/heart_model.joblib")

print("\n===== TRAINING COMPLETED =====")