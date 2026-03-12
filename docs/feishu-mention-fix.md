# OpenClaw 飞书群聊 @Mention 问题修复记录

## 问题描述

在飞书群聊中使用 OpenClaw 机器人发送消息时，如果在消息文本中使用 `@用户名` 格式，飞书无法正确识别为 @mention，导致被@的用户收不到通知。

### 错误示例

```plaintext
@张哥 该你回复了。
```

飞书显示为纯文本，用户不会收到 @ 通知。

### 正确示例

```plaintext
<at user_id="ou_f78b42c53c52588d013e6ed55d239ec2">张哥</at> 该你回复了。
```

飞书正确识别 @mention，用户收到通知。

---

## 问题根因

OpenClaw 的飞书消息发送模块在发送消息时，没有自动将 `@用户名` 文本转换为飞书要求的 `<at user_id="...">用户名</at>` 格式。

飞书 API 要求：
- 在消息内容中使用 `at` 类型的 `user_id` 字段
- 而非简单的文本 `@用户名`

---

## 解决方案

### 方案一：修改 OpenClaw 代码（推荐）

在飞书消息发送逻辑中添加自动转换：

```python
# 伪代码示例
def convert_mention_to_feishu(text, user_map):
    """将 @用户名 转换为飞书格式"""
    for name, user_id in user_map.items():
        text = text.replace(f"@{name}", f'<at user_id="{user_id}">{name}</at>')
    return text
```

### 方案二：使用飞书 API 直接发送

通过飞书 SDK 发送消息，指定 `msg_type: "text"` 并在 `content` 中包含 `user_id` 字段。

---

## 用户ID映射

| 用户 | 飞书 User ID |
|------|-------------|
| 张哥 | ou_f78b42c53c52588d013e6ed55d239ec2 |
| 小红 | ou_da31d4656caff649eb97511f6777f68d |
| 小琼 | ou_7cafda7380891f3324e251c91adfe25e |
| 宇   | ou_25d1596012f051dddf718ac5604857a5 |

---

## 测试验证

1. 使用正确格式发送消息
2. 确认被@用户收到飞书通知
3. 确认消息中显示 @mention 链接

---

## 相关文件

- OpenClaw 源码：`src/plugins/feishu/`
- 飞书文档：https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN

---

## 更新日志

- 2026-03-12: 首次记录问题
