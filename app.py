import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle5 as pickle
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
@st.cache
def load_data():
    data = pd.read_csv("Ecommerce_Customers.csv")
    return data

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Data Summary", "Data Visualization", "Modeling"])

    data = load_data()

    if page == "Data Summary":
        show_data_summary(data)
    elif page == "Data Visualization":
        show_data_visualization(data)
    elif page == "Modeling":
        show_modeling(data)

def show_data_summary(data):
    st.title("Data Summary")
    st.write(data.head())

def show_modeling(data):
    st.title("Modeling")
    # Example modeling (replace this with your own)
    X = data[['feature1', 'feature2']]
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    st.write("Model Accuracy:", accuracy)

def main():
    st.title("Histogram Selector")
    
    data = load_data()
    
    # Create select box for column selection
    selected_column = st.selectbox("Select a column", data.columns)
    
    # Display histogram for selected column
    st.write(f"### Histogram for {selected_column}")
    plt.hist(data[selected_column])
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)



# Run the app
if __name__ == "__main__":
    main()
