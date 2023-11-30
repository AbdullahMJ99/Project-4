

# Project-4 - Predicting Residential Real Estate Prices Using a Neural Network and a Random Forest

Development on this project has stopped.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Gallery](#gallery-of-results)
- [Conclusion](#conclusion)
- [References](#references)
- [Licenses](#licenses)
- [Acknowledgements](#acknowledgements)
- [Authors](#authors)

## Description

This project aimed to predict house sale prices based on features derived from the Ames, Iowa housing data set spanning residential property sales from 2006 to 2010. The project utilized two different machine learning models: a neural network and a random forest.

The primary notebooks and documents included:
- `regression_models.ipynb`: Contains the final models.
- `exploratory_data_analysis.ipynb`: Presents multiple plots displaying the data and the very first neural network.
- `House Prices Spreadsheet.xlsx`: Documentation of trial models and outcomes.
- `nn_template.ipynb`: Illustrates the usage of Keras Tuner for hyperparameter tuning in trial neural network models.
- `./trial_models/`: Contains subsequent neural network models from trial iterations.

### Overview

The project workflow encompassed Exploratory Data Analysis (EDA), the implementation of a Neural Network, and the construction of a Regression Model. It involved data preprocessing, model construction, evaluation, and visualization of model performance.

### EDA

The exploratory data analysis process involved understanding the dataset's structure, distributions, missing values, and relationships between variables.

### Neural Network Implementation

Implemented a Neural Network using TensorFlow and Keras to predict house sale prices. The process included data preprocessing, hyperparameter tuning, model training, evaluation, and comparison with baseline predictions.

### Regression Model Construction

Constructed a regression model using a neural network architecture for house price prediction. This phase involved data retrieval, preprocessing, exploratory data analysis, model training, and evaluation.

### Insights and Challenges

- **Key Insights**: Understanding data relationships, model performance evaluation, and visualization impact were crucial insights.
- **Challenges**: Addressed challenges including hyperparameter tuning and feature engineering to enhance predictive accuracy.

## Usage

Restart the kernel and run `regression_models.ipynb`.

## Gallery of Results

### Neural Network

Sample Neural Network Evaluation Metrics:

![Sample Neural Network Evaluation Metrics](/images/nn_residuals_hist.png)

Neural Network Actual vs. Predicted Sale Price:

![Neural Network Actual vs. Predicted Sale Price](/images/nn_scatter.png)

Neural Network Training and Validation Loss:

![Neural Network Training and Validation Loss](/images/nn_loss.png)

Neural Network Residuals:

![Neural Network Residuals](/images/nn_residuals.png)

### Random Forest

Sample Random Forest Evaluation Metrics:

![Sample Random Forest Evaluation Metrics](/images/rf_residuals_hist.png)

Random Forest Actual vs. Predicted Sale Price:

![Random Forest Actual vs. Predicted Sale Price](/images/rf_scatter.png)

Random Forest Residuals:

![Random Forest Residuals](/images/rf_residuals.png)

## Conclusion

The project provided insights into house price prediction using data-driven approaches. Exploratory analysis, model implementation, and evaluation facilitated a comprehensive understanding of the dataset and model performance. Challenges, including hyperparameter tuning and feature engineering, were addressed to improve predictive accuracy.

## References

Dataset provided by Kaggle. [House Prices Competition - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)

## Licenses

This project is licensed under the terms of the [GNU General Public License version 2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).

## Acknowledgements

Thanks to Justin Bisal, James Newman, and Geronimo Perez for their valuable feedback and assistance.

## Authors

Moussa Diop, Abdullah Jaura, Bryan Johns, Bolima Tafah, November, 2023.

