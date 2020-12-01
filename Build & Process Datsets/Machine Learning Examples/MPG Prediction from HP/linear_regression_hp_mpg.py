import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

# reading in the raw data as a csv, hosted online at below url
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']
raw_dataset = pd.read_csv(url, names=column_names, na_values='?', comment='\t', sep=' ', skipinitialspace=True)
dataset = raw_dataset.copy()

# Cleaning Dataset a little
dataset.isna().sum()
dataset['Origin'] = dataset['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
dataset = pd.get_dummies(dataset, prefix='', prefix_sep='')
dataset = dataset.dropna()
print(dataset.tail())

# Splitting Datasets to train and test data
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('MPG')
test_labels = test_features.pop('MPG')

# Normalization to level the playing field
normalizer = preprocessing.Normalization()
normalizer.adapt(np.array(train_features))

first = np.array(train_features[:1])

horsepower = np.array(train_features['Horsepower'])
horsepower_normalizer = preprocessing.Normalization(input_shape=[1,])
horsepower_normalizer.adapt(horsepower)
horsepower_model = tf.keras.Sequential([horsepower_normalizer,layers.Dense(units=1)])
print(horsepower_model.summary())

#choosing our model of adam
horsepower_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.1), loss='mean_absolute_error')


# Model Parameters to play with
history = horsepower_model.fit(
    train_features['Horsepower'],
    train_labels,
    epochs=100,
    # suppress logging
    verbose=0,
    # Calculate validation results on 20% of the training data
    validation_split = 0.2)

#viewing how well our model did
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print(hist.tail())

test_results = {}
test_results['horsepower_model'] = horsepower_model.evaluate(test_features['Horsepower'], test_labels, verbose=0)

#predicting off the linear regression
x = tf.linspace(0.0, int(󰀂v.3-horsepower󰀂), 251)
y = horsepower_model.predict(x)
print(y[-1])

variables['mpg'] = y[-1][0]
