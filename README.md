# ACon AI 自动化工具仓库

## 仓库定位

本仓库定位为面向 **财务/税务/Excel/PDF** 的自动化工具库骨架，后续可持续扩展为可复用的命令行工具与脚本集合，支持日常财务运营的自动化需求。

## 推荐使用方式

- **命令行**：用于执行标准化、可复用的自动化任务。
- **脚本**：用于一次性或定制化的任务编排。

## 快速开始

```bash
# 安装（开发模式）
pip install -e .

# 查看 CLI 帮助
python -m acon_ai_tools --help

# 运行示例命令
python -m acon_ai_tools hello
python -m acon_ai_tools doctor
```

## 目录说明

```
.
├── docs/                # 文档
├── examples/            # 示例数据/示例用法
├── scripts/             # 一次性脚本入口
├── src/acon_ai_tools/   # 主包
│   ├── utils/           # 通用工具（日志、路径、时间、配置读取）
│   ├── cli.py           # CLI 入口
│   └── __init__.py
├── tests/               # pytest 测试
├── pyproject.toml       # 项目配置
└── README.md
```

## 开发规范

- **分层**：核心业务代码放在 `src/acon_ai_tools`，一次性脚本放在 `scripts/`，示例数据放在 `examples/`。
- **命名**：模块名使用小写 + 下划线，类使用驼峰，函数使用动词开头。
- **日志**：统一使用 `utils.logging.get_logger`，避免直接在业务代码中配置全局 logging。
- **异常处理**：在 CLI 层统一捕获并输出可读错误信息；模块层抛出语义化异常，避免吞错。
