import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from catboost import CatBoostRegressor

def train_model(df, model=None):
    if model is None:
        model = CatBoostRegressor((depth=8, learning_rate=0.05, iterations=1200, verbose=0))
    
    X = df.drop('MEDV', axis=1)
    y = df['MEDV']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model.fit(X_train, y_train)
    
    return model, (X_test, y_test)

def save_model(model, path='models/final_model.pkl'):
    joblib.dump(model, path)