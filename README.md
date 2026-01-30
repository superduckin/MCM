# MCM - 数学建模项目 / Mathematical Modeling Project

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 项目简介 / Project Overview

这是一个数学建模工程项目，提供完整的数据处理、模型训练和结果分析工具链。
This is a mathematical modeling project that provides a complete toolchain for data processing, model training, and result analysis.

### 主要特性 / Key Features

- 📊 **数据处理** / Data Processing: 完整的数据预处理和清洗工具
- 🤖 **模型库** / Model Library: 内置多种常用数学建模算法
- 💾 **数据库支持** / Database Support: 支持 SQLite、MySQL、PostgreSQL
- 📝 **实验管理** / Experiment Management: 完整的实验记录和追踪系统
- 📈 **可视化** / Visualization: 丰富的数据可视化功能

## 目录结构 / Project Structure

```
MCM/
├── config/                 # 配置文件 / Configuration files
│   ├── .env.example       # 环境变量模板 / Environment template
│   └── database.py        # 数据库配置 / Database configuration
├── data/                  # 数据目录 / Data directory
│   ├── raw/              # 原始数据 / Raw data
│   ├── processed/        # 处理后的数据 / Processed data
│   └── external/         # 外部数据 / External data
├── database/              # 数据库脚本 / Database scripts
│   └── init_db.py        # 数据库初始化 / Database initialization
├── docs/                  # 文档 / Documentation
│   ├── ENVIRONMENT_SETUP.md  # 环境配置说明 / Environment setup
│   └── DATABASE.md           # 数据库文档 / Database documentation
├── src/                   # 源代码 / Source code
│   ├── data_processing/  # 数据处理模块 / Data processing
│   │   └── preprocess.py
│   ├── models/           # 模型模块 / Models
│   │   └── linear_model.py
│   └── utils/            # 工具函数 / Utilities
│       └── helpers.py
├── .gitignore            # Git 忽略文件 / Git ignore
├── requirements.txt      # Python 依赖 / Python dependencies
├── environment.yml       # Conda 环境 / Conda environment
└── README.md            # 项目说明 / Project documentation
```

## 快速开始 / Quick Start

### 1. 环境配置 / Environment Setup

详细的环境配置说明请参考: [环境配置文档](docs/ENVIRONMENT_SETUP.md)

**使用 pip 安装:**
```bash
# 克隆项目 / Clone repository
git clone https://github.com/superduckin/MCM.git
cd MCM

# 创建虚拟环境 / Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows

# 安装依赖 / Install dependencies
pip install -r requirements.txt
```

**使用 Conda 安装:**
```bash
conda env create -f environment.yml
conda activate mcm
```

### 2. 数据库配置 / Database Configuration

详细的数据库配置说明请参考: [数据库文档](docs/DATABASE.md)

```bash
# 复制环境配置文件 / Copy environment config
cp config/.env.example .env

# 编辑 .env 文件配置数据库连接 / Edit .env for database connection
# 对于本地开发，默认使用 SQLite / For local development, use SQLite by default

# 初始化数据库 / Initialize database
python database/init_db.py
```

### 3. 运行示例 / Run Examples

**运行线性回归示例:**
```bash
python src/models/linear_model.py
```

**启动 Jupyter Notebook:**
```bash
jupyter notebook
```

## 核心模块说明 / Core Modules

### 数据处理 / Data Processing

`src/data_processing/preprocess.py` 提供了常用的数据预处理功能:

```python
from src.data_processing.preprocess import load_data, clean_data, normalize_data

# 加载数据 / Load data
df = load_data('data/raw/sample.csv')

# 清洗数据 / Clean data
df_cleaned = clean_data(df)

# 标准化 / Normalize
normalized = normalize_data(df_cleaned.values)
```

### 模型训练 / Model Training

`src/models/linear_model.py` 提供了示例模型:

```python
from src.models.linear_model import LinearModel

# 创建模型 / Create model
model = LinearModel()

# 训练 / Train
model.train(X_train, y_train)

# 评估 / Evaluate
results = model.evaluate(X_test, y_test)
```

### 数据库操作 / Database Operations

```python
from config.database import get_engine
from database.init_db import ModelData
from sqlalchemy.orm import sessionmaker

# 创建会话 / Create session
engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

# 保存数据 / Save data
data = ModelData(name='test', value='[1,2,3]')
session.add(data)
session.commit()
```

## 开发指南 / Development Guide

### 添加新模型 / Adding New Models

1. 在 `src/models/` 目录下创建新的模型文件
2. 继承基础模型类或实现标准接口
3. 实现 `train()`, `predict()`, `evaluate()` 方法
4. 添加相应的文档和测试

### 数据处理流程 / Data Processing Pipeline

1. 将原始数据放入 `data/raw/` 目录
2. 使用 `src/data_processing/preprocess.py` 处理数据
3. 将处理后的数据保存到 `data/processed/`
4. 在模型中加载处理后的数据进行训练

## 文档 / Documentation

- [环境配置说明](docs/ENVIRONMENT_SETUP.md) - 详细的环境安装和配置指南
- [数据库文档](docs/DATABASE.md) - 数据库设计和使用说明

## 依赖包 / Dependencies

主要依赖包括 / Main dependencies include:

- numpy, pandas, scipy - 数据处理 / Data processing
- scikit-learn - 机器学习 / Machine learning
- matplotlib, seaborn, plotly - 可视化 / Visualization
- sqlalchemy, pymysql - 数据库 / Database
- jupyter, notebook - 交互式开发 / Interactive development

完整依赖列表见 `requirements.txt`

## 常见问题 / FAQ

### Q: 如何切换数据库？/ How to switch database?

A: 修改 `.env` 文件中的 `DB_TYPE` 参数，支持 sqlite、mysql、postgresql

### Q: 数据应该放在哪里？/ Where to put data?

A: 原始数据放在 `data/raw/`，处理后的数据放在 `data/processed/`

### Q: 如何添加自定义模型？/ How to add custom models?

A: 在 `src/models/` 目录下创建新文件，参考 `linear_model.py` 的实现方式

## 贡献指南 / Contributing

欢迎提交 Issue 和 Pull Request！
Issues and Pull Requests are welcome!

## 许可证 / License

MIT License

## 联系方式 / Contact

如有问题或建议，请提交 Issue 或联系项目维护者。
For questions or suggestions, please submit an Issue or contact the maintainer.