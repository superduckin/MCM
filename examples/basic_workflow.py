"""
示例工作流脚本 / Example Workflow Script
演示完整的数学建模流程 / Demonstrates complete mathematical modeling workflow
"""
import sys
import os

# 添加项目根目录到路径 / Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from src.data_processing import split_data, normalize_data
from src.models import LinearModel
from src.utils import setup_logger, get_timestamp


def main():
    """主函数 / Main function"""
    # 设置日志 / Setup logging
    logger = setup_logger('example_workflow')
    logger.info("=" * 50)
    logger.info("开始数学建模示例工作流 / Starting example workflow")
    logger.info("=" * 50)
    
    # 1. 生成示例数据 / Generate sample data
    logger.info("\n步骤 1: 生成示例数据 / Step 1: Generate sample data")
    np.random.seed(42)
    X = np.random.rand(200, 3)
    # 真实系数: [1.5, -2.0, 0.5] / True coefficients: [1.5, -2.0, 0.5]
    y = X @ np.array([1.5, -2.0, 0.5]) + np.random.randn(200) * 0.1
    logger.info(f"  数据形状 / Data shape: X={X.shape}, y={y.shape}")
    
    # 2. 数据标准化 / Normalize data
    logger.info("\n步骤 2: 数据标准化 / Step 2: Normalize data")
    X_normalized = normalize_data(X)
    logger.info(f"  标准化范围 / Normalized range: [{X_normalized.min():.4f}, {X_normalized.max():.4f}]")
    
    # 3. 划分训练集和测试集 / Split train and test sets
    logger.info("\n步骤 3: 划分数据集 / Step 3: Split dataset")
    X_train, X_test, y_train, y_test = split_data(X_normalized, y, test_size=0.2, random_state=42)
    logger.info(f"  训练集大小 / Training set size: {len(X_train)}")
    logger.info(f"  测试集大小 / Test set size: {len(X_test)}")
    
    # 4. 创建并训练模型 / Create and train model
    logger.info("\n步骤 4: 训练模型 / Step 4: Train model")
    model = LinearModel()
    model.train(X_train, y_train)
    logger.info("  模型训练完成 / Model training completed")
    
    # 5. 评估模型 / Evaluate model
    logger.info("\n步骤 5: 评估模型 / Step 5: Evaluate model")
    results = model.evaluate(X_test, y_test)
    logger.info(f"  均方误差 MSE / Mean Squared Error: {results['mse']:.6f}")
    logger.info(f"  R² 分数 / R² Score: {results['r2']:.6f}")
    
    # 6. 显示模型参数 / Display model coefficients
    logger.info("\n步骤 6: 模型参数 / Step 6: Model coefficients")
    coeffs = model.get_coefficients()
    logger.info(f"  模型系数 / Coefficients: {coeffs['coefficients']}")
    logger.info(f"  截距 / Intercept: {coeffs['intercept']:.6f}")
    logger.info(f"  (真实系数 / True coefficients: [1.5, -2.0, 0.5])")
    
    # 7. 总结 / Summary
    logger.info("\n" + "=" * 50)
    logger.info("工作流完成！/ Workflow completed!")
    logger.info("=" * 50)
    
    # 返回结果 / Return results
    return {
        'mse': results['mse'],
        'r2': results['r2'],
        'coefficients': coeffs['coefficients'],
        'intercept': coeffs['intercept']
    }


if __name__ == "__main__":
    try:
        results = main()
        print("\n" + "=" * 50)
        print("✅ 示例工作流执行成功！/ Example workflow executed successfully!")
        print(f"📊 模型性能 / Model Performance: R² = {results['r2']:.4f}")
        print("=" * 50)
    except Exception as e:
        print(f"\n❌ 工作流执行失败 / Workflow failed: {e}")
        import traceback
        traceback.print_exc()
