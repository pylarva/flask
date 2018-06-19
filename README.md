# flask
>flask实践项目  
1. flask基本使用
2. 前后端数据传送
3. 配置文件设置
4. 登陆验证装饰器？
5. 路由系统
    * 通过装饰器生成 闭包 实质是add_url_rule来实现
    * endpoint 默认返回函数名
    * 页面重定向 redirect_to
    * 子域名访问 subdomain
    * 不支持正则表达会（需要扩展支持）
6. 模板
    * 可以定制执行函数
    * 防止代码注入攻击 | safe 或者 markup
7. 请求和响应
    * request
    * make_response 返回字符和cookie         
8. session
    * app.secret_key
9. 蓝图
    * pro_flask_simple
10. 上下文管理   
    * 前提  
    1）threading.Local 为每一个单独的进程开辟内存空间  
    2）flask实现的自定义Local对象用来为协程开辟单独空间  
    * 请求到来   
    1）ctx = 封装RequestContext(request, session)     
    2）ctx放到Local中
    * 执行视图函数  
    1）导入request   
    2）使用request  
    print（request） --> LocalProxy对象的__str__    
       request.method --> LocalProxy对象的__getattr__
       调用_lookup_req_object函数：去Local中将requestContext中获取到
       再去requestContext中获取request或session
    * 结束请求  
    1）ctx.auto_pop()  
    2）ctx从Local中移除
    
11. 使用DBUtils实现数据库连接池  
    db_helper
    
12. WTForm表单验证

13. 数据库ORM: SQLAchemy

14. 插件
    * flask-script
    * flask-migrate  
    python run.py db init   
    python run.py db migrate   
    python run.py db upgrade   
       