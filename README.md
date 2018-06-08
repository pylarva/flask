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
    