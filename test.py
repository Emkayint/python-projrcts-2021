data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input())
#your code goes here
adult = 0
child = 0
for x in data.values():
    if x > age:
        adult += 1
    
    if x <= age:
        child += 1
        
tatal = adult*20 + child * 5
print("no of adults :" , + adult )
print("no of children:" ,+ child)

#before disc
adult1 = 0
child1 = 0
for w in data.values():
	if w > 18:
		adult1 += 1
	
	if w <= 18:
		child1 += 1
		
tatal1 = (child1 * 5 + adult1* 20)

discount = (tatal - tatal1)/tatal1 * 100

print(int(discount))
		
		
    
