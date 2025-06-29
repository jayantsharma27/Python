#  Import the libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the files
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
sample_submission = pd.read_csv('sample_submission.csv')

# Separate the target variable
y = train['SalePrice']
train.drop('SalePrice', axis=1, inplace=True)

#  Combine train and test data
train['is_train'] = 1
test['is_train'] = 0
data = pd.concat([train, test], axis=0)

#  Drop columns with too many missing values or not useful
data.drop(['Id', 'Alley', 'PoolQC', 'Fence', 'MiscFeature', 'FireplaceQu'], axis=1, inplace=True)

# Fill missing values
# Fill known missing categorical features with 'None'
fill_none = ['BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
             'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'MasVnrType']
for col in fill_none:
    data[col] = data[col].fillna('None')

# Fill numerical features that can be zero
fill_zero = ['MasVnrArea', 'GarageYrBlt', 'GarageArea', 'GarageCars',
             'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF']
for col in fill_zero:
    data[col] = data[col].fillna(0)

# Fill LotFrontage by neighborhood median
data['LotFrontage'] = data.groupby('Neighborhood')['LotFrontage'].transform(lambda x: x.fillna(x.median()))

# Fill everything else with mode or median
for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = data[col].fillna(data[col].mode()[0])
    else:
        data[col] = data[col].fillna(data[col].median())

# Fix data types
data['MSSubClass'] = data['MSSubClass'].astype(str)
data['MoSold'] = data['MoSold'].astype(str)
data['YrSold'] = data['YrSold'].astype(str)

# Map quality features to numbers
quality_map = {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'None': 0}
for col in ['ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'HeatingQC',
            'KitchenQual', 'GarageQual', 'GarageCond']:
    data[col] = data[col].map(quality_map)

# Create new useful features
data['TotalBathrooms'] = data['FullBath'] + 0.5*data['HalfBath'] + data['BsmtFullBath'] + 0.5*data['BsmtHalfBath']
data['TotalPorchSF'] = data['OpenPorchSF'] + data['EnclosedPorch'] + data['3SsnPorch'] + data['ScreenPorch']
data['TotalSF'] = data['TotalBsmtSF'] + data['1stFlrSF'] + data['2ndFlrSF']
data['HouseAge'] = data['YrSold'].astype(int) - data['YearBuilt']
data['RemodAge'] = data['YrSold'].astype(int) - data['YearRemodAdd']
data['IsRemodeled'] = (data['YearBuilt'] != data['YearRemodAdd']).astype(int)
data['HasGarage'] = (data['GarageArea'] > 0).astype(int)
data['HasFireplace'] = (data['Fireplaces'] > 0).astype(int)
data['HasPool'] = (data['PoolArea'] > 0).astype(int)

# Convert categorical columns into numbers (one-hot encoding)
data = pd.get_dummies(data, drop_first=True)

# Split the data back into train and test sets
train_data = data[data['is_train'] == 1].drop('is_train', axis=1)
test_data = data[data['is_train'] == 0].drop('is_train', axis=1)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(train_data)
X_test = scaler.transform(test_data)

# Train a simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y)

# Check how  it does on training data
train_predictions = model.predict(X_train)
rmse = np.sqrt(mean_squared_error(y, train_predictions))
print("Training RMSE:", rmse)

# Make predictions on the test set and save for submission
test_predictions = model.predict(X_test)
sample_submission['SalePrice'] = test_predictions
sample_submission.to_csv('linear_regression_submission.csv', index=False)
print("Submission file saved as 'linear_regression_submission.csv'")
