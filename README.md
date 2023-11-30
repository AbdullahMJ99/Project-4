# Project-4 - Predicting Residential Real Estate Prices Using a Neural Network and a Random Forest

Development on this project has stopped.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Gallery](#gallery-of-results)
- [References](#references)
- [Licenses](#licenses)
- [Acknowledgements](#acknowledgements)
- [Authors](#authors)

## Description

We predict housing prices based on features derived from the Ames, Iowa housing data set, containing residential property sales from 2006 - 2010. Two different machine learning models are used, a neural network and a random forest.

`regression_models.ipynb` contains the final models.

`exploratory_data_analysis.ipynb` contains multiple plots displaying the data and the very first neural network. 

Documentation of the trial models is contained in `House Prices Spreadsheet.xlsx`. `nn_template.ipynb` shows the keras tuner used to adjust hyperparameters during those trials. Subsequent neural network models are contained in the `./trial_models/` folder.

## Usage

Restart the kernel and run `regression_models.ipynb`

## Gallery of Results

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
