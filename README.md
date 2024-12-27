# README.md

# Kaggle Insurance Premium

## Project Overview
This project analyzes insurance premium data and builds predictive models to estimate insurance costs based on various factors.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Kaggle-Insurance-Premium.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Kaggle-Insurance-Premium
    ```
3. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Prepare the dataset:
    - Ensure you have the dataset in the correct format and place it in the `data` directory.
2. Run the data preprocessing script:
    ```bash
    python preprocess.py
    ```
3. Train the model:
    ```bash
    python train.py
    ```
4. Evaluate the model:
    ```bash
    python evaluate.py
    ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Data Files

The following large CSV files are tracked using Git LFS. You can download them directly using the links below:

- [sample_submission.csv](data/sample_submission.csv)
- [test.csv](data/test.csv)
- [train.csv](data/train.csv)

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