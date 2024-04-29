# Ecommerce Customer Analysis Web App


This web application analyzes and predicts the yearly amount spent by customers of an e-commerce platform. It includes features for data summary, data visualization, and prediction based on user input.

## Getting Started
To run this project locally, follow these steps:

### Prerequisites
Make sure you have Python 3 installed on your system.


### Installation:

- Clone this repository to your local machine.

- Copy code   ``` git clone https://github.com/Pratham0405/Customer-Spendings-Prediction.git```
- Navigate to the project directory. Copy code ``` cd Customer-Spendings-Prediction```
- Install the required Python packages using pip ```- pip install -r requirements.txt```
- Running the App : Run the Streamlit app using the following command:
  ```streamlit run app.py```
- This will start the app, and you can access it in your web browser at http://localhost:8501.




# Usage
The web application consists of three main sections:

- Data Summary:
 This section provides basic information about the dataset, including the number of rows and columns, column names, data types, the first few rows of data, and summary statistics of numerical columns.

- Data Visualization:
 In this section, users can visualize the distribution of numerical columns in the dataset through histograms and boxplots. Users can select a column from the dropdown menu to visualize.

- Prediction:
 This section allows users to input their data for prediction. Users can input values for average session length, time on app, time on website, and length of membership. Upon clicking the "Predict" button, the app predicts the yearly amount spent by the customer based on the input data.


Model:
 The prediction is made using a pre-trained linear regression model. The model is trained on the provided dataset and saved as a pickle file (pipe4.pkl).


## Authors

-  [Pratham]([https://github.com/yourusername](https://www.linkedin.com/in/pratham-yeshwante-542333259/))

<a href="https://medium.com/@yeshwantepratham/unveiling-customer-spending-habits-a-data-driven-exploration-6d64c268bdff">Visit my Blog on Medium</a>
<br><br>
<a href="https://www.linkedin.com/in/pratham-yeshwante-542333259/">Connect on Linkedin</a> 
  
