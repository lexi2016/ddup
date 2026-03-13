#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ddup CLI 入口
使用方法:
    python ddup.py run        # 执行Heartbeat
    python ddup.py snapshot   # 创建快照
    python ddup.py backup     # 备份
    python ddup.py security   # 安全检查
    python ddup.py memory      # 查看记忆
    python ddup.py status     # 存储状态
"""

import sys
import os
import json
import subprocess
import shutil
from datetime import datetime

# 设置UTF-8输出
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 项目根目录
ROOT = os.path.dirname(os.path.abspath(__file__))

def get_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_timestamp():
    return datetime.now().isoformat()

# ===== snapshot =====
def create_snapshot():
    """创建系统快照"""
    try:
        result = subprocess.run(
            "openclaw status", shell=True, capture_output=True, text=True, timeout=30, encoding='utf-8', errors='ignore'
        )
        status = {"returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        status = {"error": str(e)}
    
    timestamp = get_timestamp()
    date = get_date()
    
    snapshot_data = {"timestamp": timestamp, "date": date, "openclaw_status": status}
    
    snapshot_file = os.path.join(ROOT, "snapshots", f"{date}.json")
    
    existing = []
    if os.path.exists(snapshot_file):
        with open(snapshot_file, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    
    existing.append(snapshot_data)
    
    with open(snapshot_file, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    
    return snapshot_data

# ===== backup =====
def backup_workspace():
    """备份工作空间"""
    date = get_date()
    timestamp = datetime.now().strftime("%H%M%S")
    backup_name = f"{date}_{timestamp}"
    backup_dir = os.path.join(ROOT, "backups", backup_name)
    
    os.makedirs(backup_dir, exist_ok=True)
    
    workspace = os.path.dirname(ROOT)
    config_files = ["SOUL.md", "AGENTS.md", "MEMORY.md", "TOOLS.md"]
    
    for config_file in config_files:
        src = os.path.join(workspace, config_file)
        if os.path.exists(src):
            dst = os.path.join(backup_dir, config_file)
            shutil.copy2(src, dst)
    
    meta = {"backup_name": backup_name, "date": date, "timestamp": timestamp, "files": config_files}
    meta_file = os.path.join(backup_dir, "meta.json")
    with open(meta_file, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    
    return backup_name

def list_backups():
    backup_dir = os.path.join(ROOT, "backups")
    if not os.path.exists(backup_dir):
        return []
    
    backups = []
    for name in os.listdir(backup_dir):
        path = os.path.join(backup_dir, name)
        if os.path.isdir(path):
            backups.append(name)
    return sorted(backups, reverse=True)

# ===== security =====
def security_check():
    workspace = os.path.dirname(ROOT)
    core_files = ["SOUL.md", "AGENTS.md", "MEMORY.md", "TOOLS.md"]
    
    result = {"timestamp": get_timestamp(), "passed": True, "missing_files": [], "suspicious": []}
    
    for filename in core_files:
        filepath = os.path.join(workspace, filename)
        if not os.path.exists(filepath):
            result["missing_files"].append(filename)
            result["passed"] = False
    
    return result

# ===== memory =====
def get_memory_list():
    files = []
    for f in os.listdir(ROOT):
        if f.endswith('.md') and f[0].isdigit():
            files.append(f)
    return sorted(files, reverse=True)

# ===== storage =====
def get_storage_info():
    total_size = 0
    file_count = 0
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            fp = os.path.join(root, f)
            total_size += os.path.getsize(fp)
            file_count += 1
    return {"total_size": total_size, "file_count": file_count}

# ===== heartbeat =====
def run_heartbeat():
    """执行Heartbeat任务"""
    results = {"tasks": [], "success": True}
    
    # 1. 快照
    try:
        snap = create_snapshot()
        results["tasks"].append({"name": "snapshot", "status": "success", "timestamp": snap.get("timestamp")})
    except Exception as e:
        results["tasks"].append({"name": "snapshot", "status": "error", "error": str(e)})
        results["success"] = False
    
    # 2. 安全检查
    try:
        sec = security_check()
        results["tasks"].append({"name": "security", "status": "success" if sec["passed"] else "warning", "passed": sec["passed"]})
    except Exception as e:
        results["tasks"].append({"name": "security", "status": "error", "error": str(e)})
        results["success"] = False
    
    return results

# ===== main =====
def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1].lower()
    
    if cmd == "run":
        print("🔄 执行Heartbeat任务...")
        result = run_heartbeat()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
    elif cmd == "snapshot":
        print("📸 创建系统快照...")
        result = create_snapshot()
        print(f"✅ 快照已创建: {result.get('timestamp')}")
        
    elif cmd == "backup":
        print("💾 执行备份...")
        result = backup_workspace()
        print(f"✅ 备份完成: {result}")
        
    elif cmd == "list-backups":
        print("📋 备份列表:")
        for b in list_backups():
            print(f"  - {b}")
        
    elif cmd == "security":
        print("🔒 执行安全检查...")
        result = security_check()
        print(f"✅ 检查完成，通过: {result.get('passed')}")
        if result.get('missing_files'):
            print(f"⚠️ 缺失文件: {result['missing_files']}")
            
    elif cmd == "memory":
        print("🧠 记忆列表:")
        for f in get_memory_list():
            print(f"  - {f}")
            
    elif cmd == "status":
        print("📊 存储状态:")
        info = get_storage_info()
        print(f"  文件数: {info['file_count']}")
        print(f"  总大小: {info['total_size']} bytes")
        
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)

if __name__ == "__main__":
    main()
