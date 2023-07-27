import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def marks_prediction(hours, courses):
    df =pd.read_csv('Student_Marks.csv')
    # print(df.head())
    X=df.drop('Marks',axis='columns')
    Y=df['Marks']
    # print(X)
    # print(Y)
    # plt.scatter(X,Y)
    # plt.xlabel("No of Hours")
    # plt.ylabel("Marks")
    # # plt.show()
    X_train, X_test, Y_train , Y_test=train_test_split(X, Y, random_state=42, test_size=0.2)
    model=LinearRegression()
    model.fit(X_train,Y_train)
    model.score(X_test, Y_test)
    
    return model.predict(np.array([[hours, courses]]))

