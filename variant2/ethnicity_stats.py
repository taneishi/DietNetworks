import numpy as np
import argparse

from common import dataset_utils

def execute(dataset, dataset_path):
    # Load the dataset
    print('Loading data')
    splits = [0.75]  # This will split the data into [60%, 20%, 20%]

    if dataset == '1000_genomes':
        data = dataset_utils.load_1000_genomes(transpose=False, label_splits=splits, path=dataset_path)
    else:
        print('Unknown dataset')
        return

    (x_train, y_train), (x_valid, y_valid), (x_test, y_test), x_nolabel = data

    y_train = y_train.argmax(1)
    y_valid = y_valid.argmax(1)
    y_test = y_test.argmax(1)

    eth_train = np.zeros((26,))
    eth_valid = np.zeros((26,))
    eth_test = np.zeros((26,))
    eth_tot = np.zeros((26,))

    for i in range(26):
        eth_train[i] = (y_train == i).sum()
        eth_valid[i] = (y_valid == i).sum()
        eth_test[i] = (y_test == i).sum()

        eth_tot[i] = eth_train[i] + eth_valid[i] + eth_test[i]

    print(eth_tot)

def main():
    parser = argparse.ArgumentParser(description='Compute ethnicity stats')
    parser.add_argument('--dataset', default='1000_genomes', help='Dataset.')
    parser.add_argument('--dataset_path', default='temp', help='Path to dataset')

    args = parser.parse_args()
    print('Printing args')
    print(vars(args))

    execute(args.dataset, args.dataset_path)

if __name__ == '__main__':
    main()
