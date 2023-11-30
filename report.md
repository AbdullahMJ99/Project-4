# Predicting Residential Real Estate Prices Using a Neural Network and a Random Forest

## Abstract

We predict the price of individual residential property with two different machine learning models using the classic Ames, Iowa housing dataset. Through feature engineering and tweaking hyperparameters, we experimented with improving a neural network. A random forest was also built for comparison. We conclude by discussing the strengths and weaknesses of each.

## Table of Contents

- [Abstract](#abstract)
- [Introduction](#introduction)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Neural Network Creation](#neural-network-creation)
- [Trial Models](#trial-models)
- [Random Forest](#random-forest)
- [Results](#results)
- [Discussion](#discussion)

## Introduction

The Ames housing dataset is a comprehensive collection of local government data related to housing prices, covering the period from 2006-2010. Dean De Cock collected it from the Ames City Assessor's Office in 2011. It contains 80 variables pertaining to the quality and quantity of many attributes potentially related to the sale price of an individual property (see `/resources/data_description.txt`), such as size, room count, location, and age. It offers a rich opportunity to use machine learning to predict home sales price.

Our task was to come up with a linear regression machine learning model that predicted the sales price of a residential property. We used the dataset provided by [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques), so our data contained 1460 samples to train and test with.

## Exploratory Data Analysis

Starting with research, online and consulting with colleagues that work in real estate, we expected the dominant features to be the condition of the property, indoor square footage, number of rooms, the age of the property, and "location, location, location".

As can be seen in this initial correlation heatmap, there were a lot of potential features, but no overwhelming indicators (labels intentionally left blurry to convey the number of possibilities with this dataset).

![Correlation heatmap](/images/correlation_heatmap_initial.png)

After looking at the data, we plotted a histogram of the target variable, SalePrice.

![Histogram of Sale Price](/images/eda_sale_price_hist.png).

The SalePrice appears to have a fairly normal distribution, but with a long tail, potential outliers, that are later removed.

We looked specifically at indoor living area a few different ways, and this looked most promising.

![Scatter plot of Total Indoor Living Area](/images/eda_sale_price_GrLivArea_BsmtFinSF.png)

Neighborhood proved to be a difficult proxy for location, as 13 of the 28 categories had less than 50 values, including ones with 11, 9, and 2.

Finding sale conditions like 'Abnormal' and 'Family' in `/resources/data.description.text` revealed 259 values not categorized as 'Normal'. Sales covered a range between trade, foreclosure, short sales, between family members, and houses not completed when last assessed (usually associated with new houses).

Visualizing all discrete and continuous data with historgrams, and scatter plots enabled easy exploration of potential features related to the sale price. Reviewing the data led us to focus on overall quality and condition, anything to do with square footage, number and type of rooms, and the year built or remodeled.

We visualized nominal and ordinal data with bar plots for future feature engineering and identification of potential outliers, such as the one property with no sewer or water utilities. Ordinal values related to quality showed promise for future analysis.

## Neural Network Creation

Devloping a neural network, `nn_template.ipynb` was crafted for developing trial models. 

Leveraging data retrieved from a SQLite database, the template jupyter notebook contains a section dedicated to data processing and feature engineering. It extracts the target feature, SalePrice, and partitions the data into training, testing, and validation sets before normalizing the data.

Implementaion of a keras tuner automates exploration of hyperparameter space, facilitating optimization of the configuration of hidden layers, neurons, and activation functions. Keras tuner does not inherently support optimization of R-squared, a metric quantifying variance in predicted values. The notebook utilizes mean absolute error as a surrogate metric, to mitigate the influence of outliers.

Post-tuning, the model is constructed selecting the best hyperparameters, incorporating early stopping to counteract potential overfitting. 

Comprehensive evaluation metrics include R-squared, mean squared error, mean absolute error, and mean percentage error. Visualiztion of results centers on a scatter plot comparing actual and predicted sales. Key indicators of potential overfitting are presented through the depiction of training and validation loss. A deailed portrayal of model residuals concludes the evaluation.

This structured approach allows for an immense range of data preprocessing and feature engineering, automates hyperparameter optimization, and provides readily interpretable metrics for evaluating model performance before designing subsequent trials.

## Trial Models

We ran multiple trials. The models can be found in `/trial_models/`. Changes made to each model iteration are contained in `House Prices Spreadsheet.xlsx`.

We found a strange outlier, the neighborhood BlueStem, containing only 2 values, which we dropped, as well as the properties with more than 4000 square feet of indoor space (see [Exploratory Data Analysis](#exploratory-data-analysis)).

![BlueSte outlier](/images/BlueSte_after_scaling.png)

All non-'Normal' Sale Condition values were dropped.

The tuner range of layers, neurons, and activation features were manipulated. Multiple columns were added and dropped, including such promising correlated features as garage area and the presence of a fireplace. Feature engineering was tried in multiple ways, creating new values for total living square footage, number of rooms, and even kitchen quality. Attempts to evaluate the impact of location were addressed by binning rare neighborhood values.

## Random Forest

Plateauing on significant model improvement, we built a simple random forest regression model to compare with the neural network.

## Results

Our best neural network was based on a combination of Overall Quality, Overall Condition, Total Indoor Square Footage, Number of Rooms, Year Built, and Neighborhood.

Sample Neural Network Evaluation Metrics:

![Image of Sample Neural Network Evaluation Metrics](/images/nn_results.png)

Neural Network Actual vs. Predicted Sale Price:

![Plot of Neural Network Actual vs. Predicted Sale Price](/images/nn_scatter.png)

Neural Network Training and Validation Loss:

![Plot of Neural Network Training and Validation Loss](/images/nn_loss.png)

Neural Network Residuals:

![Plot of Neural Network Residuals](/images/nn_residuals.png)

The best model for the random forest was the one that only removed the four properties containing more than 4000 square feet of indoor living space.

![Image of Best Random Forest Evaluation Metrics](/images/rf_results_best.png)

## Discussion

More EDA

Compare / contrast random forest vs neural network

Cast a wider net

Suggestions: Cross Validation, Feature Engineering w categorical values

Feature engineer 'location, location, location' with nearby amenities

Garage area, fireplaces, kitchen