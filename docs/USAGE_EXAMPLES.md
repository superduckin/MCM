# 快速使用指南 / Quick Start Guide

## 1. 基础示例 / Basic Example

### 数据处理示例 / Data Processing Example

```python
import numpy as np
import pandas as pd
from src.data_processing import load_data, clean_data, normalize_data

# 创建示例数据 / Create sample data
data = pd.DataFrame({
    'x1': np.random.randn(100),
    'x2': np.random.randn(100),
    'y': np.random.randn(100)
})

# 保存数据 / Save data
data.to_csv('data/raw/sample_data.csv', index=False)

# 加载数据 / Load data
df = load_data('data/raw/sample_data.csv')

# 清洗数据 / Clean data
df_cleaned = clean_data(df)

# 标准化 / Normalize
X = df_cleaned[['x1', 'x2']].values
X_normalized = normalize_data(X)

print(f"原始数据形状: {df.shape}")
print(f"清洗后数据形状: {df_cleaned.shape}")
print(f"标准化后的数据范围: [{X_normalized.min():.2f}, {X_normalized.max():.2f}]")
```

## 2. 模型训练示例 / Model Training Example

```python
from src.models import LinearModel
from src.data_processing import split_data
import numpy as np

# 准备数据 / Prepare data
X = np.random.rand(200, 3)
y = X @ np.array([1.5, -2.0, 0.5]) + np.random.randn(200) * 0.1

# 划分训练集和测试集 / Split data
X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2)

# 创建并训练模型 / Create and train model
model = LinearModel()
model.train(X_train, y_train)

# 评估模型 / Evaluate model
results = model.evaluate(X_test, y_test)
print(f"模型评估结果: {results}")

# 获取模型参数 / Get model coefficients
coeffs = model.get_coefficients()
print(f"模型系数: {coeffs}")
```

## 3. 数据库操作示例 / Database Operations Example

```python
from config.database import get_engine
from database.init_db import ModelData, ModelResult, Experiment
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

# 创建数据库连接 / Create database connection
engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

# 保存输入数据 / Save input data
input_data = ModelData(
    name='temperature_readings',
    description='温度传感器读数',
    data_type='time_series',
    value=json.dumps([23.5, 24.1, 25.3, 24.8, 23.9])
)
session.add(input_data)

# 保存模型结果 / Save model results
result = ModelResult(
    model_name='LinearRegression',
    parameters=json.dumps({'learning_rate': 0.01, 'iterations': 1000}),
    result=json.dumps({'coefficients': [1.5, -2.0, 0.5], 'intercept': 0.1}),
    accuracy=0.95
)
session.add(result)

# 创建实验记录 / Create experiment record
experiment = Experiment(
    experiment_name='实验-001',
    description='线性回归模型测试',
    status='completed',
    start_time=datetime.now(),
    end_time=datetime.now(),
    notes='模型表现良好，R²=0.95'
)
session.add(experiment)

# 提交更改 / Commit changes
session.commit()

# 查询数据 / Query data
all_results = session.query(ModelResult).all()
for r in all_results:
    print(f"模型: {r.model_name}, 精度: {r.accuracy}")

# 关闭会话 / Close session
session.close()
```

## 4. 完整工作流示例 / Complete Workflow Example

```python
# 完整的数学建模工作流 / Complete mathematical modeling workflow

# Step 1: 导入必要的库 / Import necessary libraries
import numpy as np
import pandas as pd
from src.data_processing import load_data, clean_data, split_data
from src.models import LinearModel
from src.utils import setup_logger, ensure_dir, get_timestamp
from config.database import get_engine
from database.init_db import Experiment
from sqlalchemy.orm import sessionmaker

# Step 2: 设置日志 / Setup logging
logger = setup_logger('workflow', log_file=f'logs/workflow_{get_timestamp()}.log')
logger.info("开始数学建模工作流")

# Step 3: 准备数据 / Prepare data
logger.info("加载和处理数据...")
# 这里使用生成的示例数据，实际使用时应该加载真实数据
# Use generated sample data here, replace with real data in practice
X = np.random.rand(200, 3)
y = X @ np.array([1.5, -2.0, 0.5]) + np.random.randn(200) * 0.1

# Step 4: 划分数据集 / Split dataset
X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2)
logger.info(f"训练集大小: {len(X_train)}, 测试集大小: {len(X_test)}")

# Step 5: 训练模型 / Train model
logger.info("训练模型...")
model = LinearModel()
model.train(X_train, y_train)

# Step 6: 评估模型 / Evaluate model
logger.info("评估模型...")
results = model.evaluate(X_test, y_test)
logger.info(f"评估结果: MSE={results['mse']:.4f}, R²={results['r2']:.4f}")

# Step 7: 保存实验记录到数据库 / Save experiment to database
logger.info("保存实验记录...")
engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

experiment = Experiment(
    experiment_name=f'实验_{get_timestamp()}',
    description='线性回归模型工作流测试',
    status='completed',
    notes=f"MSE={results['mse']:.4f}, R²={results['r2']:.4f}"
)
session.add(experiment)
session.commit()
session.close()

logger.info("工作流完成!")
print("数学建模工作流执行成功！")
```

## 5. 数据可视化示例 / Data Visualization Example

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 设置样式 / Set style
sns.set_style('whitegrid')

# 创建示例数据 / Create sample data
X = np.random.randn(100, 2)
y = X[:, 0] * 1.5 - X[:, 1] * 2.0 + np.random.randn(100) * 0.5

# 创建图表 / Create plots
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# 散点图 / Scatter plot
axes[0].scatter(X[:, 0], y, alpha=0.5)
axes[0].set_xlabel('Feature X1')
axes[0].set_ylabel('Target y')
axes[0].set_title('Feature X1 vs Target')

# 直方图 / Histogram
axes[1].hist(y, bins=20, alpha=0.7, edgecolor='black')
axes[1].set_xlabel('Target Value')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Target Distribution')

plt.tight_layout()
plt.savefig('data/processed/visualization.png', dpi=150)
plt.show()

print("可视化图表已保存到 data/processed/visualization.png")
```

## 运行这些示例 / Running These Examples

将以上代码保存为 Python 脚本或在 Jupyter Notebook 中运行。
Save the above code as Python scripts or run in Jupyter Notebook.

```bash
# 运行 Python 脚本 / Run Python script
python examples/basic_workflow.py

# 或启动 Jupyter Notebook / Or start Jupyter Notebook
jupyter notebook
```

## 下一步 / Next Steps

1. 查看详细文档: [环境配置](ENVIRONMENT_SETUP.md) 和 [数据库文档](DATABASE.md)
2. 尝试修改示例代码以适应你的数据
3. 添加自定义模型和数据处理方法
4. 探索更多高级功能
