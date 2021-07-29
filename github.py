dic1={1:10,2:20,3:10,4:20,5:10,6:20}
flag=0
print("Sample: ",dic1)

key=int(input("Enter key : "))
for i in dic1.keys():
	if key==i:
		print("Yes,key",i," exists in dictionary")
		flag=1
if flag==0:
	print("No,key",key," does not exist in dictionary")
