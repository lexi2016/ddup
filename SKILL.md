---
name: ddup
description: |
  OpenClaw Agent Management Toolkit. Provides automatic learning, memory management, system snapshots, backup/restore, and security checking for OpenClaw agents.
  
  为OpenClaw智能体打造的管理工具集，提供自动学习、记忆管理、系统快照、备份还原、安全检查等能力。
  
  触发场景（精确匹配）：
  - "每天自动备份" / "自动备份"
  - "查看系统状态" / "系统状态"
  - "执行Heartbeat" / "运行Heartbeat" / "Heartbeat任务"
  - "检查配置文件安全" / "安全检查"
  - "管理记忆" / "查看记忆" / "记忆管理"
  
  排除场景（不应触发）：
  - "备份数据库" / "备份文件" → 应触发其他备份skill
  - "查看股票状态" → 应触发股票skill
  - "发送邮件" → 应触发邮件skill
metadata:
  requires:
    bins: [python]
  install:
    - label: 自动安装
      command: |
        git clone https://github.com/lexi2016/ddup.git ~/.openclaw/skills/ddup
---

# ddup - OpenClaw Agent Management Toolkit

## 概述

OpenClaw智能体管理工具，让AI能够：
- 📸 定期记录系统状态
- 🧠 自动管理长期记忆
- 💾 自动备份重要配置
- 🔒 安全检查核心文件
- 🌙 凌晨自动学习进化

## 触发场景

当用户提到以下内容时触发：
- "执行每日任务"
- "运行Heartbeat"
- "查看系统快照"
- "备份工作空间"
- "检查配置文件"
- "查看存储状态"
- "一键备份"

## 快速开始

### 1分钟上手

```bash
# 进入目录
cd skills/ddup

# 执行所有任务
python ddup.py run
```

### 一键运行（Windows）

```bash
run.bat
```

## 功能说明

### 核心功能

| 命令 | 功能 | 示例 |
|------|------|------|
| `run` | 执行所有增量任务 | `python ddup.py run` |
| `snapshot` | 创建系统快照 | `python ddup.py snapshot` |
| `backup` | 备份配置文件 | `python ddup.py backup` |
| `security` | 安全检查 | `python ddup.py security` |
| `status` | 查看存储状态 | `python ddup.py status` |
| `memory` | 记忆列表 | `python ddup.py memory` |
| `list-backups` | 备份列表 | `python ddup.py list-backups` |

## 使用示例

### 日常使用

```bash
# 每天早上执行一次
python ddup.py run

# 查看存储状态
python ddup.py status
# 输出：
# 📊 存储状态:
#   文件数: 8
#   总大小: 19751 bytes

# 手动备份
python ddup.py backup
# 输出：
# 💾 执行备份...
# ✅ 备份完成: 2026-03-11_095159
```

### 集成到Heartbeat

在AGENTS.md中添加：

```markdown
## daydayup 增量任务
- 执行 `python ddup/ddup.py run`
```

### 集成到Cron（Linux）

```bash
# 每天 9:00 执行
0 9 * * * cd /path/to/skills/ddup && python ddup.py run
```

## 输出格式

### run 命令

```json
{
  "tasks": [
    {
      "name": "snapshot",
      "status": "success",
      "timestamp": "2026-03-11T09:51:54.051905"
    },
    {
      "name": "security",
      "status": "success",
      "passed": true
    }
  ],
  "success": true
}
```

### snapshot 命令

```json
{
  "timestamp": "2026-03-11T09:51:54.051905",
  "date": "2026-03-11",
  "openclaw_status": {
    "returncode": 0,
    "stdout": "...",
    "stderr": ""
  }
}
```

### backup 命令

```
💾 执行备份...
✅ 备份完成: 2026-03-11_095159
```

### security 命令

```
🔒 执行安全检查...
✅ 检查完成，通过: True
⚠️ 缺失文件: ['SOUL.md']
```

### status 命令

```
📊 存储状态:
  文件数: 8
  总大小: 19751 bytes
```

## 数据存储

```
ddup/
├── snapshots/              # 系统快照
│   └── 2026-03-11.json   # 每日快照数组
├── backups/               # 备份文件
│   └── 2026-03-11_093000/ # 时间戳目录
│       ├── SOUL.md
│       ├── meta.json
├── logs/                  # 运行日志
└── *.md                   # 记忆文档
```

## 注意事项

1. **首次运行**：确保snapshots、backups、logs目录存在
2. **权限**：确保有写入skills/ddup目录的权限
3. **路径**：建议使用绝对路径或从skills/ddup目录执行
4. **编码**：Windows下确保使用UTF-8编码

## 故障排查

| 问题 | 解决方案 |
|------|----------|
| 目录不存在 | 手动创建snapshots/backups/logs目录 |
| openclaw命令失败 | 检查openclaw是否正确安装 |
| 编码错误 | 确保Python输出UTF-8 |

## 参考资料

- [详细设计](references/ddup-design.md)
- [测试报告](TEST-REPORT-FORMAL.md)
- [PRD](PRD.md)
