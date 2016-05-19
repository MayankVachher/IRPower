import enchant

f = open("customWords.txt",'w')
f.close()

pwl = enchant.request_pwl_dict("customWords.txt")
d = enchant.Dict("en_US")
singleLetters = ['a','i']

def validateLeft(variable):
	return d.check(variable) or pwl.check(variable)

def compute(variable, parent):
	if variable == '': return True
	if len(variable) == 1: return []
	tempRes = []
	for i in reversed(range(1,len(variable)+1)):
		resLeft = validateLeft(variable[:i])
		if resLeft:

			resRight = compute(variable[i:],variable[:i])
			if(resRight == True and i!=1): tempRes.append([[variable[:i].lower()]]) # Don't add single letter entries
			elif(len(variable[:i]) == 1 and variable[:i].lower() not in singleLetters): pass # If single letter entries are not 'i' or 'a', move on
			else: # Recursively check for all words in right part of entries
				for y in resRight:
					innerRes = [variable[:i]]
					for entry in y:
						innerRes+=entry
					tempRes.append([innerRes])
	return tempRes

def check(variable):
	variable = variable.replace('_','')
	perm = []
	for x in compute(variable,''):
		perm.append((x[0], len(x[0])))

	cleaned = sorted(perm, key = lambda x: x[1]) # Rank the list based on number of terms found
	print "\n***********\n"
	print "Suggestions for",variable,"are: "

	final_reco = []
	
	for sugg in cleaned[:10]:
		print sugg[0]
		child_reco = ''
		for indi_component in sugg[0][:-1]:
			child_reco += indi_component+", "
		child_reco += sugg[0][-1]
		final_reco.append(child_reco)

	return final_reco

	
	print "\n***********\n"