# 数据库设计说明

**适用范围**：AI智能运动动作矫正系统\
**数据库规范**：表名 lower\_snake\_case，主键 id，时间字段 created\_at/updated\_at，包含 is\_deleted

## 1. 实体清单

- sys\_user (用户表)
- sport\_type (运动类型表)
- sport\_record (运动记录表)
- sys\_config (系统配置表)
- ai\_chat\_session (AI会话表)
- knowledge\_article (运动知识表)
- &#x20;

## 2. 表结构设计

### 2.1 sys\_user (用户表)

**主键**：id\
**索引**：uk\_username, uk\_openid, idx\_phone

| 字段名            | 类型         | 长度  | 是否为空 | 默认值                | 描述                      |
| :------------- | :--------- | :-- | :--- | :----------------- | :---------------------- |
| id             | BIGINT     | 20  | NO   | AUTO\_INCREMENT    | 主键 ID                   |
| username       | VARCHAR    | 50  | NO   | -                  | 用户名                     |
| password\_hash | VARCHAR    | 255 | YES  | -                  | 密码哈希值                   |
| openid         | VARCHAR    | 64  | YES  | -                  | 微信 OpenID               |
| unionid        | VARCHAR    | 64  | YES  | -                  | 微信 UnionID              |
| avatar\_url    | VARCHAR    | 255 | YES  | -                  | 头像 URL                  |
| phone          | VARCHAR    | 20  | YES  | -                  | 手机号                     |
| gender         | TINYINT(1) | 1   | YES  | 0                  | 性别 (0:未知, 1:男, 2:女)     |
| age            | INT        | 3   | YES  | -                  | 年龄                      |
| height         | FLOAT      | -   | YES  | -                  | 身高 (cm)                 |
| weight         | FLOAT      | -   | YES  | -                  | 体重 (kg)                 |
| nick\_name     | VARCHAR    | 64  | YES  | -                  | 昵称                      |
| role           | VARCHAR    | 20  | NO   | 'user'             | 角色 (super, admin, user) |
| status         | VARCHAR    | 20  | NO   | 'active'           | 状态 (active, inactive)   |
| created\_at    | DATETIME   | -   | NO   | CURRENT\_TIMESTAMP | 创建时间                    |
| updated\_at    | DATETIME   | -   | NO   | CURRENT\_TIMESTAMP | 更新时间                    |
| is\_deleted    | TINYINT(1) | 1   | NO   | 0                  | 逻辑删除标记                  |

### 2.2 sport\_type (运动类型表)

**主键**：id\
**索引**：uk\_code

| 字段名         | 类型         | 长度 | 是否为空 | 默认值                | 描述     |
| :---------- | :--------- | :- | :--- | :----------------- | :----- |
| id          | BIGINT     | 20 | NO   | AUTO\_INCREMENT    | 主键 ID  |
| name        | VARCHAR    | 50 | NO   | -                  | 运动名称   |
| code        | VARCHAR    | 50 | NO   | -                  | 运动代码   |
| status      | VARCHAR    | 20 | NO   | 'active'           | 状态     |
| created\_at | DATETIME   | -  | NO   | CURRENT\_TIMESTAMP | 创建时间   |
| updated\_at | DATETIME   | -  | NO   | CURRENT\_TIMESTAMP | 更新时间   |
| is\_deleted | TINYINT(1) | 1  | NO   | 0                  | 逻辑删除标记 |

### 2.3 sport\_record (运动记录表)

**主键**：id\
**索引**：idx\_user\_id, idx\_sport\_type\_id, idx\_created\_at

| 字段名              | 类型         | 长度 | 是否为空 | 默认值                | 描述                            |
| :--------------- | :--------- | :- | :--- | :----------------- | :---------------------------- |
| id               | BIGINT     | 20 | NO   | AUTO\_INCREMENT    | 主键 ID                         |
| user\_id         | BIGINT     | 20 | NO   | -                  | 用户 ID (外键关联 sys\_user.id)     |
| sport\_type\_id  | BIGINT     | 20 | NO   | -                  | 运动类型 ID (外键关联 sport\_type.id) |
| duration         | INT        | -  | NO   | 0                  | 运动时长 (秒)                      |
| correct\_count   | INT        | -  | NO   | 0                  | 正确次数                          |
| incorrect\_count | INT        | -  | NO   | 0                  | 错误次数                          |
| detail\_json     | JSON       | -  | YES  | -                  | 详细数据 (骨架点/角度等)                |
| created\_at      | DATETIME   | -  | NO   | CURRENT\_TIMESTAMP | 创建时间                          |
| updated\_at      | DATETIME   | -  | NO   | CURRENT\_TIMESTAMP | 更新时间                          |
| is\_deleted      | TINYINT(1) | 1  | NO   | 0                  | 逻辑删除标记                        |

### 2.4 sys\_config (系统配置表)

**主键**：id\
**索引**：uk\_config\_key

| 字段名           | 类型         | 长度  | 是否为空 | 默认值                | 描述     |
| :------------ | :--------- | :-- | :--- | :----------------- | :----- |
| id            | BIGINT     | 20  | NO   | AUTO\_INCREMENT    | 主键 ID  |
| config\_key   | VARCHAR    | 50  | NO   | -                  | 配置键名   |
| config\_value | TEXT       | -   | YES  | -                  | 配置值    |
| description   | VARCHAR    | 255 | YES  | -                  | 描述     |
| created\_at   | DATETIME   | -   | NO   | CURRENT\_TIMESTAMP | 创建时间   |
| updated\_at   | DATETIME   | -   | NO   | CURRENT\_TIMESTAMP | 更新时间   |
| is\_deleted   | TINYINT(1) | 1   | NO   | 0                  | 逻辑删除标记 |

### 2.5 ai\_chat\_session (AI会话表)

**主键**：id\
**索引**：idx\_user\_id

| 字段名            | 类型         | 长度 | 是否为空 | 默认值                | 描述                        |
| :------------- | :--------- | :- | :--- | :----------------- | :------------------------ |
| id             | BIGINT     | 20 | NO   | AUTO\_INCREMENT    | 主键 ID                     |
| user\_id       | BIGINT     | 20 | NO   | -                  | 用户 ID (外键关联 sys\_user.id) |
| session\_id    | VARCHAR    | 64 | NO   | -                  | 会话标识                      |
| message\_count | INT        | -  | NO   | -                  | 消息数量                      |
| created\_at    | DATETIME   | -  | NO   | CURRENT\_TIMESTAMP | 创建时间                      |
| updated\_at    | DATETIME   | -  | NO   | CURRENT\_TIMESTAMP | 更新时间                      |
| is\_deleted    | TINYINT(1) | 1  | NO   | 0                  | 逻辑删除标记                    |

### 2.6 knowledge\_article (运动知识表)

**主键**：id\
**索引**：idx\_category

| 字段名         | 类型         | 长度  | 是否为空 | 默认值                | 描述     |
| :---------- | :--------- | :-- | :--- | :----------------- | :----- |
| id          | BIGINT     | 20  | NO   | AUTO\_INCREMENT    | 主键 ID  |
| title       | VARCHAR    | 128 | NO   | -                  | 标题     |
| category    | VARCHAR    | 64  | NO   | -                  | 分类     |
| content     | TEXT       | -   | NO   | -                  | 内容     |
| status      | TINYINT    | 1   | NO   | -                  | 状态     |
| created\_at | DATETIME   | -   | NO   | CURRENT\_TIMESTAMP | 创建时间   |
| updated\_at | DATETIME   | -   | NO   | CURRENT\_TIMESTAMP | 更新时间   |
| is\_deleted | TINYINT(1) | 1   | NO   | 0                  | 逻辑删除标记 |

### 2.7 model\_version (模型版本表)

**主键**：id\
**索引**：uk\_model\_code

| 字段名            | 类型           | 长度 | 是否为空 | 默认值                | 描述      |
| :------------- | :----------- | :- | :--- | :----------------- | :------ |
| id             | BIGINT       | 20 | NO   | AUTO\_INCREMENT    | 主键 ID   |
| model\_code    | VARCHAR      | 64 | NO   | -                  | 模型代码    |
| model\_name    | VARCHAR      | 64 | NO   | -                  | 模型名称    |
| version\_tag   | VARCHAR      | 32 | NO   | -                  | 版本标签    |
| accuracy\_rate | DECIMAL(5,2) | 5  | NO   | -                  | 准确率     |
| latency\_ms    | INT          | -  | NO   | -                  | 延迟 (ms) |
| created\_at    | DATETIME     | -  | NO   | CURRENT\_TIMESTAMP | 创建时间    |
| updated\_at    | DATETIME     | -  | NO   | CURRENT\_TIMESTAMP | 更新时间    |
| is\_deleted    | TINYINT(1)   | 1  | NO   | 0                  | 逻辑删除标记  |

### 2.8 correction\_report (矫正报告表)

**主键**：id\
**索引**：idx\_user\_id, idx\_sport\_record\_id

| 字段名                       | 类型         | 长度  | 是否为空 | 默认值                | 描述                              |
| :------------------------ | :--------- | :-- | :--- | :----------------- | :------------------------------ |
| id                        | BIGINT     | 20  | NO   | AUTO\_INCREMENT    | 主键 ID                           |
| user\_id                  | BIGINT     | 20  | NO   | -                  | 用户 ID (外键关联 sys\_user.id)       |
| sport\_record\_id         | BIGINT     | 20  | NO   | -                  | 运动记录 ID (外键关联 sport\_record.id) |
| summary\_text             | VARCHAR    | 512 | NO   | -                  | 总结文本                            |
| error\_distribution\_json | TEXT       | -   | YES  | -                  | 错误分布数据                          |
| created\_at               | DATETIME   | -   | NO   | CURRENT\_TIMESTAMP | 创建时间                            |
| updated\_at               | DATETIME   | -   | NO   | CURRENT\_TIMESTAMP | 更新时间                            |
| is\_deleted               | TINYINT(1) | 1   | NO   | 0                  | 逻辑删除标记                          |

