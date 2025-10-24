import numpy as np

def calculate(liste):
    if(len(liste) < 9): 
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(liste).reshape(3,3)
    
    mean_line = np.mean(matrix, axis=0)
    mean_column = np.mean(matrix, axis=1)
    mean_matrix = np.mean(matrix)
    
    
    variance_line = np.var(matrix, axis=0)
    variance_column = np.var(matrix, axis=1)
    variance_matrix = np.var(matrix)
    
    
    SD_line = np.std(matrix, axis=0)
    SD_column = np.std(matrix, axis=1)
    SD_matrix = np.std(matrix)
    
    
    max_line = np.max(matrix, axis=0)
    max_column = np.max(matrix, axis=1)
    max_matrix = np.max(matrix)
    
    
    min_line = np.min(matrix, axis=0)
    min_column = np.min(matrix, axis=1)
    min_matrix = np.min(matrix)
    
    
    sum_line = np.sum(matrix, axis=0)
    sum_column = np.sum(matrix, axis=1)
    sum_matrix = np.sum(matrix)
    
    
    calculations = {
        "mean": [mean_line.tolist(), mean_column.tolist(), mean_matrix.tolist()],
        "variance": [variance_line.tolist(), variance_column.tolist(), variance_matrix.tolist()],
        "standard deviation": [SD_line.tolist(), SD_column.tolist(), SD_matrix.tolist()],
        "max": [max_line.tolist(), max_column.tolist(), max_matrix.tolist()],
        "min": [min_line.tolist(), min_column.tolist(), min_matrix.tolist()],
        "sum": [sum_line.tolist(), sum_column.tolist(), sum_matrix.tolist()]
    }

    return calculations