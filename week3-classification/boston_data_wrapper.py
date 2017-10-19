"""Wrapper that returns training data for the Boston house prices dataset"""
from sklearn.datasets import load_boston
from sklearn.decomposition import PCA # to visualize our data
from sklearn.preprocessing import normalize # to standardize our data
from sklearn.model_selection import train_test_split

def get_data():
	data, targets = load_boston(True)
	data = normalize(data)
	targets = targets.reshape((targets.shape[0],1)) # reshape targets to follow our variables
	X_train, X_test, y_train, y_test = train_test_split(data, targets, 
	                                                    test_size = 0.3, random_state = 42)
	return X_train, X_test, y_train, y_test