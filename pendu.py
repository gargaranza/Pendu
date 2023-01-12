from pendu_biblio import *
from tkinter import *
import tkinter.font as tkFont
import time



fenetre = Tk()

vies = 0
m = ''
L = []
mem = []
TEST = False

def createCanvas() :
	global canvas
	
	canvas = Canvas(fenetre, width=1000, height=1000)
	canvas.place(x = 0, y = 0)

def dessin_pendu(n) :
	global canvas
	
	if n == 1 :
		canvas.create_line(100,700,500,700)
	elif n == 2 :
		canvas.create_line(250,700,250,100)
	elif n == 3 :
		canvas.create_line(250,100,600,100)
	elif n == 4 :
		canvas.create_line(350,100,250,200)
	elif n == 5 :
		canvas.create_line(600,100,600,200)
	elif n == 6 :
		canvas.create_oval(550,200,650,300)
	elif n == 7 :
		canvas.create_line(600,300,600,500)
	elif n == 8 :
		canvas.create_line(600,500,550,600)
		canvas.create_line(600,500,650,600)
	elif n == 9 :
		canvas.create_line(525,350,675,350)
	fenetre.update()


def affiche_mot() :
	global L
	global affiche_Lettre
	
	affiche_Lettre.configure(text = ' '.join(L))
	fenetre.update()

def updateLettres() :
	global mem
	for i in range(len(mem)) :
		Buttons[mem[i].upper()].destroy()
		Label(fenetre, text = mem[i].upper(), font = tkFont.Font(family = 'Helvetica', size = 30)).place(x = 1100 + (i * 100)%800, y = 520 + 100 * int(i/8))

def rejouer() :
	for c in fenetre.winfo_children() :
		c.destroy()
	setup()

def recomancer() :
	for c in fenetre.winfo_children() :
		c.destroy()
	Label(fenetre, text = 'Tu veux rejouer ?', font = tkFont.Font(family = 'Helvetica', size = 50)).place(x = 300, y = 100)
	Button(fenetre, text = 'Rejouer', width = 10, height = 4, command=rejouer, font = tkFont.Font(family = 'Helvetica', size = 30)).place(x = 150, y = 500)
	Button(fenetre, text = 'Quitter' ,width = 10, height = 4, command = fenetre.quit, font = tkFont.Font(family = 'Helvetica', size = 30)).place(x = 1300, y = 500)


def perdu() :
	global m
	global L
	
	global TEST
	TEST = True
	
	L = list(m)
	affiche_mot()
	for i in [chr(k) for k in range(ord('A'), ord('Z') + 1)] :
		Buttons[i].destroy()
	
	Label(fenetre, text = 'ABBA Cebette' , font = tkFont.Font(family = 'Helvetica', size = 30)).place(x = 1200, y = 200)
	
	fenetre.update()
	
	time.sleep(5)
	
	recomancer()

def gagné() :
	for i in [chr(k) for k in range(ord('A'), ord('Z') + 1)] :
		Buttons[i].destroy()
	
	Label(fenetre, text = 'Bravo !' , font = tkFont.Font(family = 'Helvetica', size = 30)).place(x = 1300, y = 200)
	
	fenetre.update()
	
	time.sleep(5)
	
	recomancer()


def Lettre(lettre_choisie) :
	global mem
	global vies
	global L
	global m
	global TEST
	
	mem.append(lettre_choisie)
	updateLettres()
	
	L = met_a_jour(L ,m , lettre_choisie)
	if lettre_choisie in m[1:-1] :
		affiche_mot()
		if L == list(m) : gagné()
	else :
		vies = vies - 1
		dessin_pendu(9 - vies)
		if vies == 0 : perdu()



def cliqueA() : Lettre('a')	
def cliqueB() : Lettre('b')
def cliqueC() : Lettre('c')
def cliqueD() : Lettre('d')
def cliqueE() : Lettre('e')
def cliqueF() : Lettre('f')
def cliqueG() : Lettre('g')
def cliqueH() : Lettre('h')
def cliqueI() : Lettre('i')
def cliqueJ() : Lettre('j')
def cliqueK() : Lettre('k')
def cliqueL() : Lettre('l')
def cliqueM() : Lettre('m')
def cliqueN() : Lettre('n')
def cliqueO() : Lettre('o')
def cliqueP() : Lettre('p')
def cliqueQ() : Lettre('q')
def cliqueR() : Lettre('r')
def cliqueS() : Lettre('s')
def cliqueT() : Lettre('t')
def cliqueU() : Lettre('u')
def cliqueV() : Lettre('v')
def cliqueW() : Lettre('w')
def cliqueX() : Lettre('x')
def cliqueY() : Lettre('y')
def cliqueZ() : Lettre('z')


def createButtons() :
	global Buttons
	
	taille = 5
	
	Buttons = {'A' : Button(fenetre, width = taille, height = taille, text='A', command=cliqueA),
	'B' : Button(fenetre, width = taille, height = taille, text='B', command=cliqueB),
	'C' : Button(fenetre, width = taille, height = taille, text='C', command=cliqueC),
	'D' : Button(fenetre, width = taille, height = taille, text='D', command=cliqueD),
	'E' : Button(fenetre, width = taille, height = taille, text='E', command=cliqueE),
	'F' : Button(fenetre, width = taille, height = taille, text='F', command=cliqueF),
	'G' : Button(fenetre, width = taille, height = taille, text='G', command=cliqueG),
	'H' : Button(fenetre, width = taille, height = taille, text='H', command=cliqueH),
	'I' : Button(fenetre, width = taille, height = taille, text='I', command=cliqueI),
	'J' : Button(fenetre, width = taille, height = taille, text='J', command=cliqueJ),
	'K' : Button(fenetre, width = taille, height = taille, text='K', command=cliqueK),
	'L' : Button(fenetre, width = taille, height = taille, text='L', command=cliqueL),
	'M' : Button(fenetre, width = taille, height = taille, text='M', command=cliqueM),
	'N' : Button(fenetre, width = taille, height = taille, text='N', command=cliqueN),
	'O' : Button(fenetre, width = taille, height = taille, text='O', command=cliqueO),
	'P' : Button(fenetre, width = taille, height = taille, text='P', command=cliqueP),
	'Q' : Button(fenetre, width = taille, height = taille, text='Q', command=cliqueQ),
	'R' : Button(fenetre, width = taille, height = taille, text='R', command=cliqueR),
	'S' : Button(fenetre, width = taille, height = taille, text='S', command=cliqueS),
	'T' : Button(fenetre, width = taille, height = taille, text='T', command=cliqueT),
	'U' : Button(fenetre, width = taille, height = taille, text='U', command=cliqueU),
	'V' : Button(fenetre, width = taille, height = taille, text='V', command=cliqueV),
	'W' : Button(fenetre, width = taille, height = taille, text='W', command=cliqueW),
	'X' : Button(fenetre, width = taille, height = taille, text='X', command=cliqueX),
	'Y' : Button(fenetre, width = taille, height = taille, text='Y', command=cliqueY),
	'Z' : Button(fenetre, width = taille, height = taille, text='Z', command=cliqueZ)}
	

def setup() :
	global vies
	global m
	global L
	global L_1
	global mem
	
	createCanvas()
	createButtons()
	
	global Buttons
	
	vies = 9
	m = mot_au_hasard()
	L = mot_vers_liste(m)
	mem = []
	
	global affiche_Lettre
	affiche_Lettre = Label(fenetre, text = ' '. join(L), font = tkFont.Font(family = 'Helvetica', size = 50))
	affiche_Lettre.place(x = 10, y = 820)
	
	Label(fenetre,text = 'Lettres déjà demandées :', font = tkFont.Font(family = 'Helvetica', size = 20)).place(x = 1000, y = 450)
	
	alphabet = [chr(k) for k in range(ord('A'), ord('Z') + 1)]
	
	for i in range(len(alphabet)) :
		Buttons[alphabet[i]].place(x = 1020 + (100 * i)%900, y= 10 + 130 * int(i/9))
	
	fenetre.update()


setup()

fenetre.mainloop()
