def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def handle_missing_values(df):
    # Example: Fill missing values with the median for numerical columns
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].median(), inplace=True)
    
    # Example: Fill missing values for categorical columns with the mode
    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    
    return df

def encode_categorical_variables(df):
    # Example: One-hot encoding for categorical variables
    df = pd.get_dummies(df, drop_first=True)
    return df

def scale_features(df):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df)
    return pd.DataFrame(scaled_features, columns=df.columns)

def preprocess_data(file_path):
    df = load_data(file_path)
    df = handle_missing_values(df)
    df = encode_categorical_variables(df)
    df = scale_features(df)
    return df