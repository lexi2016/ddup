# DDUP1.0 - 多智能体协作平台

> 一个指令，一个团队

## 简介

DDUP1.0（多智能体协作平台）让用户用自然语言指令快速创建可协作的AI团队。

## 特性

- 🎯 **自然语言创建团队** - 一句话创建多Agent协作团队
- 🤖 **智能任务分发** - 自动拆分任务给合适的Agent
- 📊 **结果自动汇总** - 聚合各Agent输出为统一报告
- 📦 **预置团队模板** - 短视频、数据分析、产品发布团队

## 安装

```bash
# 克隆仓库
git clone https://github.com/lexi2016/ddup.git
cd ddup

# 或使用Gitee
git clone https://gitee.com/lexi2016/ddup.git
```

## 快速开始

```python
from ddup import DDUP

# 创建DDUP实例
ddup = DDUP()

# 查看可用模板
print(ddup.list_templates())
# ['短视频团队', '数据分析团队', '产品发布团队']

# 从模板创建团队
team = ddup.create_team_from_template("数据分析团队")

# 执行任务
results = ddup.execute_task(team.team_id, "分析宁德时代投资价值")

# 汇总结果
report = ddup.aggregate_results(team.team_id)
print(report)
```

## 使用示例

### 场景1：创建短视频团队

```
用户：帮我创建一个短视频团队

DDUP：
✓ 已创建"短视频团队"
├── 编导Agent - 负责脚本创作
├── 拍摄Agent - 负责内容拍摄
└── 剪辑Agent - 负责后期制作
```

### 场景2：数据分析

```
用户：分析宁德时代投资价值

DDUP：
✓ 已创建"数据分析团队"
├── 数据收集Agent - 获取财报、研报数据
├── 数据分析Agent - 分析财务指标、行业趋势
└── 报告生成Agent - 生成投资分析报告
```

## 项目结构

```
ddup/
├── ddup.py              # 核心逻辑
├── SKILL.md             # Skill定义
├── README.md            # 使用说明
├── 技术方案.md          # 技术文档
└── config/
    └── templates/       # 预置模板
```

## 技术架构

- **主Agent** - 负责意图理解、任务分发、结果汇总
- **子Agent** - 通过sessions_spawn创建执行子任务
- **记忆存储** - 共享memory目录存储上下文

详见 [技术方案.md](技术方案.md)

## 版本

- v1.0 (2026-03-13) - MVP版本

## 贡献

欢迎提交Issue和PR！

## 许可证

MIT License
