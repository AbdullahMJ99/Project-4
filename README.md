# Project-4 - Insights into Housing Prices: Neural Network vs. Random Forest Analysis

Development on this project has stopped.

Refer to `predictive_models_report.md` for insight and analysis.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Gallery](#gallery-of-results)
- [References](#references)
- [Licenses](#licenses)
- [Acknowledgements](#acknowledgements)
- [Authors](#authors)

## Description

This project employs the classic Ames, Iowa housing dataset to predict individual residential property prices using two distinct machine learning models. The experiment involves improving a neural network through feature engineering and hyperparameter tuning, alongside the construction of a random forest model for comparative analysis. The subsequent discussion delves into the strengths and weaknesses of each model, offering insights into their unique attributes and trade-offs.

Refer to `predictive_models_report.md` for insight and analysis.

## Usage

Restart the kernel and run `regression_models.ipynb` to output the results of both a neural network and a random forest model.

---

Details of repo structure:

- `regression_models.ipynb` contains the final models, built after all trials
- `exploratory_data_analysis.ipynb` displays multiple plots guiding feature engineering, data cleaning, and processing
- `House Prices Spreadsheet.xlsx` documents trial models
- `/trial_models/` contains subsequent neural network and random forest models 
- `nn_template.ipynb` demonstrates the keras tuner used for hyperparameter tuning 

## Gallery of Results

Note how closely both model predictions perform.

Sample Neural Network Evaluation Metrics:

![Picture of Sample Neural Network Evaluation Metrics](/images/nn_results.png)

Neural Network Actual vs. Predicted Sale Price:

![Plot of Neural Network Actual vs. Predicted Sale Price](/images/nn_scatter.png)

Neural Network Training and Validation Loss:

![Plot of Neural Network Training and Validation Loss](/images/nn_loss.png)

Neural Network Residuals:

![Plot of Neural Network Residuals](/images/nn_residuals.png)

Sample Random Forest Evaluation Metrics:

![Picture of Sample Random Forest Evaluation Metrics](/images/rf_results.png)

Random Forest Actual vs. Predicted Sale Price:

![Random Forest Actual vs. Predicted Sale Price](/images/rf_scatter.png)

Random Forest Residuals:

![Plot of Random Forest Residuals](/images/rf_residuals.png)

## References

Dataset provided by [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)

## Licenses

This project is licensed under the terms of the [GNU General Public License version 2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).

## Acknowledgements

Thanks to Justin Bisal, James Newman, and Geronimo Perez for feedback and assistance

## Authors

Moussa Diop, Abdullah Jaura, Bryan Johns, Bolima Tafah, November, 2023
