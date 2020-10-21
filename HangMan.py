def clear():
    import os
    os.system( 'clear' )
    
    
a1 = ''' 
   +---+
       |
       |
       |
       ==='''
a2 = ''' 
   +---+
   O   |
       |
       |
       ==='''


a3 = ''' 
   +---+
   O   |
   |   |
       |
       ==='''

a4 = ''' 
   +---+
   O   |
  /|\  |
       |
       ==='''



a5 = ''' 
   +---+
   O   |
  /|\  |
  / \  |
       ==='''


list=[]
l=[]
chan=0
g=0
a = "-"
n = "sajid"
for length in range(len(n)):
	list.append(a)

active=True
while active:
	if chan==5:
		clear()
		print(a5)
		print("You lose")
		print(f"The Word is {n}")
		active=False
	elif g == (len(n)):
		clear()
		print("You won")
		print(f"Word is {n}")
		active=False
	else:
		clear()
		print("Chances of wrong = 5")
		for lt in list:
			print(lt,end="")
		
		if len(l) != 0:
			if len(l) == 1:
				print(a1)
			elif len(l) == 2:
				print(a2)
			elif len(l) == 3:
				print(a3)
			elif len(l) == 4:
				print(a4)
			
			print("\n\nWrong Letters Used")
			for ll in l:
				print(ll,end=",")
		
		a = input("\n\n")
		for el in a:
			if el in n and el not in list:
				g+=1
				list.pop(n.index(el))
				list.insert(n.index(el),el)
			if el not in n and el not in l:
				chan+=1
				l.append(el)
		
