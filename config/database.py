"""
数据库连接配置 / Database Connection Configuration
"""
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 加载环境变量 / Load environment variables
load_dotenv()


def get_database_url():
    """
    根据环境变量构建数据库连接URL
    Build database connection URL from environment variables
    """
    db_type = os.getenv('DB_TYPE', 'sqlite')
    
    if db_type == 'sqlite':
        db_path = os.getenv('DB_PATH', 'database/mcm.db')
        return f'sqlite:///{db_path}'
    
    elif db_type == 'mysql':
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '3306')
        db_name = os.getenv('DB_NAME')
        return f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    
    elif db_type == 'postgresql':
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '5432')
        db_name = os.getenv('DB_NAME')
        return f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    
    else:
        raise ValueError(f"Unsupported database type: {db_type}")


def get_engine():
    """
    创建数据库引擎
    Create database engine
    """
    database_url = get_database_url()
    return create_engine(database_url, echo=True)


# 示例使用 / Example usage
if __name__ == "__main__":
    engine = get_engine()
    print(f"Database engine created successfully")
    print(f"Database URL: {engine.url}")
