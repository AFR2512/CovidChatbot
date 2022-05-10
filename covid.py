#module covid
import patterns
import re


def CovidSymptoms(symptomes):
	score_symp = 0
	liste_symp = patterns.symptomes
	liste_grave = patterns.graves
	for grv in liste_grave:
		if re.search(grv,symptomes) is not None:
			return 999
	for symp in liste_symp:
		if re.search(symp, symptomes) is not None:
			score_symp += 1
	return score_symp



def vaccination(description):
	match = re.search(patterns.pattern,str(description))
	if match is not None:
		match_age = int(match.group("age"))
		comorbidite = match.group("desease")
		if match_age >= 75:
			return True
		elif match_age >= 18 and match_age <= 75:
			if comorbidite != None:
				return True
			else:
				return False
	else:
		return description


	
