# ddup 详细设计文档

## 产品定位

**类型**：AI+产品（用AI赋能OpenClaw）

**目标用户**：
- OpenClaw高级用户
- 需要AI自我进化的开发者
- 需要自动化运维的个人AI助手

## 核心功能

### 1. 系统快照 (snapshot.py)
```python
# 获取OpenClaw状态
python ddup.py snapshot

# 输出
📸 快照已创建: 2026-03-11T09:27:21.220091
```

### 2. 备份还原 (backup.py)
```bash
# 备份
python ddup.py backup

# 列出备份
python ddup.py list-backups

# 还原
# 手动复制备份文件到工作空间
```

### 3. 安全检查 (security.py)
```bash
python ddup.py security

# 输出
🔒 执行安全检查...
✅ 检查完成，通过: True
```

### 4. Heartbeat任务
```bash
python ddup.py run

# 输出
🔄 执行Heartbeat任务...
{
  "tasks": [
    {"name": "snapshot", "status": "success", "timestamp": "..."},
    {"name": "security", "status": "success", "passed": true}
  ],
  "success": true
}
```

## 数据流

```
用户触发 → CLI解析 → 执行任务 → 写入文件 → 返回结果
```

## 存储结构

```
ddup/
├── snapshots/
│   └── 2026-03-11.json   # 每日快照数组
├── backups/
│   └── 2026-03-11_093000/ # 时间戳命名
│       ├── SOUL.md
│       ├── AGENTS.md
│       └── meta.json
└── 2026-03-11.md         # 每日记忆
```

## 扩展计划

### v1.1 新手引导
- 任务模板
- 向导程序

### v1.2 技能推荐
- 根据场景推荐OpenClaw skills

### v1.3 智能提醒
- 定时任务提醒
- 异常告警

## 技术特点

- ✅ 零外部依赖（纯Python标准库）
- ✅ Windows/Linux兼容
- ✅ 可独立运行
- ✅ 可集成到OpenClaw Heartbeat
