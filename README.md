# README.md

# Kaggle Insurance Premium Prediction

This repository contains the code and resources for the Kaggle competition focused on predicting insurance premiums based on various factors. The goal of this project is to develop a model that accurately predicts the premium amounts for a given set of features.

## Project Structure

```
kaggle-insurance-premiums
├── data
│   ├── train.csv          # Training dataset with features and target variable
│   ├── test.csv           # Test dataset for predictions
│   └── sample_submission.csv # Template for submission format
├── notebooks
│   └── exploratory_data_analysis.ipynb # Jupyter notebook for EDA
├── src
│   ├── data_preprocessing.py # Data preprocessing functions and classes
│   ├── model_training.py      # Model training implementation
│   └── model_evaluation.py     # Model evaluation functions
├── submissions
│   └── submission.csv         # Final submission file with predictions
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to ignore in Git
```

## Dataset

- **train.csv**: Contains the training dataset with features and the continuous target variable, Premium Amount.
- **test.csv**: Contains the test dataset for which predictions of the Premium Amount need to be made.
- **sample_submission.csv**: Provides a template for the submission format.

## Notebooks

- **exploratory_data_analysis.ipynb**: This Jupyter notebook is used for exploratory data analysis (EDA) on the datasets. It includes visualizations and insights derived from the training data.

## Source Code

- **data_preprocessing.py**: Functions and classes for preprocessing the data, including handling missing values, encoding categorical variables, and scaling features.
- **model_training.py**: Implementation of the model training process, defining the model architecture, compiling the model, and fitting it to the training data.
- **model_evaluation.py**: Functions for evaluating the model's performance using metrics such as Root Mean Squared Logarithmic Error (RMSLE) and generating predictions on the test set.

## Submission

The final submission file containing the predicted Premium Amounts for the test dataset is located in the `submissions` directory.

## Requirements

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

1. Preprocess the data using `data_preprocessing.py`.
2. Train the model using `model_training.py`.
3. Evaluate the model using `model_evaluation.py`.
4. Generate predictions and format them according to the submission requirements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.