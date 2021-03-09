def jiecheng(n): # 定义一个函数名是jiecheng,参数为n的函数
	if n==1:     # 当参数n为1时，返回n的值
		return n    # 结束函数，并返回一个值n给函数
	n = n*jiecheng(n-1)   # 当不满足n==1时，进行递推，n!=n*(n-1)!
	return n     # 结束函数，并返回一个值n给函数
m = jiecheng(5)  # 将函数中的参数n赋值为5，将函数值赋值给m
print(m)         # 打印出m的值
