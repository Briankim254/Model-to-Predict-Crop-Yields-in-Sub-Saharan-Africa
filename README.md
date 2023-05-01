# Machine Learning Model to Predict Crop Yields in Sub-Saharan Africa
Link to the live application - https://yieldpredictor.streamlit.app/

### Devs
1. [Brian Kimutai](https://github.com/Briankim254)
2. [Antoinette Akinyi](https://github.com/kisha-net)
3. [Peterson Kariuki](https://github.com/p_kanyu)
4. [Francis Mayieka](https://github.com/francis-100)
5. [Marcellus Kimutai](https://github.com/marcellus-kimutai)
6. [Ryan Matibo](https://github.com/haxor44)

<details>
<summary><h1> Business Understanding </h1></summary>

<h2> Who is the client? </h2>
- The target user of this machine learning model is a farmer.

<h2> Needs of the client </h2>

1. To be able to make informed decisions regarding crop planting and harvesting.
2. To improve on food security.
3. To reduce on food waste.
4. To increase income for the farmers.
5. To be able to improve on farming techniques.
6. To be able to choose on better irrigation systems.
7. To be able to make informed decisions on the type of plant based on the soil quality.

## Client engagement process
 1. Machine learning team initially meet with the farmers.
 2. Data collection to understand the problem statement and the project scope and objectives.
 3. Analyzing and evaluating farmers information so as to develop a personalized strategy. 
 4. Implementing solutions and monitoring appropriate areas where the maize crop can yield.

## Project Objectives
* To develop a machine learning model that predicts crop yields in Sub-Saharan Africa based on various factors such as:
    - Weather patterns
    - Soil quality
    - Irrigation systems
    - Farming techniques
</details>

<details>
<summary><h1> Data Acquisition </h1></summary>

## Source Systems
 -The data for this project was obtained and analysed in GYGA. The dataset consists of all the 9 Sub-Saharan countries with three sheets; Country, climate zone and station.
 
## Data Acquisition process
- Data collection: This is the first phase of data acquisition process and the file is in an excel format.
- Data Extarction: After uploading the data in our working environment and exported it into dataframes.
- Data cleaning: It involves checking of any missing values, duplicates and inconsistencies in our data.
- Data preparation: Transforming raw data i.e to remove outliers or anomalies to make accurate predictions in our project. 
- Data analysis: To find trends, patterns, and insights we managed to use data analysis. 

</details>

<details>
<summary><h1> Exploratory Data Analysis </h1></summary>

## Exploratory Data Analysis process
 -EDA (Exploratory Data Analysis):  it involves exploring and analyzing data to understand its characteristics and relationships between features. EDA in our project has help in gaining insights about the data, identifying patterns, and detecting anomalies.
 
## Exploratory Data Analysis outcomes
 -In this project we have used Pandas profiling and Sweetviz libraries that are used for exploratory data analysis. Both libraries provide a quick and automated way to generate a comprehensive report of the data, including summary statistics, data quality issues, and visualizations. Pandas profiling library generates a report that contains descriptive statistics of each feature in the dataset while Sweetviz generates a comparison report between two datasets.
</details>

<details>
<summary><h1> Data Cleaning </h1></summary>

## Data cleaning process
 1. Removing duplicate observations
 2. Filtering unwanted outliers
 3. Fixing structural errors
 4. Fixing missing data
 5. Validating data
 
## Data cleaning outcomes
 1. Improved data quality which is consistent
 2. Obtaining distinct data sets
 3. Obtaining relevant data
 
</details>

<details>
<summary><h1> Feature Engineering </h1></summary>

## Feature engineering process
 - Data cleansing.
 - Data transformation.
 - Feature extraction.
 - Feature selection.
 
## Features description
 Independent variables:

  'YW'                                                
  'YP'                                                    
  'WPA'                           
  'YW_CV_TEMPORAL'               
  'YP_CV_TEMPORAL'                
  'YA_CV_TEMPORAL'                
  'CLIMATEZONE'               
  'AREA_IN_CLIMATEZONE_HA'

Target variable is 'YA'
</details>

<details>
<summary><h1> Model Development </h1></summary>

## Model development approach
 The development of the project involves using supervised learning techniques to create a model. In this approach, the machine is given labeled data consisting of input and output pairs. Using this data, the computer learns to construct a model that can map new input data to the corresponding output and as well make predictions.
 
## Model justification
To evaluate the model's overall performance, F1 score takes into account both precision and recall. A high F1 score indicates superior model performance. Additionally, the F1 score can be used to determine if the model is overfitting.
</details>

<details>
<summary><h1> Model Evaluation </h1></summary>

## Metrics used
- To evaluate the overall effectiveness of the model, F1 score, which combines precision and recall into one score, was utilized as the criterion. In order to provide a comprehensive assessment of the model's performance, it considers both precision and recall. The R2 score in a regression model measures the percentage of variance in the dependent variable that is explained by the independent variables.
## Metrics justification
 - A higher F1-score suggests that the model is performing better and it detects overfitting in the model.
 
## Results
 -The model training accuracy was 87%. The F1 score which was 0.98. This means that the model was good.
 
## Conclusions
 F1 score provides a balanced measure of metric. Propotion of correctly classified total number of instance datermines the accuracy.

</details>

<details>
<summary><h1> Model Deployment </h1></summary>

## Deployment model justification
 Streamlit esily deploys machine learning models such as interactive web applications because it simplifies the development and deployment process, provides a Python-based API, and supports deployment to various platforms. It provides a built-in server, making it easy to test the application before deploying it. It also makes it easier for non-technical stakeholders to interact with the model and understand its outputs.
## Deployment process
 1. Preparing the Model: After developing a machine learning model, we prepared it for deployment. This involved saving the model in a file format that could be used by Streamlit.
2. Creating a Streamlit Application: Wrote the application code using Streamlit's Python-based API. The application enables users to interact with the model.
3. Deploy application: Deployed the application to Streamlit community cloud.
4. Testing the Application: Tested the deployed application to ensure that it was working as expected.
</details>

<details>
<summary><h1> Challenges Faced </h1></summary>

1. Data Quality: One of the main challenges faced in creating this machine learning model was ensuring that the data used to train the model is of high quality. This included checking for missing values, outliers, and ensuring that the data was representative of the problem being solved.
2. Data Quantity: Another challenge was getting enough data to train the model effectively. This was especially important for this complex model that required large amounts of data to learn patterns accurately.
3. Model Selection: Choosing the right model for this problem was challenging. There are many types of machine learning models, and selecting the best one required a deep understanding of the problem and the available data.
</details>
































   
