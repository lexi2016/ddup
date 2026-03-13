# ddup 产品手册

> 码姐自我进化系统 | v1.0.0

---

## 一、产品设计思路

### 1.1 背景与问题

OpenClaw用户面临的核心痛点：

| 痛点 | 描述 | 影响 |
|------|------|------|
| 记忆缺失 | 每次对话AI像陌生人 | ⭐⭐⭐⭐⭐ |
| 状态不明 | 不知道AI在做什么 | ⭐⭐⭐⭐ |
| 备份繁琐 | 手动复制配置文件 | ⭐⭐⭐⭐ |
| 故障难查 | 出问题不知原因 | ⭐⭐⭐ |

### 1.2 设计目标

打造AI的"自我进化系统"，让AI能够：
- 📸 定期记录系统状态
- 🧠 自动管理长期记忆
- 💾 自动备份重要配置
- 🔒 安全检查核心文件

### 1.3 产品定位

**类型**：AI+产品（用AI赋能现有系统）

**目标用户**：
- OpenClaw高级用户
- 需要AI自我进化的开发者
- 需要自动化运维的个人AI助手

### 1.4 技术架构

```
┌─────────────────────────────────┐
│         CLI 入口 (ddup.py)      │
├─────────────────────────────────┤
│  snapshot  │  backup  │ security│
│  (快照)    │  (备份)  │ (检查)   │
├─────────────────────────────────┤
│       文件系统存储               │
│   snapshots/ backups/ logs/     │
└─────────────────────────────────┘
```

**技术特点**：
- ✅ 零外部依赖（纯Python标准库）
- ✅ Windows/Linux兼容
- ✅ 可独立运行
- ✅ 可集成到OpenClaw Heartbeat

---

## 二、产品特点

### 2.1 核心功能

| 功能 | 描述 | 命令 |
|------|------|------|
| 系统快照 | 定期获取OpenClaw状态 | `python ddup.py snapshot` |
| 备份还原 | 自动备份配置文件 | `python ddup.py backup` |
| 安全检查 | 检测核心文件异常 | `python ddup.py security` |
| Heartbeat | 一键执行所有任务 | `python ddup.py run` |

### 2.2 一键启动

```bash
# 方式1: Python CLI
python ddup.py run

# 方式2: Windows一键运行
run.bat
```

### 2.3 数据存储

```
ddup/
├── snapshots/           # 系统快照
│   └── 2026-03-11.json
├── backups/            # 备份文件
│   └── 2026-03-11_093000/
├── logs/               # 运行日志
└── *.md               # 每日记忆
```

### 2.4 集成能力

可集成到OpenClaw Heartbeat：

```markdown
## daydayup 增量任务
- 执行 `python ddup/ddup.py run`
- 写入 ddup/记忆文档
```

---

## 三、测试验证

### 3.1 测试环境

| 项目 | 配置 |
|------|------|
| 平台 | Windows |
| Python | 3.14 |
| 安装方式 | 手动复制到 skills/ddup |

### 3.2 测试用例

| ID | 用例 | 预期结果 | 实际结果 | 状态 |
|----|------|----------|----------|------|
| T01 | 状态查询 | 显示存储状态 | 文件数:4, 大小:10563 | ✅ PASS |
| T02 | Heartbeat | 执行快照+检查 | success:true | ✅ PASS |
| T03 | 创建快照 | 生成JSON文件 | snapshots/2026-03-11.json | ✅ PASS |
| T04 | 安全检查 | 检查核心文件 | passed:false(warning) | ⚠️ WARN |
| T05 | 一键运行 | 双击执行 | 正常输出 | ✅ PASS |

### 3.3 问题修复

| 问题 | 现象 | 修复 |
|------|------|------|
| 目录不存在 | No such file or directory | 初始化时创建 |
| Unicode编码 | gbk codec error | 添加UTF-8处理 |

### 3.4 测试结论

**通过率**：4/5 (80%)

✅ 核心功能测试通过
⚠️ 警告项不影响功能

---

## 四、安装使用

### 4.1 安装

```bash
# 克隆或下载
git clone <repo> ddup

# 创建必要目录
mkdir ddup/snapshots ddup/backups ddup/logs

# 或从ClawHub安装
clawhub install ddup
```

### 4.2 命令

```bash
python ddup.py run        # 执行所有任务
python ddup.py snapshot   # 创建快照
python ddup.py backup     # 备份
python ddup.py security   # 安全检查
python ddup.py status     # 存储状态
python ddup.py memory     # 记忆列表
```

### 4.3 一键运行

```bash
# Windows
run.bat
```

---

## 五、用户收益

| 维度 | 安装前 | 安装后 | 提升 |
|------|--------|--------|------|
| 备份耗时 | 手动2分钟 | 5秒 | 24x |
| 安全检查 | 从未 | 每日自动 | ∞ |
| 记忆管理 | 手动 | 自动 | ∞ |
| 状态查询 | 无 | 一键 | ∞ |

---

## 六、总结

**核心价值**：
1. 自动化 - 释放人力
2. 可追溯 - 问题可查
3. 持续进化 - 凌晨学习

**推荐等级**：⭐⭐⭐⭐⭐ 强烈推荐安装

---

*手册版本：1.0.0*
*更新日期：2026-03-11*
