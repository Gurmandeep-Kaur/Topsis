import sys
import pandas as pd
import numpy as np

def error_exit(msg):
    print(f"Error: {msg}")
    sys.exit(1)

def main():
    #number of parameters
    if len(sys.argv) != 5:
        error_exit("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
    
    input_file = sys.argv[1]
    weights_str = sys.argv[2]
    impacts_str = sys.argv[3]
    output_file = sys.argv[4]

    #handling file not found exception
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        error_exit("Input file not found.")
    except:
        error_exit("Unable to read input file.")

    #input file must contain three or more columns
    if data.shape[1] < 3:
        error_exit("Input file must contain three or more columns.")
    
    decision_matrix = data.iloc[:, 1:].copy()

    #second to last column must contain numeric values only
    for col in decision_matrix.columns:
        if not pd.api.types.is_numeric_dtype(decision_matrix[col]):
            error_exit("From 2nd to last columns must contain numeric values only.")

    impacts = impacts_str.split(',')

    #impacts must be separated by commas
    if any(imp.strip() == "" for imp in impacts):
        error_exit("Impacts must be separated by commas.")

    #impacts must be positive or negative
    for imp in impacts:
        if imp not in ['+', '-']:
            error_exit("Impacts must be either '+' or '-'.")
    
    #weights must be separated by comma
    try:
        weights = list(map(float, weights_str.split(',')))
    except:
        error_exit("Weights must be numeric and separated by commas.")
    
    num_criteria = decision_matrix.shape[1]

    #number of weights, number of impacts, and number of columns must be same
    if len(weights) != num_criteria or len(impacts) != num_criteria:
        error_exit("Number of weights, impacts, and criteria columns must be same.")
    
    #topsis 
    norm_matrix = decision_matrix/np.sqrt((decision_matrix**2).sum())

    weighted_matrix = norm_matrix * weights

    ideal_best = []
    ideal_worst = []

    for j in range(num_criteria):
        if impacts[j] == '+':
            ideal_best.append(weighted_matrix.iloc[:, j].max())
            ideal_worst.append(weighted_matrix.iloc[:, j].min())
        else:
            ideal_best.append(weighted_matrix.iloc[:, j].min())
            ideal_worst.append(weighted_matrix.iloc[:, j].max())
    
    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    topsis_score = dist_worst / (dist_best + dist_worst)

    rank = topsis_score.rank(ascending=False, method='dense').astype(int)

    data['Topsis Score'] = topsis_score
    data['Rank'] = rank

    try:
        data.to_csv(output_file, index=False)
    except:
        error_exit("Unable to write output file.")

    print("TOPSIS analysis completed successfully.")

if __name__ == '__main__':
    main()