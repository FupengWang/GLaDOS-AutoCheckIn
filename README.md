# GLaDOS-AutoCheckIn
GLaDOS每日自动签到并钉钉通知

## 使用方法
1,使用浏览器开发人员工具或者FD抓包获取当前登录账号的cookie信息 填入'AutoCheckIn.py'第23行

2,如需要启用钉钉群通知请修改'AutoCheckIn.py'第24行与第25行的钉钉机器人配置信息.若不填写,则不会开启钉钉群通知,仅本地控制台输出执行结果


## 自动签到
可配置腾讯云函数或部署Github Action实现每日自动签到

腾讯云函数程序入口为main_handler
