x = 2
password = 'a123456'
while x >= 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else: 
		print('密碼錯誤!,還有', int(x) , '次機會')
		x = x-1
