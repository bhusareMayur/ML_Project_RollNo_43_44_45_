import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

# Load data
df = pd.read_csv('data/student_data.csv').dropna()
X = df[['study_hours', 'attendance', 'previous_score']]
y = df['pass_exam']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model to model/model.pkl
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as model/model.pkl")
