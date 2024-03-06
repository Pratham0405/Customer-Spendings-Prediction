import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle5 as pickle
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
@st.cache
def load_data():
    data = pd.read_csv("Ecommerce_Customers.csv")
    return data

data = load_data()

# Sidebar with buttons
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Data Summary", "Data Visualization", "Modeling"])

# Data Summary
if selection == "Data Summary":
    st.title("Data Summary")
    st.write(data.head())

# Data Visualization
# Data Visualization
elif selection == "Data Visualization":
    st.title("Data Visualization")
    # Filter out numerical columns
    numerical_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    selected_column = st.selectbox("Select a column for visualization", numerical_columns)
    
    # If there are numerical columns available
    if numerical_columns:
        # Histogram
        st.subheader("Histogram")
        plt.hist(data[selected_column])
        st.pyplot()

        # Boxplot
        st.subheader("Boxplot")
        sns.boxplot(data[selected_column])
        st.pyplot()
    else:
        st.write("No numerical columns found in the dataset.")


# Modeling
# Modeling
elif selection == "Modeling":
    st.title("Modeling")
    # Example modeling (replace this with your own)
    if 'target' in data.columns:  # Check if the target column exists in the dataset
        X = data.drop(columns=['target'])  # Assuming 'target' is the dependent variable
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        st.write("Model Accuracy:", accuracy)
    else:
        st.write("Error: Target column not found in the dataset.")



