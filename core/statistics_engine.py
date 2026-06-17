# Statistics calculator logic
import numpy as np
import pandas as pd

class StatisticsEngine:
    @staticmethod
    def analyze(data_list):
        arr = np.array(data_list, dtype=float)
        return {
            "Count": len(arr),
            "Sum": np.sum(arr),
            "Mean": np.mean(arr),
            "Median": np.median(arr),
            "Mode": pd.Series(arr).mode()[0],
            "Std Dev": np.std(arr),
            "Variance": np.var(arr),
            "Min": np.min(arr),
            "Max": np.max(arr)
        }