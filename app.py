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



# Run the app
if __name__ == "__main__":
    main()
