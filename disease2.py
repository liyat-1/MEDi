import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# Load the training dataset
train_data = pd.read_csv('Training.csv')

# Load the test dataset
test_data = pd.read_csv('Testing.csv')

# Get column names of the training dataset
train_columns = train_data.columns

# Get column names of the test dataset
test_columns = test_data.columns

# Split the training data into features (X_train) and target variable (y_train)
X_train = train_data[train_columns[:-1]]  # Exclude the last column (assumed to be the target variable)
y_train = train_data[train_columns[-1]]    # Use the last column as the target variable

# Split the test data into features (X_test) and target variable (y_test)
X_test = test_data[test_columns[:-1]]  # Exclude the last column (assumed to be the target variable)
y_test = test_data[test_columns[-1]]    # Use the last column as the target variable

# Initialize the random forest classifier
model = RandomForestClassifier(random_state=42)

# Define the parameter grid for grid search
param_grid = {
    'n_estimators': [100, 200, 300],  # Number of trees in the forest
    'max_depth': [10, 15, 20],  # Maximum depth of the trees
    'min_samples_split': [10, 20, 30],  # Minimum number of samples required to split an internal node
    'min_samples_leaf': [5, 10, 15]  # Minimum number of samples required to form a leaf node
}

# Perform grid search to find the best hyperparameters
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best model from the grid search
best_model = grid_search.best_estimator_

# Make predictions on the test data
y_pred = best_model.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained model to a .joblib file
joblib.dump(best_model, 'traineed_model')