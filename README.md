# ddup - OpenClaw Agent Management Toolkit

English | [中文](#中文)

## Overview

A comprehensive management toolkit for OpenClaw AI agents, providing:

- 📸 Regular system status snapshots
- 🧠 Automatic long-term memory management  
- 💾 Automatic backup of important configurations
- 🔒 Security checking of core files
- 🌙 Automatic learning and evolution during midnight

## Quick Start

```bash
# Clone the repository
git clone https://github.com/lexi2016/ddup.git ~/.openclaw/skills/ddup

# Run all tasks
cd ~/.openclaw/skills/ddup
python ddup.py run
```

## Commands

| Command | Description |
|---------|-------------|
| `python ddup.py run` | Execute all incremental tasks |
| `python ddup.py snapshot` | Create system snapshot |
| `python ddup.py backup` | Backup configuration files |
| `python ddup.py security` | Run security check |
| `python dddd.py status` | View storage status |

## Features

### System Snapshot
Automatically records OpenClaw agent status, including runtime information, active sessions, and system health.

### Memory Management  
Manages long-term memory across sessions, enabling persistent knowledge retention.

### Auto Backup
Automatically backs up critical configuration files (SOUL.md, AGENTS.md, TOOLS.md, etc.).

### Security Check
Validates integrity of core configuration files and detects suspicious modifications.

---

## 中文

## 概述

OpenClaw智能体管理工具，为AI智能体提供：

- 📸 定期记录系统状态
- 🧠 自动管理长期记忆
- 💾 自动备份重要配置
- 🔒 安全检查核心文件
- 🌙 凌晨自动学习进化

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/lexi2016/ddup.git ~/.openclaw/skills/ddup

# 运行所有任务
cd ~/.openclaw/skills/ddup
python ddup.py run
```

## 命令

| 命令 | 描述 |
|------|------|
| `python ddup.py run` | 执行所有增量任务 |
| `python ddup.py snapshot` | 创建系统快照 |
| `python ddup.py backup` | 备份配置文件 |
| `python ddup.py security` | 运行安全检查 |
| `python ddup.py status` | 查看存储状态 |

## 功能说明

### 系统快照
自动记录OpenClaw智能体状态，包括运行时信息、活动会话、系统健康状况。

### 记忆管理
管理跨会话的长期记忆，实现持久化知识保留。

### 自动备份
自动备份关键配置文件（SOUL.md、AGENTS.md、TOOLS.md等）。

### 安全检查
验证核心配置文件的完整性，检测可疑修改。

## License

MIT License
