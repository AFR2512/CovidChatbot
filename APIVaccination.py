#API Vaccination
import re
import requests, json
import urllib.parse
import pandas as pd
from math import sin, cos, acos, pi,floor

api_url = "https://api-adresse.data.gouv.fr/search/?q="
sivac = "https://www.data.gouv.fr/fr/datasets/r/5cb21a85-b0b0-4a65-a249-806a040ec372"
centres = pd.read_csv(sivac, sep = ";")


def get_centres_departement(adresse):
	code_post = re.findall("[0-9]+", adresse)
	departement = code_post[1][0:2]
	a = centres[centres["com_cp"] >= float(departement)*1000]
	b = centres[centres["com_cp"] <= (float(departement)+1)*1000]
	centres_departement = pd.merge(a, b, how ='inner', on =["com_cp"])
	return centres_departement

def get_geolocalisation(adresse):
	r = requests.get(api_url + urllib.parse.quote(adresse))
	coord = r.content.decode('unicode_escape')
	data = json.loads(r.content)
	ici = data['features'][0]['geometry']['coordinates']
	return ici

def deg2rad(dd):
	return dd/180*pi

def distanceGPS(latA, longA, latB, longB):
	RT = 6378137
	S = acos(sin(latA)*sin(latB) + cos(latA)*cos(latB)*cos(abs(longB-longA)))
	return S*RT/1000
 

def centre_le_plus_proche(adresse):
	localisation = get_geolocalisation(adresse)
	centres_proches = get_centres_departement(adresse)
	plus_proches = []
	latA = deg2rad(localisation[1])
	longA = deg2rad(localisation[0])
	for i in range(centres_proches.shape[0]):
		latB = deg2rad(centres_proches.iloc[i][10])
		longB = deg2rad(centres_proches.iloc[i][11])
		plus_proches.append(distanceGPS(latA,longA,latB,longB))
	a = min(plus_proches)
	less_distance = plus_proches.index(a)
	plus_proche = centres_proches.iloc[less_distance]
	return plus_proche["nom_x"] + ", " + plus_proche["adr_num_x"]+ " "+plus_proche["adr_voie_x"]+", "+str(floor(plus_proche["com_cp"])) + ", " + plus_proche["com_nom_x"]+ ", numero telephone : "+plus_proche["rdv_tel_x"]



