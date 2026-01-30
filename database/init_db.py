"""
数据库初始化脚本 / Database Initialization Script
创建数据库表结构 / Create database table structure
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import sys
import os

# 添加父目录到路径 / Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.database import get_engine

Base = declarative_base()


class ModelData(Base):
    """
    模型数据表 / Model Data Table
    存储数学建模的输入数据 / Store input data for mathematical modeling
    """
    __tablename__ = 'model_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, comment='数据名称 / Data name')
    description = Column(Text, comment='数据描述 / Data description')
    data_type = Column(String(50), comment='数据类型 / Data type')
    value = Column(Text, comment='数据值 / Data value')
    created_at = Column(DateTime, default=datetime.now, comment='创建时间 / Created time')
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, 
                       comment='更新时间 / Updated time')


class ModelResult(Base):
    """
    模型结果表 / Model Results Table
    存储数学建模的计算结果 / Store calculation results
    """
    __tablename__ = 'model_results'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(255), nullable=False, comment='模型名称 / Model name')
    parameters = Column(Text, comment='模型参数 / Model parameters')
    result = Column(Text, comment='计算结果 / Calculation result')
    accuracy = Column(Float, comment='模型精度 / Model accuracy')
    created_at = Column(DateTime, default=datetime.now, comment='创建时间 / Created time')


class Experiment(Base):
    """
    实验记录表 / Experiment Records Table
    记录建模实验过程 / Record modeling experiment process
    """
    __tablename__ = 'experiments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    experiment_name = Column(String(255), nullable=False, comment='实验名称 / Experiment name')
    description = Column(Text, comment='实验描述 / Experiment description')
    status = Column(String(50), comment='实验状态 / Experiment status')
    start_time = Column(DateTime, comment='开始时间 / Start time')
    end_time = Column(DateTime, comment='结束时间 / End time')
    notes = Column(Text, comment='实验笔记 / Experiment notes')
    created_at = Column(DateTime, default=datetime.now, comment='创建时间 / Created time')


def init_database():
    """
    初始化数据库，创建所有表 / Initialize database and create all tables
    """
    try:
        engine = get_engine()
        Base.metadata.create_all(engine)
        print("数据库初始化成功！/ Database initialized successfully!")
        print(f"已创建表 / Tables created:")
        print(f"  - {ModelData.__tablename__}")
        print(f"  - {ModelResult.__tablename__}")
        print(f"  - {Experiment.__tablename__}")
        return True
    except Exception as e:
        print(f"数据库初始化失败 / Database initialization failed: {e}")
        return False


if __name__ == "__main__":
    init_database()
