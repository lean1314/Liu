
# Liu
Yummy ，share your love
 
 这是大学中一个课程项目的拓展
 目的是为了让更多的人能够知道更好的高端零食
 没有申请域名和服务器，用的是flask搭建的mysql数据库后台


## 准备

需要安装的库

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import desc
from flask import jsonify
from flask import request
import copy
```

配置数据库

```python
app=Flask(__name__)
#实例Flask对象
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:123456@localhost:3306/test1?charset=utf8'
#配置数据库 采用本地mysql建立test1数据库
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SECRET_KEY"]="xxx"
#为数据库添加识别key xxx
db=SQLAlchemy(app)
#实例化数据库
```

### 需求分析

**用户**

- [x] 用户登录(wx)
- [x] 查看评价

**平台**

- [x] 轮播图广告
- [x] 品类展示
- [x] 推荐展示

**内容社区**

- [x] 文章展示
- [x] 产品跳转

**产品**

- [x] 产品信息
- [x] 用户评分
- [x] 购买跳转



### 编写逻辑

**前端**

![前端流程图](https://github.com/lean1314/Liu/blob/test/images/前端流程图.png)

**后端**

![后端流程图](https://github.com/lean1314/Liu/blob/test/images/后端流程图.png)

**总体闭环设计**

| Yummy       |               线上零食评分社区                                |
| ----------- | ------------------------------------------------------------ |
| 制作人      | 朱浩南、刘庭伟                                               |
| 日期        | 2020年06月20日                                               |
| 小程序名称  | Yummy                                                        |
| 功能说明    | 平台展示、产品简介、食品评价、购买链接跳转、食品社区         |
| 小程序Pages | 1）index：平台页  2)my：个人页   3）list1：种类页4）logs：登录页   5)search：搜索页 6）detail：详情页7）comment：评价页  8） discover：发现页9）article：社区文章页 |
| 数据库      | 采用mysql搭建数据库 ：comments评价表/products产品表          |
| 小程序闭环  | 1. 平台页浏览-搜索-商品详情页-评价(购买)                                                                                                    2. 平台页浏览-推荐-商品详情页-评价(购买)                                                                                                3. 平台页浏览-种类-商品详情页-评价(购买)                                                                                                4. 发现页浏览-社区文章页-商品详情页-评价(购买) |
| 使用方法    | 1. 执行后端文件 sql.py运行数据库与后端                                                                                                         2. 导入微信开发工具的Yummy项目                                                                                                           3.实现前端与后端连接，获取数据库数据并完成评分、小程序跳转购买等功能。 |
