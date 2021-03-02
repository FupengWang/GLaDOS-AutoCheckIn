# GLaDOS-AutoCheckIn
GLaDOS每日自动签到并钉钉通知

## 使用方法
1,使用浏览器开发人员工具或者FD抓包获取当前登录账号的cookie信息 填入'AutoCheckIn.py'第21行

2,如需要启用钉钉群通知请修改'AutoCheckIn.py'第9行与第10行的钉钉机器人配置信息

3,关闭钉钉群机器人通知及启用本地通知等请按照注释说明删除'AutoCheckIn.py'中相应代码

## 自动签到
可配置腾讯云函数或部署Github Action实现每日自动签到

腾讯云函数程序入口为main_handler



