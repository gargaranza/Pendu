from tp6_fr_dic import fr_dic
from random import *
from turtle import *
from math import *
from random import *
from unicodedata import normalize


def asciize(s) :
	return normalize('NFKD', s).encode('ascii ', 'ignore').decode('ascii')

def mot_au_hasard() :
	global fr_dic
	#return 'pneumonoultramicroscopicsilicovolcanoconiosis'
	return fr_dic[randint(0,len(fr_dic))]

def mot_vers_liste(m) :
	L = ['_'] * len(m)
	L[0] = m[0]
	L[-1] = m[-1]
	return L

def met_a_jour2(L, m, c) :
	if c == m :
		for i in range(len(m)) :
			L[i] = m[i]
		return True
	b = False
	M = asciize(m)
	for i in range(len(m)) :
		if M[i] == c and asciize(L[i]) != c :
			b = True
			L[i] = m[i]
	return b

def met_a_jour(L, m, c) :
	M = asciize(m)
	for i in range(len(m)) :
		if M[i] == c and asciize(L[i]) != c :
			L[i] = m[i]
	return L

def lettre_valide(m,mem,l) :
	if not(l in [chr(i) for i in range(ord('a'),ord('z') + 1)]) and len(l) != len(m) or l in mem :
		return False
	else :
		return True

def restart() :
	while True :
		test = input('On rejoue ?')
		test = test.lower()
		if test in ['y', 'yes','o','oui'] :
			print('Ok on est reparti !')
			return True
		elif test in ['n', 'x' , 'no', 'non'] :
			print('Ok :''(')
			return False
		else :
			print('je n''ai pas compris')

Pi = 3.141592
def cercle(c,r,deb) :
	
	def trace_parametrique(tmin,tmax,fx,fy,dt) :
		t=tmin
		(x,y)=(fx(t),fy(t))
		up() ; goto(x,y) ; down()
		while t<tmax:
			(x,y) = (fx(t),fy(t))
			goto(x,y)
			t=t+dt
		
	def x(t) : return c[0] + r * cos(t + deb)
	def y(t) : return c[1] + r * sin(t + deb)
	
	trace_parametrique(0,2 * Pi,x,y,0.1)


def dessin_pendu2(étape) :
	if étape == 1 :
		up()
		goto(-250, -300)
		down()
		goto(50, -300)
		up()
	elif étape == 2 :
		up()
		goto(-100 ,-300)
		down()
		goto(-100, 300)
		up()
	elif étape == 3 :
		up()
		goto(-100, 300)
		down()
		goto(200, 300)
		up()
	elif étape == 4 :
		up()
		goto(0,300)
		down()
		goto(-100, 200)
		up()
	elif étape == 5 :
		up()
		goto(200, 300)
		down()
		goto(200, 200)
		up()
	elif étape == 6 :
		up()
		cercle((200,170),30,Pi/2)
		up()
	elif étape == 7 :
		up()
		goto(200,140)
		down()
		goto(200,0)
		up()
	elif étape == 8 :
		up()
		goto(200,0)
		down()
		goto(150,-50)
		up()
		goto(250,-50)
		down()
		goto(200,0)
		up()
	elif étape == 9 :
		up()
		goto(150,100)
		down()
		goto(250,100)
		up()



def candidats(deb, fin, l) :
	L = []
	for i in fr_dic :
		if len(i) == l and asciize(i)[0] == deb and asciize(i)[-1] == fin :
			L += [i]
	return L

def choix_lettre(s,L, mem) :
	Li = []
	for i in range(len(s)) :
		if s[i] == '_' :
			for j in L :
				if j[i] not in mem :
					Li += j[i]
	return Li[randint(0,len(Li) - 1)]

def filtre_lettre(s, L) :
	Li = []
	for i in L :
		if not(s in asciize(i)[1:-1]) :
			Li += [i]
	return Li

def est_compatible(s, m) :
	if len(s) != len(m) : return False
	for i in range(len(s)) :
		if asciize(s)[i] != asciize(m)[i] and asciize(s)[i] != '_' :
			return False
	return True

def jouer() :
	gameOn = True
	
	while gameOn :
		try :
			vies = int(input('Combien de vies voulez vous ? '))	
		except :
			print('Tu sais pas écrire')
			vies = 1
		m = mot_au_hasard()
		L = mot_vers_liste(m)
		mem = []
		print('il te reste {} vie{}'.format(vies,'s' if vies >1 else ''))
		while vies > 0 and '_' in L :
			print(''. join(L))
			print('Lettres déjà demandées :', mem)
			lettre_choisie = input('Choisis une lettre')
			if not(lettre_valide(m,mem,lettre_choisie)) :
				print('lettre refusée')
			else :
				mem += [lettre_choisie]
				if met_a_jour2(L ,m , lettre_choisie ) :
					print('bien joue !')
				else :
					print('rate ... ')
					vies -= 1
					print('il te reste {} vie{}'.format(vies,'s' if vies >1 else ''))
		if vies == 0 :
			print('PENDU ! Le mot secret était {}.'.format(m), end = ' ')
		else :
			print(m)
			print('GAGNÉ !', end = '')
		gameOn = restart()
	

def joue_chercheur(vies) :
	M = input('Quel est ton indice de départ humain ?')
	L = candidats(M[0], M[-1], len(M))
	mem = []
	while vies > 0 and len(L) > 1 :
		print('J\'hésite entre', L)
		lettre = asciize(choix_lettre(M, L, mem))
		mem += [lettre]
		print('Je demande le {} .'.format(lettre), end = ' ')
		m = input('Nouvel indice ? ')
		if not(est_compatible(M, m)) :
			print('Je ne connais pas ce mot')
			vies = 0
			break
		if m == M :
			vies -= 1
			print('Il me reste {} vie{}'.format(vies,'s' if vies > 1 else ''))
			L = filtre_lettre(lettre, L)
		else :
			M = m
			L = [i for i in L if (i not in filtre_lettre(lettre,L) and est_compatible(M, i))]
	if vies == 0 :
		print('J\'ai perdu, tu es trop fort pour moi humain')
	elif len(L) == 0 :
		print('Je ne connais pas ce mot')
	else :
		print('J\'ai trouvé :', L[0])
		vérification = (input('C\'est ça ?').lower() in ['y', 'yes','o','oui'])
		if not(vérification) :
			print('Bah je connais pas ce mot')





