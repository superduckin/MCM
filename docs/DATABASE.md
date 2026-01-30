# 数据库设计文档 / Database Design Documentation

## 概述 / Overview

本项目使用关系型数据库存储数学建模相关数据，包括输入数据、模型结果和实验记录。
This project uses a relational database to store mathematical modeling data, including input data, model results, and experiment records.

## 支持的数据库 / Supported Databases

- SQLite (开发环境推荐 / Recommended for development)
- MySQL (生产环境推荐 / Recommended for production)
- PostgreSQL (企业级应用 / Enterprise applications)

## 数据表结构 / Database Schema

### 1. model_data 表 / Model Data Table

存储数学建模的输入数据
Store input data for mathematical modeling

| 字段名 / Field | 类型 / Type | 说明 / Description |
|---------------|-------------|-------------------|
| id | INTEGER | 主键，自增 / Primary key, auto-increment |
| name | VARCHAR(255) | 数据名称 / Data name |
| description | TEXT | 数据描述 / Data description |
| data_type | VARCHAR(50) | 数据类型 / Data type |
| value | TEXT | 数据值 (JSON格式) / Data value (JSON format) |
| created_at | DATETIME | 创建时间 / Created timestamp |
| updated_at | DATETIME | 更新时间 / Updated timestamp |

**示例 / Example:**
```sql
INSERT INTO model_data (name, description, data_type, value) 
VALUES ('temperature', '温度数据', 'numerical', '[23.5, 24.1, 25.3]');
```

### 2. model_results 表 / Model Results Table

存储数学建模的计算结果
Store calculation results from mathematical models

| 字段名 / Field | 类型 / Type | 说明 / Description |
|---------------|-------------|-------------------|
| id | INTEGER | 主键，自增 / Primary key, auto-increment |
| model_name | VARCHAR(255) | 模型名称 / Model name |
| parameters | TEXT | 模型参数 (JSON格式) / Model parameters (JSON format) |
| result | TEXT | 计算结果 (JSON格式) / Calculation result (JSON format) |
| accuracy | FLOAT | 模型精度 / Model accuracy |
| created_at | DATETIME | 创建时间 / Created timestamp |

**示例 / Example:**
```sql
INSERT INTO model_results (model_name, parameters, result, accuracy) 
VALUES ('LinearRegression', '{"alpha": 0.01}', '{"coefficients": [1.5, -2.0]}', 0.95);
```

### 3. experiments 表 / Experiments Table

记录建模实验过程和结果
Record modeling experiment processes and results

| 字段名 / Field | 类型 / Type | 说明 / Description |
|---------------|-------------|-------------------|
| id | INTEGER | 主键，自增 / Primary key, auto-increment |
| experiment_name | VARCHAR(255) | 实验名称 / Experiment name |
| description | TEXT | 实验描述 / Experiment description |
| status | VARCHAR(50) | 实验状态 (running/completed/failed) / Status |
| start_time | DATETIME | 开始时间 / Start timestamp |
| end_time | DATETIME | 结束时间 / End timestamp |
| notes | TEXT | 实验笔记 / Experiment notes |
| created_at | DATETIME | 创建时间 / Created timestamp |

**示例 / Example:**
```sql
INSERT INTO experiments (experiment_name, description, status, start_time) 
VALUES ('Exp-001', '线性回归测试', 'running', NOW());
```

## 数据库关系图 / ER Diagram

```
┌─────────────────┐
│   model_data    │
├─────────────────┤
│ id (PK)         │
│ name            │
│ description     │
│ data_type       │
│ value           │
│ created_at      │
│ updated_at      │
└─────────────────┘

┌─────────────────┐
│ model_results   │
├─────────────────┤
│ id (PK)         │
│ model_name      │
│ parameters      │
│ result          │
│ accuracy        │
│ created_at      │
└─────────────────┘

┌─────────────────┐
│  experiments    │
├─────────────────┤
│ id (PK)         │
│ experiment_name │
│ description     │
│ status          │
│ start_time      │
│ end_time        │
│ notes           │
│ created_at      │
└─────────────────┘
```

## 使用示例 / Usage Examples

### Python 代码示例 / Python Code Example

```python
from sqlalchemy.orm import sessionmaker
from config.database import get_engine
from database.init_db import ModelData, ModelResult, Experiment
from datetime import datetime

# 创建数据库会话 / Create database session
engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

# 插入数据 / Insert data
data = ModelData(
    name='sample_data',
    description='示例数据',
    data_type='numerical',
    value='[1, 2, 3, 4, 5]'
)
session.add(data)
session.commit()

# 查询数据 / Query data
results = session.query(ModelData).filter_by(name='sample_data').all()
for result in results:
    print(f"Data: {result.name} - {result.value}")

# 关闭会话 / Close session
session.close()
```

## 数据库维护 / Database Maintenance

### 备份数据库 / Backup Database

**SQLite:**
```bash
cp database/mcm.db database/mcm_backup_$(date +%Y%m%d).db
```

**MySQL:**
```bash
mysqldump -u username -p mcm_database > backup_$(date +%Y%m%d).sql
```

**PostgreSQL:**
```bash
pg_dump -U username mcm_database > backup_$(date +%Y%m%d).sql
```

### 恢复数据库 / Restore Database

**SQLite:**
```bash
cp database/mcm_backup_20240101.db database/mcm.db
```

**MySQL:**
```bash
mysql -u username -p mcm_database < backup_20240101.sql
```

**PostgreSQL:**
```bash
psql -U username mcm_database < backup_20240101.sql
```

## 安全建议 / Security Recommendations

1. 不要在代码中硬编码数据库凭据 / Never hardcode database credentials
2. 使用 .env 文件存储敏感信息 / Use .env file for sensitive information
3. 定期备份数据库 / Regular database backups
4. 使用强密码 / Use strong passwords
5. 限制数据库访问权限 / Restrict database access permissions

## 性能优化 / Performance Optimization

1. 为常用查询字段添加索引 / Add indexes for frequently queried fields
2. 定期清理历史数据 / Regular cleanup of historical data
3. 使用连接池管理数据库连接 / Use connection pooling
4. 监控数据库性能指标 / Monitor database performance metrics
