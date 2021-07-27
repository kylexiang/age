password = '123456';
a = 0;
while a<3:
	key = input("请输入密码：");
	if key == password:
		print("登入成功！");
		break
	if key != password:
		a = a + 1;
		b = 3 - a;
		if b != 0:
			print("密码错误！还有",b,"次机会");
		else:
			print("登入机会已用完！");
