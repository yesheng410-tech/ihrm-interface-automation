
# iHRM登录接口自动化测试项目

## 项目介绍
基于Python实现的iHRM人力资源管理系统登录接口自动化测试项目，覆盖14条核心测试场景，包含参数化、全量字段校验、批量执行及报告生成功能。

## 技术栈
- 语言：Python
- 接口请求：requests
- 测试框架：unittest
- 数据驱动：JSON
- 全量字段校验：JSON Schema
- 报告生成：pytest-html

## 项目结构
ihrm-interface-automation/

├──api/ # 接口对象层

├── common/ # 通用工具（数据读取、Schema 校验、断言工具）

├── data/ # 测试数据（登录用例 JSON 文件）

├── scripts/ # 测试用例（登录接口测试脚本）

├── requirements.txt # 项目依赖

└── README.md # 项目说明


## 使用方法
1. 克隆仓库：`git clone https://github.com/你的GitHub用户名/ihrm-interface-automation.git`
2. 安装依赖：`pip install -r requirements.txt`
3. 运行用例：`unittest scripts/test_login.py --html=report.html`



