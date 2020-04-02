#密码重试练习
user_password = 'a12345'
x = 3

while x > 0:
	password = input('请输入您的密码：')
	if password == user_password:
		print('登录成功！')
		break
	else:
		x = x - 1
		print('登录失败，你还有',x,'次机会')