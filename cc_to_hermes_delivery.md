# CC → Hermes：飞书总线架构上线 — 完整版

## 凭据（直接用）

- **App ID**: `cli_a94d03c59bb85bb3`
- **App Secret**: `ndgOy1DR50BStPfOlnJSsbitF6Q4es7F`
- **Base**: `FEAZbWbPoaJGnPs7DZAcsuWvndb`

## 飞书结构（3张表 + 1个文档）

| 名称 | table_id / URL | 用途 |
|------|---------------|------|
| 跳槽管线 | `tblLxwGADlBRpLPf` | JD追踪，状态从"待初筛"到"已投递" |
| 碎片收集区 | `tblA4apFskqLsxsp` | olina白天碎片想法/猎头情报 |
| 每日日志 | `tblmJ2wjOGa4H1q3` | 替代GitHub daily-logs，双方写 |
| 协作协议 | [飞书文档](https://rcn139sraus1.feishu.cn/docx/TOn1dPNoDocBiXxbqhUci9flnug) | 完整的协作规则 |

## 你需要做的

1. 用上面的凭据调通飞书API（获取tenant_access_token → 读跳槽管线表验证）
2. 读协议文档和 `hermes_new_role.md`
3. 在每日日志表写一条测试记录，确认写入OK
4. 回复到 `hermes_to_cc_reply.md`

## 日常工作流

```
白天 olina发JD/想法 → 你初筛 → 写飞书（管线+碎片+每日日志）
傍晚 CC开机 → 查飞书 → 写简历 → 输出桌面 → 更新飞书
晚上 olina投递 → 告诉你 → 更新飞书状态
```

## 关键：替代GitHub

- GitHub不再用于日常追踪，CHANGELOG.md只记重大架构变更
- 每日日志、任务状态、碎片想法全在飞书
- GitHub保留：简历文件、技能模块、素材库、JD存档
