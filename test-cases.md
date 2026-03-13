# ddup 测试用例设计

## 功能测试用例

### T01: 状态查询
- **命令**: `python ddup.py status`
- **预期**: 显示文件数、总大小
- **验证点**: 输出包含"文件数"、"总大小"

### T02: Heartbeat任务
- **命令**: `python ddup.py run`
- **预期**: 执行快照+安全检查
- **验证点**: 返回success:true

### T03: 创建快照
- **命令**: `python ddup.py snapshot`
- **预期**: 生成snapshots/日期.json
- **验证点**: 文件存在且包含timestamp

### T04: 备份功能
- **命令**: `python ddup.py backup`
- **预期**: 创建backups/日期_时间/
- **验证点**: 目录存在、包含meta.json

### T05: 安全检查
- **命令**: `python ddup.py security`
- **预期**: 检查配置文件
- **验证点**: 返回passed状态

### T06: 记忆列表
- **命令**: `python ddup.py memory`
- **预期**: 列出md文件
- **验证点**: 输出文件列表

### T07: 备份列表
- **命令**: `python ddup.py list-backups`
- **预期**: 列出备份目录
- **验证点**: 输出备份列表

### T08: 错误处理
- **命令**: `python ddup.py invalid_cmd`
- **预期**: 显示帮助信息
- **验证点**: 返回错误提示

## 集成测试用例

### T09: 文件创建
- **验证**: 执行snapshot后文件存在

### T10: 数据格式
- **验证**: JSON文件可解析

### T11: 多次执行
- **验证**: 多次运行snapshot数据追加

## 性能测试用例

### T12: 执行时间
- **验证**: run命令<10秒

## 兼容性测试

### T13: Python版本
- **验证**: Python 3.x兼容
