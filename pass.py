#!/usr/bin python3
#passw =  'AAAaaaaa4444!!!!!@@@@@@@@@@@'
passww = input()
islower_i =  0
issuper_i =  0
isdigit_i =  0
j  = 0
def pass_good(password):
	global islower_i,issuper_i,isdigit_i,j
	if len(password) > 14:
		a =  list(password)
		for i in range(len(a)):
			if a[i].islower():
				islower_i += 1
			elif a[i].isupper():
				issuper_i += 1
			elif a[i].isdigit():
				isdigit_i += 1
			else:
				j += 1
		if islower_i >= 5 and issuper_i >= 3 and isdigit_i >= 4 and j >= 2:
			return True
		else:
			return False
	else:
		return False 
print(pass_good(passww))
