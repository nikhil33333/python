
list = [10, 21, 4, 45, 66, 93, 1] 

even_count=0, odd_count = 0

 
for num in list: 
	
	# checking condition 
	if num % 2 == 0: 
		even_count += 1

	else: 
		odd_count += 1
		
print("Even numbers in the list: ", even_count) 
print("Odd numbers in the list: ", odd_count) 
