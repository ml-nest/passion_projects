# All the global parameters can be given here
TRAINING_FILE = "../input/mnist_train_folds.csv"
MODEL_OUTPUT = "../models/"

# creating folds - Stratified K folds
TARGET_COL = "label"
INPUT_FILE = "../input/mnist_train.csv"
POSITIVE_BINARY_CLASS = 1
SPLITS = 8
SHUFFLE = 1