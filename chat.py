#Module de chat et conversations
import covid
import stats
import APIVaccination
import patterns
import re


prec = []

def choix(text):
	message = text.lower()
	if prec == []:
		if match(patterns.pattern_choix_demarrer,message) is not None:
			return "CovidBot Bienvenue! Vous pouvez :  \n - Vérifier vos symptomes \n - Calculer votre éligibilité à la vaccination \n - Consulter les chiffres hospitaliers du jour \n - Savoir quel centre de vaccination est le plus proche de chez vous "
		elif match(patterns.pattern_choix_stop,message) is not None:
			return "CovidBot au revoir 'noubliez pas les gestes barrières ! "
		elif match(patterns.pattern_choix_symptomes,message) is not None:
			prec.append("symptomes")
			return "Vous etes malade ? Décrivez vos symptomes "
		elif match(patterns.pattern_choix_vaccination,message) is not None:
			prec.append("vaccination")
			return "Calcul de l'éligibilité à la vaccination décrivez vos critères "
		elif match(patterns.pattern_choix_statistiques,message) is not None:
			return "En France : \n hospis {hosp} \n réas {rea}".format(hosp = stats.get_hospis(), rea = stats.get_reas())
		elif match(patterns.pattern_choix_centres,message) is not None:
			prec.append("centre")
			return "Centre de vaccination le plus proche : \n Entrez votre adresse complète (numéro, Rue, code postal, ville)"
		else:
			return "Je n'ai pas compris :( "

	elif prec[len(prec)-1] == "symptomes":
		del prec[len(prec)-1]
		res = covid.CovidSymptoms(message)
		if res > 5:
			return "Vous faites une forme grave appelez le 15 immédiatement"
		elif res > 0 and res <= 5 : 
			return "Vous avez des symptomes du covid vous devriez vous faire tester par PCR"
		else : 
			return "Vous n'avez pas de symptomes covid testez vous par Antigénique si vous avez des doutes"

	elif prec[len(prec)-1] == "vaccination":
		del prec[len(prec)-1]
		res = covid.vaccination(message)
		if res == True:
			return "Vous êtes éligibles à la vaccination ! "
		elif res == False:
			return "Vous n'êtes pas encore éligible à la vaccination pour le moment :("
		else:
			return message
	elif prec[len(prec)-1] == "centre":
		del prec[len(prec)-1]
		proche = APIVaccination.centre_le_plus_proche(message)
		return proche

def match(liste_pattern, string):
	for pattern in liste_pattern:
		if re.search(pattern,str(string)) is not None:
			return True
	return None






