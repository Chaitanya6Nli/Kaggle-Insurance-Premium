def calculate_rmsle(y_true, y_pred):
    import numpy as np
    from sklearn.metrics import mean_squared_log_error

    # Calculate RMSLE
    rmsle = np.sqrt(mean_squared_log_error(y_true, y_pred))
    return rmsle

def evaluate_model(model, X_test, y_test):
    import numpy as np

    # Generate predictions
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    rmsle = calculate_rmsle(y_test, y_pred)
    
    # Print evaluation results
    print(f'Root Mean Squared Logarithmic Error (RMSLE): {rmsle:.4f}')
    
    return y_pred, rmsle

def generate_submission_file(predictions, submission_file_path):
    import pandas as pd

    # Load sample submission file
    sample_submission = pd.read_csv('data/sample_submission.csv')

    # Update the predictions in the sample submission
    sample_submission['Premium Amount'] = predictions

    # Save the submission file
    sample_submission.to_csv(submission_file_path, index=False)
    print(f'Submission file saved to {submission_file_path}')