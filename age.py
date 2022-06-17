driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入: 有/沒有')
	raise SystemExit


age = input('請問你的年齡?')
age = int(age)

if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('蝦!你開過車?')

elif driving == '沒有':
	if age >= 18:
		print('你可以考照了呀')
	else :
		print('很好 在幾年後就可以考了')
