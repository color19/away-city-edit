# away · The City Edit 现有网站结构（2026-09-19 探索）
- 技术：Expo（React Native Web）单页应用，一个 JS 包，无独立后端源码；访问需 ChatGPT 登录。
- 页面：Discover（月份、大洲、Top N、结果卡片、城市详情）与 Preferences（出发机场、大洲、预算、天数、舒适度、排序、look ahead）。
- 数据接口：GET /api/fares?origin=IAD&month=2026-10&minDays=9&maxDays=15
  返回 {rows:[{destination, nonstop:{ready,average,observations}, oneStop:{...}}], updatedAt, windowDays:30, minimumSamples:5}
  现状 rows 为空，所以页面显示 "The top 0"。
- 城市数据（内嵌前端）：id, name, region, code, color, tag, desc, score, Unsplash photo id, restaurants（餐厅推荐）。
- 偏好保存在浏览器 localStorage；出发机场约 18 个美国机场；月份 Sep 2026–Mar 2027。
- 配色：主色 #183f36，辅色 #79847a，背景 #f7f6f0。
