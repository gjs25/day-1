def bottle_song(num):
	for x in range(num,0,-1): #num is the input we give and we want to create a step range that decrements by 1
		if x == 1:  #change to no more bottles
			print (f"1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall!")
		
		elif x ==2: #change to singular 
			print (f"2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall.")
			
		elif x > 1: #exercise for loop 
			print (f"{x} bottles of beer on the wall, {x} bottles of beer. Take one down and pass it around, {x-1} bottles of beer on the wall.")


(bottle_song(50))
