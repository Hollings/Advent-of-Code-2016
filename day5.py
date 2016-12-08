import hashlib

input = "wtnhxymk"
m = hashlib.md5()
# m.update(input.encode())
# print(m.hexdigest())
found = False
i=0
answer = ""

while(len(answer)<8):
	check = input+str(i)
	m = hashlib.md5()
	m.update(check.encode())

	if(str(m.hexdigest())[:5] == "00000"):
		found = True
		answer = answer + m.hexdigest()[5]

	# So my computer doesn't crash
	if i>10000000:
		found = True
	
	i+=1
	
print(answer)
