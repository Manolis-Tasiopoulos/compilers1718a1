#------------------------------------------Dictionaries-----------------------------------------
td = { 'q0':{'thrNine':'q1', 'zerOne':'q4', 'two':'q2' },
       'q1':{ 'colon':'q3' },
       'q2':{ 'colon':'q3', 'zerThree':'q1' },
       'q3':{ 'zerFive':'q5',  },
       'q4':{ 'colon':'q3', 'zerNine':'q2' },
       'q5':{ 'zerNine':'q6' }             
     } 


ad = { 'q6':'TIME_TOKEN' }
#------------------------------------------Functions-------------------------------------------
def getchar(times,pos):
	
	check_array = ['colon', 'thrNine', 'zerNine', 'zerThree','zerFive', 'zerOne', 'two']
	check = False

	if pos < 0 or pos >= len(times): 		
		check_array = []
		return check_array
	if not(ord(times[pos]) == ord(':') or ord(times[pos]) == ord('.')):
		check_array.remove('colon')
		check = True		
	if not(ord(times[pos]) >= ord('3') and ord(times[pos]) <= ord('9')): 			
		check_array.remove('thrNine')
		check = True
	if not(ord(times[pos]) >= ord('0') and ord(times[pos]) <= ord('9')):  	
		check_array.remove('zerNine')
		check = True
	if not(ord(times[pos]) >= ord('0') and ord(times[pos]) <= ord('3')): 	
		check_array.remove('zerThree')
		check = True
	if not(ord(times[pos]) >= ord('0') and ord(times[pos]) <= ord('5')): 	
		check_array.remove('zerFive')
		check = True
	if not(ord(times[pos]) >= ord('0') and ord(times[pos]) <= ord('1')): 			
		check_array.remove('zerOne')
		check = True
	if not(ord(times[pos]) == ord('2')): 			
		check_array.remove('two')
		check = True

	if not check:
		check_array = ['ERROR']
	
	return check_array
	

def scan(text,transition_table,accept_states):
	
	pos = 0
	state = 'q0'
	
	while True:
		check = False		
		c = getchar(text,pos)				
		for i in c:
			if state in transition_table and i in transition_table[state] and not check:					
					state = transition_table[state][i]	
					pos += 1		
					check = True
					break											
		if not check:
			if state in accept_states:
				return accept_states[state],pos

			
			return 'ERROR_TOKEN',pos			

#------------------------------------------Main_Program------------------------------------------
print('\n\n		***DFA TIME RECOGNITION***\n')				
temp = input('		      -check: ')

while temp:		
	token,position = scan(temp,td,ad)
	print('\n		     ---RESAULTS---')
	
	print("	             string:",temp)
	print("	             token: ",token)
	print('	             --------------\n')		
	break
