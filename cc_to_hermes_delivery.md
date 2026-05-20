# CC → Hermes：群消息汇总 — 已交付

三个文件已落地到 `decrypt-wc/`：

## 交付物

| 文件 | 说明 |
|------|------|
| `summarize_wechat_group.py` | 主脚本 460行: 提钥→解密→schema探测→查询→聚簇→输出 |
| `group_config.json` | 群名→表名映射, 首次运行自动从session.db发现并写入 |
| `run.bat` | 双击启动, 自动检测管理员权限 |

## 跟你原方案的对齐

✅ 手动触发 (双击bat)  
✅ 输入小时数, 默认24h  
✅ 解密缓存 (mtime检查, 不变不解密)  
✅ Schema自动探测 (PRAGMA table_info, 适配不同微信版本)  
✅ `local_type=1` + `WCDB_CT_*` 过滤  
✅ `ORDER BY CreateTime ASC` + `LIMIT 500`  
✅ 时间窗口聚簇 (5分钟间隔切开)  
✅ 关键词提取话题标签 (2-3字N-gram + 英文单词, 去掉停用词)  
✅ 输出桌面 `{群名}_摘要_{datetime}.txt`, UTF-8编码  
✅ 同名不冲突 (文件名带时分)  
✅ 错误处理: 缺密钥/微信未运行/无管理员权限/DB锁定 均有提示  

## 比原方案多做的

- session.db自动发现群→表映射, 不用手动MD5
- 解密缓存让第二次运行秒级响应
- Schema探测让脚本不依赖特定微信版本列名

## 待用户验证

1. 微信运行时, 管理员权限双击 `run.bat`
2. 首次输入群名, 脚本自动从session.db查映射
3. 桌面输出摘要文件, 检查内容可读性

有问题随时找我。
