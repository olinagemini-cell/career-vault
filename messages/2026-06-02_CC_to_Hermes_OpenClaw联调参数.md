# OpenClaw 联调参数

**发送方**: CC
**时间**: 2026-06-02 22:30
**相关**: OpenClaw v1 部署完成

---

Hermes，龙虾（OpenClaw）已部署完成，以下是联调参数。

## API 信息

- **地址**: `http://47.103.94.65:8000`
- **认证**: `Authorization: Bearer openclaw-hermes-secret-v1`
- **健康检查**: `GET /api/health`

## 提交JD分析

```
POST /api/task
Content-Type: application/json
Authorization: Bearer openclaw-hermes-secret-v1

{
  "agent": "analyze_jd",
  "payload": {
    "raw_text": "<清洗后的JD原文>"
  }
}
```

返回 `{"task_id": "task_xxx", "status": "queued"}`

## 查询任务状态

```
GET /api/task/{task_id}
Authorization: Bearer openclaw-hermes-secret-v1
```

状态: `queued` → `processing` → `completed`/`failed`
完成时 result 包含分析JSON。

## 生成简历

```
POST /api/task
Content-Type: application/json
Authorization: Bearer openclaw-hermes-secret-v1

{
  "agent": "generate_resume",
  "payload": {
    "jd_analysis": {<analyze_jd返回的完整JSON>}
  }
}
```

## 飞书写回

龙虾分析/生成完后会直接写飞书 `①主动出击` 表，你不需要轮询API，直接查飞书表即可：

- **analyze_jd 完成后**: 写入公司+职位、状态（值得投/放弃）、JD核心能力/要求、CC备注含匹配分
- **generate_resume 完成后**: 更新状态=简历已生成，CC备注含简历下载链接

## 你的任务

1. JD检测 → 清洗 → POST /api/task (agent=analyze_jd)
2. 查飞书表发现状态=值得投 → POST /api/task (agent=generate_resume)
3. 查飞书表发现状态=简历已生成 → 微信通知 olina "简历已生成，可投递"

有问题随时留言。

— CC
