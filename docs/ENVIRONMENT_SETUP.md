# 环境配置说明 / Environment Configuration Guide

## 目录 / Table of Contents
- [系统要求 / System Requirements](#系统要求--system-requirements)
- [安装步骤 / Installation Steps](#安装步骤--installation-steps)
- [数据库配置 / Database Configuration](#数据库配置--database-configuration)
- [验证安装 / Verify Installation](#验证安装--verify-installation)

## 系统要求 / System Requirements

- Python 3.8 或更高版本 / Python 3.8 or higher
- pip 或 conda 包管理器 / pip or conda package manager
- Git
- 至少 4GB RAM / At least 4GB RAM
- 推荐使用 Linux/macOS/Windows 10+ / Recommended: Linux/macOS/Windows 10+

## 安装步骤 / Installation Steps

### 方法 1: 使用 pip (推荐) / Method 1: Using pip (Recommended)

1. **克隆仓库 / Clone repository**
   ```bash
   git clone https://github.com/superduckin/MCM.git
   cd MCM
   ```

2. **创建虚拟环境 / Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **安装依赖 / Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### 方法 2: 使用 Conda / Method 2: Using Conda

1. **克隆仓库 / Clone repository**
   ```bash
   git clone https://github.com/superduckin/MCM.git
   cd MCM
   ```

2. **创建 Conda 环境 / Create Conda environment**
   ```bash
   conda env create -f environment.yml
   conda activate mcm
   ```

## 数据库配置 / Database Configuration

### SQLite (本地开发推荐) / SQLite (Recommended for Local Development)

1. **复制配置文件 / Copy configuration file**
   ```bash
   cp config/.env.example .env
   ```

2. **编辑 .env 文件，设置 SQLite / Edit .env file for SQLite**
   ```
   DB_TYPE=sqlite
   DB_PATH=database/mcm.db
   ```

3. **初始化数据库 / Initialize database**
   ```bash
   python database/init_db.py
   ```

### MySQL (生产环境) / MySQL (Production)

1. **安装 MySQL / Install MySQL**
   - 下载并安装 MySQL Server
   - 创建数据库: `CREATE DATABASE mcm_database;`

2. **配置环境变量 / Configure environment variables**
   ```
   DB_TYPE=mysql
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=mcm_database
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```

3. **初始化数据库 / Initialize database**
   ```bash
   python database/init_db.py
   ```

### PostgreSQL (可选) / PostgreSQL (Optional)

1. **安装 PostgreSQL / Install PostgreSQL**
   - 下载并安装 PostgreSQL
   - 创建数据库: `CREATE DATABASE mcm_database;`

2. **配置环境变量 / Configure environment variables**
   ```
   DB_TYPE=postgresql
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=mcm_database
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```

3. **初始化数据库 / Initialize database**
   ```bash
   python database/init_db.py
   ```

## 验证安装 / Verify Installation

### 1. 测试 Python 环境 / Test Python Environment
```bash
python --version
pip list
```

### 2. 测试数据库连接 / Test Database Connection
```bash
python config/database.py
```

### 3. 运行示例模型 / Run Example Model
```bash
python src/models/linear_model.py
```

### 4. 启动 Jupyter Notebook (可选) / Start Jupyter Notebook (Optional)
```bash
jupyter notebook
```

## 常见问题 / Troubleshooting

### 问题 1: 包安装失败 / Issue 1: Package Installation Failed
- 确保 pip 是最新版本: `pip install --upgrade pip`
- 使用清华镜像源: `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

### 问题 2: 数据库连接失败 / Issue 2: Database Connection Failed
- 检查数据库服务是否运行
- 验证 .env 配置文件中的连接信息
- 确保数据库用户有正确的权限

### 问题 3: 模块导入错误 / Issue 3: Module Import Error
- 确保虚拟环境已激活
- 检查 PYTHONPATH 设置
- 重新安装依赖包

## 获取帮助 / Getting Help

如有问题，请提交 Issue 或联系项目维护者。
If you have any questions, please submit an Issue or contact the project maintainer.
