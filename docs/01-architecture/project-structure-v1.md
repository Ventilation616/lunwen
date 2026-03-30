# 项目目录结构设计（v1）

## 1. 后端目录结构（完整树形）
```text
flask/
  .idea/
    inspectionProfiles/
      profiles_settings.xml
    .gitignore
    misc.xml
    modules.xml
    服务器端.iml
  photos/
    click_icon.png
    demo.jpg
    demo1.jpg
    homeLogo_ns.png
    homeLogo_s.png
    icon_exitLogin.png
    icon_history.png
    icon_personInfo.png
    index1.jpg
    knowledgeLogo_ns.png
    knowledgeLogo_s.png
    myselfLogo_ns.png
    myselfLogo_s.png
    point_icon.png
    sport_SitUp.jpg
    sport_pushUp.gif
    sport_pushUp.jpg
  tmp/
    tmp.jpg
  flaskrun.py
```

**职责说明**
- flask/：后端服务入口与资源目录
- flask/.idea/：开发环境配置与工程文件
- flask/.idea/inspectionProfiles/：代码检查配置
- flask/photos/：后端展示与示例图片资源
- flask/tmp/：临时文件与缓存文件存放

## 2. 前端目录结构
```text
miniprogram/
  cloudfunctions/
    sportHistory/
      miniprogram_npm/
      config.json
      index.js
      package-lock.json
      package.json
  image/
    click_icon.png
    demo.jpg
    demo1.jpg
    homeLogo_ns.png
    homeLogo_s.png
    icon_exitLogin.png
    icon_history.png
    icon_personInfo.png
    index1.jpg
    knowledgeLogo_ns.png
    knowledgeLogo_s.png
    myselfLogo_ns.png
    myselfLogo_s.png
    point_icon.png
    sport_SitUp.jpg
    sport_pushUp.gif
    sport_pushUp.jpg
  miniprogram_npm/
  pages/
    history/
      history.js
      history.json
      history.wxml
      history.wxss
    home/
      index.js
      index.json
      index.wxml
      index.wxss
    index/
      index.js
      index.json
      index.wxml
      index.wxss
    knowledge/
      knowledge.js
      knowledge.json
      knowledge.wxml
      knowledge.wxss
    logs/
      logs.js
      logs.json
      logs.wxml
      logs.wxss
    myself/
      myself.js
      myself.json
      myself.wxml
      myself.wxss
    prompt/
      index.js
      index.json
      index.wxml
      index.wxss
    sport/
      sport.js
      sport.json
      sport.wxml
      sport.wxss
    sportTwo/
      sportTwo.js
      sportTwo.json
      sportTwo.wxml
      sportTwo.wxss
  utils/
    util.js
  .eslintrc.js
  app.js
  app.json
  app.wxss
  package-lock.json
  package.json
  project.config.json
  project.private.config.json
  sitemap.json
```

**职责说明**
- miniprogram/：微信小程序主体工程
- miniprogram/cloudfunctions/：云函数集合
- miniprogram/cloudfunctions/sportHistory/：运动记录相关云函数
- miniprogram/cloudfunctions/sportHistory/miniprogram_npm/：云函数依赖包
- miniprogram/image/：小程序图片与图标资源
- miniprogram/miniprogram_npm/：小程序端依赖包
- miniprogram/pages/：小程序页面集合
- miniprogram/pages/history/：运动历史记录页面
- miniprogram/pages/home/：首页与入口页面
- miniprogram/pages/index/：主功能入口页面
- miniprogram/pages/knowledge/：知识科普页面
- miniprogram/pages/logs/：日志或调试页面
- miniprogram/pages/myself/：个人中心页面
- miniprogram/pages/prompt/：提示与引导页面
- miniprogram/pages/sport/：运动分析与训练页面
- miniprogram/pages/sportTwo/：运动分析扩展页面
- miniprogram/utils/：工具函数与通用能力封装

## 3. docs 目录结构
```text
docs/
  01-architecture/
    module-breakdown-v1.md
    project-structure-v1.md
    system-architecture-v1.md
```

**职责说明**
- docs/：项目文档总目录
- docs/01-architecture/：架构与结构类文档

## 4. sql 目录结构
```text
sql/
```

**职责说明**
- sql/：数据库结构脚本与初始化数据
