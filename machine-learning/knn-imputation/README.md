# KNN Imputation

A small machine-learning coursework exercise demonstrating how missing values can be filled with scikit-learn's `KNNImputer` rather than a simple mean or median replacement.

## What It Demonstrates

- Creating a NumPy dataset containing missing values
- Applying `KNNImputer` with two nearest neighbors
- Comparing the original data with the imputed result
- Basic data-preprocessing concepts used before model training

## Requirements

```bash
pip install numpy scikit-learn
```

## Run

```bash
python knn_imputation.py
```

## Workflow

```text
Input Data with Missing Values
            ↓
     KNNImputer (k=2)
            ↓
     Imputed Dataset
            ↓
   Compare Before / After
```

## Related Study Notes

`model-prediction-steps.txt` contains a personal checklist covering data inspection, cleaning, encoding, scaling, dataset splitting, class balancing, feature engineering, dimensionality reduction, augmentation, and model preparation.

## Scope

This is a focused coursework demonstration, not a complete machine-learning model or production data-processing pipeline.
