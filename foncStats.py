#utf-8
import re
import nltk
from nltk.tokenize import word_tokenize
import pprint
import treetaggerwrapper

"""
	IMPORTANT! Pour pouvoir utiliser ce module il faut avoir installé nltk et treetaggerwrapper
	C'est un module qui regroupe tous les traitements et les statistiques basiques sur un texte
	Ce module permet d'obtenir facilement le résultat pour les statistiques simples, mais souvent nécessaires pour les linguistes ou TAListes
	Ce module contient 10 fonctions dont 8 fonctions statistiques (nomlet(), nommot(), freqmot(), freqpattern(), freqphrase(), lonphrase(), patcont(), tok_nltk()) et 2 fonctions qui effectuent un traitement sur le texte (SupprEsp(), tok())
	 
"""

# début nombre de caractères
def nomlet(arg):
	"""
		Compte le nombre de caractères dans le texte
		Prend le texte en argument
	"""
	res=len(arg)
	return res
#fin nombre de caractères	
	
	
	
#début nombre de mots	
def nommot(arg):
	"""
		Compte le nombre de mots dans le texte
		Prend le texte en argument
	"""
	res=len(arg.split())
	return res
# fin nombre de mots
	
	
	
	
#début mot particulier
def freqmot(mot, texte):
	"""
		Compte fréquence d'un mot particulier au choix de l'utilisateur
		Entrée: mot, texte
	"""
	compt=0
	mot=mot.lower()
	texte=texte.lower()
	texte=texte.split()
	for i in texte:
		if i==mot:
			compt+=1
	return compt
#fin mot particulier	



# fréquence de l'apparition d'un pattern
def freqpattern (mot, texte):
	"""
		Compte la fréquence d'un mot ou un pattern au choix de l'utilisateur
		La différence avec la fonction freqmot est que non seulement les mots sont pris en compte, mais n'importe quelle combinaison de caractères
		Entrée: pattern, texte
	"""
	compt=0
	chercher=re.findall(r'{}'.format(mot), texte)
	for i in chercher:
		compt+=1
	return compt
# fin fréquence pattern



#début nombre de phrases
def freqphrase(texte):
	"""
		Compte le nombre de phrases dans le texte
		Entrée: Texte
	"""
	compt=0
	texte=texte.split(".\n")
	textt=".\t".join(texte)
	texte=textt.split(".\t")
	textt="! ".join(texte)
	texte=textt.split("! ")
	textt="? ".join(texte)
	texte=textt.split("? ")
	textt=". ".join(texte)
	texte=textt.split(". ")
	for i in texte:
		compt+=1
	return compt
# fin nombre de phrases



# longueur moyenne de la phrase
def lonphrase(texte):
	"""
	Compte la longueur moyenne d'un phrase dans le texte
	L'index est la différence entre le nombre de mots et de phrases dans le texte: N_mots/N_phrases
	Entrée: texte
	"""
	
	compt=0
	texte=texte.split(".\n")
	textt=".\t".join(texte)
	texte=textt.split(".\t")
	textt="! ".join(texte)
	texte=textt.split("! ")
	textt="? ".join(texte)
	texte=textt.split("? ")
	textt=". ".join(texte)
	texte=textt.split(". ")
	for i in texte:
		compt+=1

	count=0
	texte_mot=". ".join(texte)
	print(texte_mot)
	texte_mot=texte_mot.split()
	for i in texte_mot:
		count+=1
	
	return round((count/compt),3)
# fin longueur moyenne de la phrase
	
	
	
	
# fréquence d'un pattern en contexte
def patcont(mot, texte):
	"""
			Cherche avec le module re le pattern indiqué par l'utilisateur et renvoie les phrases dans lesquelles ce pattern se rencontre
			Entrée: pattern, texte
	"""
	phrases=[]
	texte=texte.split(".\n")
	textt=".\t".join(texte)
	texte=textt.split(".\t")
	textt="! ".join(texte)
	texte=textt.split("! ")
	textt="? ".join(texte)
	texte=textt.split("? ")
	textt=". ".join(texte)
	texte=textt.split(". ")
	print(texte)
	for i in texte:
		if mot in i:
			phrases.append(i)
	return "{}".format("\n".join(phrases))
# fin fréquence d'un pattern




#début de la focntion SupprEsp(mot) qui supprime tous les espaces
def SupprEsp(mot):
	"""
		Enlève les espaces de trop dans le texte
		Entrée: texte
		OUtput: mots sont séparés par un espace au plus
	"""
	chaineFinale=[]
	for i in range (0,len(mot)-1):
		if mot[i+1]==" "and mot[i]==" ":
			continue
		else:
			chaineFinale.append(mot[i])
	chaineFinale.append(mot[-1])
	if chaineFinale[0]==" ":
		del chaineFinale[0]
	if chaineFinale[-1] ==" ":
		del chaineFinale[-1]
	return "".join(chaineFinale)
# fin de la fonction SupprEsp(mot)




# début tagger
def tok(tex):
	"""
		Tag le texte et renvoie le texte taggé sous format facile à lire pour l'utilisateur en colonnes
		Entrée: texte
		Output: texte taggée
	"""
	tagger=treetaggerwrapper.TreeTagger(TAGLANG='fr')
	tags=tagger.tag_text(tex)
	tags2=treetaggerwrapper.make_tags(tags)
	pprint.pprint(tags2)
	empty=[]
	for tag in tags2:
		tagg=tag
		empty.append(tagg)
		print(empty)
	
	grammar=[]	
	for element in empty:
		for i in element:
#			if element.index(i)==0 or element.index(i)==1:
				grammar.append(i)
				grammar.append("\t")
		grammar.append("\n")
		res="".join(grammar)
		
	return "{}".format(res)
# fin tagger



#début richesse vocabulaire
def tok_nltk(tex):
	"""
		Renvoie l'index richesse du vocabulaire entre 0 et 1
		Entrée: Texte
		Output: float
	"""
	tokens_french=word_tokenize(tex, language='french')
	res=sorted(set(tokens_french))
	res2=(len(sorted(set(tokens_french)))/len(tokens_french))
	return "{}".format(round(res2,3))
#fin richesse vocabulaire


