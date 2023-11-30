# Insights into Housing Prices: Neural Network vs. Random Forest Analysis

## Abstract

This project employs the classic Ames, Iowa housing dataset to predict individual residential property prices using two distinct machine learning models. Experimentation involves enhancing a neural network through feature engineering and hyperparameter tuning, alongside the construction of a random forest model for comparative analysis. The subsequent discussion delves into the strengths and weaknesses of each model, offering insights into their unique attributes and trade-offs.

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

The Ames housing dataset, a comprehensive collection of local government data on housing prices spanning 2006-2010, offers a rich landscape of opportunities for predicting individual residential property prices leveraging machine learning. Curated by Dean De Cock and sourced from the Ames City Assessor's Office in 2011, the dataset comprises 80 variables capturing diverse attributes like size, room count, location, and age (see `/resources/data_description.txt`). 

The primary objective was to come up with a linear regression machine learning model capable of predicting the sale price of residential properties. Employing a dataset of 1460 samples provided by [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques), the project delves into the intricacies of neural network complexity and the robustness of a random forest model. This report encapsulates the methodologies employed and valuable insights gained from this comprehensive predictive modeling exercise.

## Exploratory Data Analysis

Commencing our analysis, extensive research and consultations with real estate professionals guided our expectations, leading us to anticipate key features influencing property prices, including property condition, indoor square footage, room count, property age, and the timeless "location, location, location".

The intentionally blurred labels in this initial correlation heatmap underscore the myriad possibilities within this dataset.

![Correlation heatmap](/images/correlation_heatmap_initial.png)

A histogram of the target variable, SalePrice, revealed a fairly normal distribution with a long tail, suggesting potential outliers, later addressed in our data processing.

![Histogram of Sale Price](/images/eda_sale_price_hist.png).

Specific attention was given to indoor living area and indicated promising patterns.

![Scatter plot of Total Indoor Living Area](/images/eda_sale_price_GrLivArea_BsmtFinSF.png)

Challenges emerged when using 'Neighborhood' as a proxy for location. Thirteen of the 28 categories had fewer than 50 values, including categories with 11, 9, and 2 instances.

Investigation into sale conditions revealed 259 values not categorized as 'Normal'. Sale conditions covered a spectrum from trade and foreclosures to short sales, transactions between family members, and houses not completed when last assessed, typically associated with new constructions.

Visualizing both discrete and continuous data through histograms and scatter plots facilitated exploration of potential features influencing sale prices, narrowing our focus to overall quality and condition, aspects related to square footage, room count, and the year built or remodeled.

Nominal and ordinal data were examined using bar plots to guide future feature engineering and potential outlier identification, such as a property lacking sewer and water utilities. Ordinal values related to quality exhibited promise for further analysis.

This meticulous data analysis provided crucial insights into feature selection and potential relationships between variables and sale prices, laying a solid foundation for subsequent modeling.

## Neural Network Creation

Developing a neural network, `nn_template.ipynb` was crafted for developing trial models. 

Leveraging data retrieved from a SQLite database, the template jupyter notebook contains a section dedicated to data processing and feature engineering. It extracts the target feature, SalePrice, and partitions the data into training, testing, and validation sets before normalizing the data.

Implementation of a keras tuner automates exploration of hyperparameter space, facilitating optimization of the configuration of hidden layers, neurons, and activation functions. Keras tuner does not inherently support optimization of R-squared, a metric quantifying variance in predicted values. The notebook utilizes mean absolute error as a surrogate metric, to mitigate the influence of outliers.

Post-tuning, the model is constructed selecting the best hyperparameters, incorporating early stopping to counteract potential overfitting. 

Comprehensive evaluation metrics include R-squared, mean squared error, mean absolute error, and mean percentage error. Visualization of results centers on a scatter plot comparing actual and predicted sales. Key indicators of potential overfitting are presented through the depiction of training and validation loss. A detailed portrayal of model residuals concludes the evaluation.

This structured approach allows for an immense range of data preprocessing and feature engineering, automates hyperparameter optimization, and provides readily interpretable metrics for evaluating model performance before designing subsequent trials.

## Trial Models

Multiple iterations were conducted, documented in `/trial_models/` and detailed in `House Prices Spreadsheet.xlsx`. Anomalies were identified and removed to enhance model robustness, such as the neighborhood Bluestem with only 2 values and properties with more than 4000 square feet of indoor space (see [Exploratory Data Analysis](#exploratory-data-analysis)).

![BlueSte outlier](/images/BlueSte_after_scaling.png)

All non-'Normal' Sale Condition values were excluded from analysis.

 The hyperparameter space for the neural network, including layers, neurons, and activation features, underwent systematic manipulation. Various columns, including promising correlated features such as garage area and the presence of a fireplace, were added and dropped in pursuit of optimal model configuration. Diverse feature engineering attempts were made, generating new values for total living square footage, room count, and even kitchen quality. To evaluate the impact of location, rare neighborhood values were binned.

 The incorporation of these adjustments aimed to fine-tune the models and explore the nuanced relationships between features and sale prices. Each trial contributed to the comprehensive understanding of the predictive capabilities and limitations of the neural network model.

## Random Forest

The incorporation of a random forest model added a comparative dimension to the analysis. Despite the simplicity of the random forest, its ability to handle diverse feature types and potential to capture complex interactions was immediately evident. 

## Results

The predictive models underwent a rigorous evaluation process. The best-performing neural network was crafted through meticulous feature engineering and hyperparameter tuning, showcasing considerable predictive prowess, approaching 88%.

Sample Neural Network Evaluation Metrics:

![Image of Sample Neural Network Evaluation Metrics](/images/nn_results.png)

Neural Network Actual vs. Predicted Sale Price:

![Plot of Neural Network Actual vs. Predicted Sale Price](/images/nn_scatter.png)

Neural Network Training and Validation Loss:

![Plot of Neural Network Training and Validation Loss](/images/nn_loss.png)

Neural Network Residuals:

![Plot of Neural Network Residuals](/images/nn_residuals.png)

The random forest model, while less intricate, presented a robust alternative, showcasing notable performance without any hyperparameter tuning, providing a valuable benchmark for comparison.

![Image of Best Random Forest Evaluation Metrics](/images/rf_results_best.png)

## Discussion

This predictive modeling exercise unveiled insights into the intricate relationship between various residential real estate property features and sale prices. Extensive exploratory data analysis was pivotal in shaping the modeling approach, setting a solid foundation by initially identifying potential features, like overall quality, square footage, room count, and property age.

The neural network, implemented with meticulous adjustments to hyperparameters and feature engineering, demonstrated commendable performance. The evaluation metrics, including R-squared, mean squared error, mean absolute error, and mean percentage error, provided a comprehensive understanding of the model's predictive capabilities. Visualization tools, such as scatter plots for actual versus predicted sale prices, training, and validation loss plots, and residual analyses, enriched the interpretability of the model's behavior.

To complement the neural network trials, a random forest regression model was introduced. The random forest, known for its simplicity and ensemble learning approach, offered a different lens through which to analyze the data. Implemented with the default parameters and a lack of feature engineering, the random forest model's performance highlighted the advantages of simplicity.

The trade-offs between the two models are noteworthy. The neural network, with its capacity for learning intricate patterns, excels in capturing nuanced relationships in the data. However, its susceptibility to overfitting and the need for extensive tuning pose challenges. On the other hand, the random forest, while less prone to overfitting and requiring minimal hyperparameter tuning, may not capture subtle patterns as effectively as the neural network.

Looking ahead, further avenues for exploration include a more in-depth analysis of categorical features, additional feature engineering experiments, and robustness testing against external factors like the 2000s subprime real estate bubble. Utilizing cross-validation could enhance model generalization, and ongoing refinement is warranted for achieving optimal predictive accuracy.

In summary, the neural network and random forest models offer distinct advantages and trade-offs. The neural network excels in capturing intricate relationships but demands meticulous tuning, while the random forest provides robustness with less complexity. The choice between them hinges on the specific goals of the modeling task and the inherent characteristics of the dataset. Further exploration of the random forest, considering its simplicity and robust performance, is recommended to uncover additional insights and potentially enhance predictive capabilities.