import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import pickle5 as pickle
import joblib


# Load data
@st.cache
def load_data():
    data = pd.read_csv("Ecommerce_Customers.csv")
    return data

def main():
    st.title("Histogram Selector")
    
    data = load_data()
    
    # Create select box for column selection
    selected_column = st.selectbox("Select a column", data.columns)
    
    # Display histogram for selected column
    st.write(f"### Histogram for {selected_column}")
    sns.histplot(data[selected_column])
    




# Run the app
if __name__ == "__main__":
    main()
