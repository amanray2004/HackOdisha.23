"""
This file contains the main application.
It contains the Machine learning model which will be integr-
ated with the web application.
The proper documentation along with the implementation with flask will be done here.

"""

# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import pickle
import warnings
from flask import Flask, request, render_template
warnings.filterwarnings('ignore')

# Creating the flask app
app = Flask(__name__)

# Loading the model
model = pickle.load(open('model.pkl', 'rb'))

# Creating the home page
@app.route('/')
def home():
    return render_template('ml.tsx')

# Creating the prediction page
@app.route('/predict', methods = ['POST'])
def predict():
    # Getting the values from the form
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    # Returning the result
    return render_template('features.tsx', prediction_text = 'The predicted result is {}'.format(prediction))

# Running the app
if __name__ == '__main__':
    app.run(debug = True)

# End of code
 


