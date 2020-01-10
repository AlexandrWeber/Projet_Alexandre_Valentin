import foncStats
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

app = QApplication([])
app.setStyle('Windows') # le style de l'application est proche de celui de windows

# définition de la classe Window qui hérite de la classe QMainWindow de Qt
class Window (QMainWindow):
	def __init__(self):
		super().__init__()
		self.UI()
	
	 

	def UI(self):
		"""Définit les composants graphiques de l'application.
			Il y a dix composants graphiques de l'application avec leur géométrie et fonction comportement
		"""
		
		#Window title TextEdit and their geometry
		self.setWindowTitle('Sympa')
		self.setGeometry(500, 300, 800, 400)
		self.textEdit=QTextEdit(self)
		self.textEdit.setGeometry(20, 140, 760, 200)
		
		#Push button "Appliquer"
		button=QPushButton('Appliquer', self)
		button.setGeometry(40, 350, 70, 20)
		button.clicked.connect(self.on_button_clicked)
		
		#Menubar Files: Open and Save
		openFile = QAction(QIcon('open.png'), 'Open', self)
		saveFile=QAction(QIcon('save.png'), 'Save', self) 
		
		saveFile.setStatusTip( "Save File" ) 
		openFile.setShortcut('Ctrl+O')
		saveFile.setShortcut('Ctrl+S')
		openFile.setStatusTip('Open new File')
		
		openFile.triggered.connect(self.showDialog)
		saveFile.triggered.connect(self.SaveFF) 
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)  
		fileMenu.addAction(saveFile) 
		
		#Label "Choisissez les stats
		self.linel=QLabel(self)
		self.linel.setGeometry(80, 25, 120, 30)
		self.linel.setText("Choisissez les stats")
		
		#Label "Choisissez les traitements
		self.lineT=QLabel(self)
		self.lineT.setGeometry(260, 25, 180, 30)
		self.lineT.setText("Choisissez les traitements")
		
		#Label Ecrivez le mot recherché
		self.lineT=QLabel(self)
		self.lineT.setGeometry(40, 70, 280, 20)
		self.lineT.setText("Ecrivez votre mot")
		
		#Combobox qui permet de choisir les stats (8 stats) cb
		self.cb = QComboBox(self)
		self.cb.setGeometry(40, 50, 200, 20)
		self.cb.addItem("    ")
		self.cb.addItem("fréquence d'un mot particulier")
		self.cb.addItems(["fréquence pattern", "index richesse vocabulaire", "nombre de caractères", "nombre de mots", "compter phrases", "longueur moyenne phrase"])
		self.cb.activated[str].connect(self.selectionchange)
		
		#Combobox qui permet de choisir les traitements à apliquer sur le texte (2 traitements) cbf
		self.cbf = QComboBox(self)
		self.cbf.setGeometry(250, 45, 180, 30)
		self.cbf.addItem("    ")
		self.cbf.addItems(["enlever les espaces en plus", "tagger"])
		self.cbf.activated[str].connect(self.selectionchangef)
	
		# Push button qui supprime le texte		
		buttonsup=QPushButton('Supprimer', self)
		buttonsup.setGeometry(120, 350, 70, 20)
		buttonsup.clicked.connect(self.on_button_clickedSUP)
		
		#Line qui permet l'entrer des mots ou patterns recherchés. Son contenu apparaîtra dans la variable linetexte dans la fonction on_button_clicked
		self.line=QLineEdit(self)
		self.line.setGeometry(40, 90, 200, 20)
		self.line.show()
		
		self.show()
# Fin définition des composants graphiques
	
	
	
	
	
# Ces fonctions définissent les comportements des composants graphiques	
	def showDialog(self):
		"""
			Ouvre le fichier et place le contenu textuel dans l'editeur texte
			Seuls les fichiers txt peuvent être ouverts
		"""

		fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

		if fname[0]:
			f = open(fname[0], 'r')

			with f:
				data = f.read()
				self.textEdit.setText(data)  
			
			
			
				
	def SaveFF(self):
		"""
			Sauvegarde les textes qui se trouvent dans l'éditeur
			La sauvegarde est seulement possible en txt
			
		"""
		
		S__File = QFileDialog.getSaveFileName(self,'SaveTextFile','/home', "Text Files (*.txt)")
		Text = self.textEdit.toPlainText()
		if S__File[0]: 
       
			with open(S__File[0], 'w') as file:
				file.write(Text)
					
	
	
	
	def selectionchange(self,text):
		"""
			Sauvegarde la valeur courante de Combobox, qui fait les stats(cb), dans la variable crt
		"""
		
		self.crt=self.cb.currentText()
		return self.crt
		
	
	
	
	def selectionchangef(self):
		"""
			Sauvegarde la valeur courante de Combobox, qui fait les traitements(cbf), dans la variable crtf
		"""
		
		self.crtf=self.cbf.currentText()
		return self.crtf
		
		
		
		
	def on_button_clickedSUP(self):
		"""
			Enlève le texte de l'éditeur si le bouton Supprimer est cliqué
		"""
		
		self.textEdit.clear()
		
		
	
	
	def on_button_clicked(self):
		"""
			IMPORTANT! Permet d'effectuer les traitements et les stats sur le texte une fois le bouton "Appliquer" est cliqué
			Se compose des applications des fonctions stats et traitements qui se trouvent dans le module "foncStats"
			A chaque traitement s'ouvre un box pour afficher le résultat, MessageBox
			Variable "linetext" représente le texte de la ligne d'entrée des mots à chercher
			Variable "tex" représente le texte de l'éditeur sur lequel s'effectue le traitement
			Variable "crt" représente le stat choisi pour appliquer au texte(tex)
			Variable "crtf" représente le traitement pour faire sur le texte (tex)
		"""
		
		alert = QMessageBox()
		linetext=self.line.text() # récupère le texte courant de la line d'entrée des mots (Line)
		tex=self.textEdit.toPlainText() # récupère le texte de l'éditeur, le transforme en texte plein et le met dans la variable tex
		self.crt=self.cb.currentText() # récupère le contenu textuel de combobox pour les stats (cb) et le met dans la variable crt
		self.crtf=self.cbf.currentText() # récupère le contenu textuel de combobox pour les traitements (cbf) et le met dans la variable crtf



#nombre de mots		
		if self.crt=="nombre de mots":
			stats = foncStats.nommot(tex)
			alert.setText("Votre texte contient {} mots".format(stats))

#nombre de lettres		
		if self.crt=="nombre de caractères":
			stats=foncStats.nomlet(tex)
			alert.setText("Votre texte contient {} lettres".format(stats))

# fréquence d'un mot particulier
		if self.crt=="fréquence d'un mot particulier":
			stats=foncStats.freqmot(linetext, tex)
			alert.setText("Le mot {} se rencontre {} fois dans le texte".format(linetext, stats))

# compter les phrases			
		if self.crt=="compter phrases":
			stats=foncStats.freqphrase(tex)
			alert.setText("Dans le texte il y a {} phrases".format(stats))

# compter la longueur moyenne de la phrase			
		if self.crt=="longueur moyenne phrase":
			stats=foncStats.lonphrase(tex)
			alert.setText("Longueur moyen de la phrase est {} mots".format(stats))
	

# enlever les espaces crtf
		if self.crtf=="enlever les espaces en plus":
			stats=foncStats.SupprEsp(tex)
			print(stats)
			self.textEdit.setPlainText(stats)
			alert.setText("{}".format(stats))
	
# tokenize crtf
		if self.crtf=="tagger":
			stats=foncStats.tok(tex)
			print(stats)
			self.textEdit.setPlainText(stats)
			alert.setText("{}".format(stats))
			
			
# richesse vocabulaire		
		if self.crt=="index richesse vocabulaire":
			stats=foncStats.tok_nltk(tex)
			print(stats)
			alert.setText("L'index richesse vocabulaire est {}".format(stats))
			
#frequence d'un pattern
		if self.crt=="fréquence pattern":
			stats=foncStats.freqpattern(linetext,tex)
			print(stats)
			alert.setText("Le pattern se rencontre {} fois".format(stats))
			
		alert.exec_() # affiche la fenêtre de résultat
		
# Fin définition de la classe main window et fin définition des comportements


# Inistanciation de la classe et l'éxecution
window=Window()

app.exec_()




		
	
		
		
