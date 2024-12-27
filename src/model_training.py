from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_log_error
import pandas as pd
import numpy as np
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Example preprocessing steps
    df.fillna(df.mean(), inplace=True)  # Handle missing values
    df = pd.get_dummies(df)  # One-hot encoding for categorical variables
    return df

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, filename):
    joblib.dump(model, filename)

def main():
    # Load training data
    train_data = load_data('../data/train.csv')
    
    # Preprocess data
    X = preprocess_data(train_data.drop('Premium Amount', axis=1))
    y = train_data['Premium Amount']
    
    # Split data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Validate model
    y_pred = model.predict(X_val)
    rmsle = np.sqrt(mean_squared_log_error(y_val, y_pred))
    print(f'Validation RMSLE: {rmsle}')
    
    # Save the trained model
    save_model(model, '../submissions/model.pkl')

if __name__ == "__main__":
    main()