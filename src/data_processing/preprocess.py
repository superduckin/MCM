"""
数据处理工具类 / Data Processing Utilities
提供常用的数据预处理功能 / Provide common data preprocessing functions
"""
import pandas as pd
import numpy as np
from typing import List, Tuple


def load_data(file_path: str) -> pd.DataFrame:
    """
    加载数据文件 / Load data file
    支持 CSV, Excel 等格式 / Support CSV, Excel formats
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith(('.xlsx', '.xls')):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def clean_data(df: pd.DataFrame, drop_na: bool = True) -> pd.DataFrame:
    """
    清洗数据 / Clean data
    处理缺失值、异常值等 / Handle missing values, outliers, etc.
    """
    df_cleaned = df.copy()
    
    if drop_na:
        df_cleaned = df_cleaned.dropna()
    
    return df_cleaned


def normalize_data(data: np.ndarray) -> np.ndarray:
    """
    数据标准化 / Data normalization
    将数据缩放到 [0, 1] 范围 / Scale data to [0, 1] range
    """
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)


def split_data(X: np.ndarray, y: np.ndarray, test_size: float = 0.2, 
               random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    划分训练集和测试集 / Split train and test sets
    """
    from sklearn.model_selection import train_test_split
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


if __name__ == "__main__":
    # 示例使用 / Example usage
    print("数据处理工具模块加载成功 / Data processing utilities loaded successfully")
