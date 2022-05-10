import re

#patterns regex
pattern = r"([a-zA-Z]+[']?[a-z]+)\s(?P<age>\d+)\s([a-z]+)(\s[a-z]+\s([a-zA-Z]+[']?[a-z]+?)\s([a-z]+)+\s(?P<desease>([a-z]+[']?)?([a-z]+)(\s[a-z]+(\s[a-z]+(\s[0-3])?)?)?))?" #pattern vaccination
symptomes = [r"fi[eè]vre([a-z]+)?", r"fatigu[eé][a-z]?", r"tou[xs]([a-z]+)?",r"diar[r]?h[ée][s]?",r"c[eé]phal[ée]([s])?",r"ma[lu][x]?\sde\t[eê]te",r"per[td][eu]\s[ld][']odorat",r"mal\s[aà]\sla\st[eê]te"] #pattern symptomes
graves = [r"mal\s[aà]\srespirer",r"difficult[eé][s]?\s[aà]\srespirer",r"op[p]?ress[é][e]?"] #pattern symptomes graves
pattern_choix_demarrer = [r"[Dd][ée]marrer", r"[Cc]ommencer",r"[Ss]tart",r"[Hh]ello",r"[Ss]alut",r"[Cc]onversation",r"[Bb]onjour"]
pattern_choix_stop = [r"[Bb]ye", r"[Aa]u\srevoir",r"[Ss]top(er)?",r"[Aa]rr[eê]t(er)?",r"[Ee]xit"]
pattern_choix_vaccination = [r"[Vv]accin([ea][rt](ion)?)?",r"[Eée]ligibilit[eé]"]
pattern_choix_symptomes = [r"[Ss]ympt[oô]me(s)?",r"malad(i)?e",r"signe(s)?"]
pattern_choix_centres = [r"[Cc]entre(s)?",r"[Ll]e(s)?\splus\sproche(s)?"]
pattern_choix_statistiques = [r"[Cc]hiffres",r"[Hh]opita[lu](x)?",r"[Eeé]volution",r"[Ss]tatistique(s)?"]

