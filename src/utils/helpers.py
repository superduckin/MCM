"""
通用工具函数 / Common Utility Functions
"""
import logging
import os
from datetime import datetime


def setup_logger(name: str, log_file: str = None, level=logging.INFO):
    """
    设置日志记录器 / Setup logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # 控制台处理器 / Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 文件处理器 / File handler
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def ensure_dir(directory: str):
    """
    确保目录存在 / Ensure directory exists
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_timestamp() -> str:
    """
    获取时间戳字符串 / Get timestamp string
    """
    return datetime.now().strftime('%Y%m%d_%H%M%S')


if __name__ == "__main__":
    logger = setup_logger('test_logger')
    logger.info("工具模块加载成功 / Utility module loaded successfully")
