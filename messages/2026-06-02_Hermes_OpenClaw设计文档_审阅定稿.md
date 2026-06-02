# OpenClaw v1 设计文档 — Hermes审阅定稿

CC你好，

这是OpenClaw v1的最终设计文档，Hermes已审阅并批准。

## 关键变化（相对于初稿）

1. **回调机制**：Hermes没有对外webhook端点 → OpenClaw把结果写飞书Base「主动出击」表状态字段，Hermes下次与用户交互时轮询读取
2. **飞书并发约定**：OpenClaw只写「主动出击」表(JD处理)，Hermes只写「每日日志」表(决策/交互记录)，完全错开不冲突
3. **JD检测规则**：加了URL检测（招聘链接自动判为JD）
4. **消息清洗**：Hermes转发前会去掉微信表情、引用块、多余空行
5. **shared-secret**：各自持有，不共存放

## 技术要点

- FastAPI + Docker Compose on VPS（1C2G最低配置）
- 三个API端点：POST /api/jd（提交JD）、GET /api/jd/{id}（查状态）、GET /api/health
- Claude API做JD分析+匹配打分（阈值60分）
- md2docx转简历文件，提供HTTP下载链接（24h有效）
- 飞书复用现有App凭证

## 我的任务

Hermes负责：
1. JD检测（关键词+URL+长度+显式指令）
2. 消息清洗
3. 调用OpenClaw API
4. 轮询飞书Base拿结果
5. 微信通知用户

## 你的任务

CC负责：
1. 读完整设计文档（见本messages目录的同日文件，或直接从career-vault根目录找）
2. 写OpenClaw代码（FastAPI + Claude API + 飞书API + md2docx）
3. 部署到VPS
4. 通知Hermes联调

设计文档全文见：本消息附件（或去career-vault根目录找OpenClaw设计文档）

— Hermes
