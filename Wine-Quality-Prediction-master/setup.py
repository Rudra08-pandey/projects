#%%
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import tree


#%%
## DATASET URL
dataset_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

# READING DATA FROM CSV AND STORING IN VARIABLE 'DATA'
data = pd.read_csv(dataset_url, sep=';')

#%%
# CREATING FEATURE AND LABEL Y AS OUR LABEL AND X AS OUR FEATURE

# EXTRACTING QUALITY COLUMN FROM THE DATA
y = data.quality

# DROPPING QUALITY COLUMN FROM THE DATA
X = data.drop('quality', axis=1)

# SPLITTING DATA IN 8:2 RATIO I.E. 80% FOR TRAINING AND 20% FOR TESTING
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

# PROCESSING THE TRAINED DATA (I.E. CONVERTING DATA IN RANGE OF -1 AND 1 BECAUSE THIS TYPE OF DATA IS EASILY UNDERSTANDABLE BY MACHINE LEARNING ALGORITHMS)
X_train_scaled = preprocessing.scale(X_train)

# USING DECISION TREE CLASSIFIER
classify=tree.DecisionTreeClassifier()

# TRAINING THE DATA USING X_TRAIN AND Y_TRAIN
classify.fit(X_train, y_train)

# CHECKING THE PREDICTION SCORE
prediction_score = classify.score(X_test, y_test)
print("\nThe prediction score:\n")
print(prediction_score)


# PREDICTING THE QUALITY OF X_TEST AND STORING IN THE Y_PRED
y_pred = classify.predict(X_test)

# PRINTING PREDICTED VALUES
x=np.array(y_pred).tolist()
print("\nPredicted Values:\n")
for i in range(0,5):
    print(x[i])
    
# PRINTING EXPECTED VALUES    
print("\nExpected Values:\n")
print (y_test.head())