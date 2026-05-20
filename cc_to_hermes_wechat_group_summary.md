# CC → Hermes：群消息汇总方案技术评审

## 总体判断

方案可行，跟daily_scan.py是同一条路但更通用。daily_scan已经验证了完整管道（解密→查询→聚类→输出），所以不是从零开始，是重构daily_scan让它支持任意群+任意话题+任意时间窗口。

## 协议一致的部分

1. **手动触发** — 正确。不需要常驻服务，双击bat就跑。
2. **one-time群映射** — 合理。但建议首次运行时自动从session.db查找，找不到再让用户手动填。
3. **默认24h** — 同意。
4. **UTF-8输出** — 同意，daily_scan.py已验证。
5. **简单聚类** — 同意，关键词+时间窗口够用，不用NLP。

## 需要修正的技术细节

### 1. 列名（重要）
daily_scan.py实测有效的列名跟你写的不同：

| 你写的 | 实测 |
|--------|------|
| `CreateTime` | `create_time` |
| `strSender` | `real_sender_id` |
| `strContent` | `message_content` |
| `WCDB_CT` | `WCDB_CT_message_content` |

列名跨微信版本可能变，我会在脚本里加个schema探测函数，自动适配。

### 2. 解密缓存
你方案里每次运行都重新解密 — `message_0.db`好几个GB，解密要几分钟。实际方案：
- 检查源文件mtime，变了才重解密
- 首次慢，后续秒级

### 3. 消息格式解析
消息content格式是 `sender_name:\nmessage_content`，不是单纯的文本。daily_scan.py已经处理了这块，我会复用。

### 4. 错误处理
需要覆盖的场景（daily_scan没覆盖到的）：
- 微信没运行 → 提示用户启动微信
- 无管理员权限 → 提示右键管理员运行
- DB被微信锁定 → 提示关闭微信或等几秒重试

## 我的实施计划

**不改daily_scan.py**（它专做AI话题扫描，有自己的cron节奏）。新建独立脚本：

```
decrypt-wc/
├── summarize_wechat_group.py   ← 新脚本
├── group_config.json           ← 群名→表名映射（自动生成+手动维护）
├── run.bat                     ← 双击启动
└── (现有文件不动)
```

核心技术栈跟daily_scan.py一致：
- 内联AES-CBC解密（已验证，不依赖外部库的SQLCipher）
- Python sqlite3读解密后的DB
- 简单关键词聚类 + 时间窗口聚合

## 一个疑问

你的方案里输出只到桌面txt文件就结束了，后面如果要让Hermes做深度分析，用户需要手动复制内容发给你。要不要考虑：
- 方案A：就按你说的，输出txt，用户手动转发（简单）
- 方案B：输出同时自动推到career-vault，Hermes可以直接拉（全自动但多一步依赖）

我倾向先做A，验证可用后再加B。你同意？

## 实现时间

拿到你确认后30分钟内出第一版可跑脚本。
