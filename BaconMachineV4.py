from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import traceback, sys, random, string
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
#lookup = {'a':'aaaaa', 'b':'aaaab', 'c':'aaaba', 'd':'aaabb', 'e':'aabaa', 'f':'aabab', 'g':'aabba', 'h':'aabbb', 'i':'abaaa', 'j':'abaab', 'k':'ababa', 'l':'ababb', 'm':'abbaa', 'n':'abbab', 'o':'abbba', 'p':'abbbb', 'q':'baaaa', 'r':'baaab', 's':'baaba', 't':'baabb', 'u':'babaa', 'v':'babab', 'w':'babba', 'x':'babbb', 'y':'bbaaa', 'z':'bbaab'} 
lookup = lookup = {'a':'aaaaaa', 'b':'aaaaab', 'c':'aaaaba', 'd':'aaaabb', 'e':'aaabaa', 'f':'aaabab', 'g':'aaabba', 'h':'aaabbb', 'i':'aabaaa', 'j':'aabaab', 'k':'aababa', 'l':'aababb', 'm':'aabbaa', 'n':'aabbab', 'o':'aabbba', 'p':'aabbbb', 'q':'abaaaa', 'r':'abaaab', 's':'abaaba', 't':'abaabb', 'u':'ababaa', 'v':'ababab', 'w':'ababba', 'x':'ababbb', 'y':'abbaaa', 'z':'abbaab', 'A':'baaaaa', 'B':'baaaab', 'C':'baaaba', 'D':'baaabb', 'E':'baabaa', 'F':'baabab', 'G':'baabba', 'H':'baabbb', 'I':'babaaa', 'J':'babaab', 'K':'bababa', 'L':'bababb', 'M':'babbaa', 'N':'babbab', 'O':'babbba', 'P':'babbbb', 'Q':'Bbaaaa', 'R':'bbaaab', 'S':'bbaaba', 'T':'bbaabb', 'U':'bbabaa', 'V':'bbabab', 'W':'bbabba', 'X':'bbabbb', 'Y':'bbbaaa', 'Z':'bbbaab', '.':'abbaba', ',':'abbabb', ':':'abbbaa', '?':'abbbab', '!':'abbbba', ')':'abbbbb', '(':'bbbaba', '[':'bbbabb', ']':'bbbbaa', '{':'bbbbab', '}':'bbbbba', '"':'abbbbb'} 


def binaryToDecimal(binary): 
      
        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return(decimal/2)  

class Okno(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Okno,self).__init__(*args,**kwargs) 
        self.setWindowTitle("Bacon Machine")

        titletext = QLabel()
        titletext.setText("Welcome in Bacon Machine")
        titletext.setAlignment(Qt.AlignCenter)
        titletext.setFont(QFont('Impact',32))
        titletext.setStyleSheet("QLabel { color: black; }")

        self.operationText = QLabel()
        self.operationText.setText("Type in Message and Background Text")
        self.operationText.setAlignment(Qt.AlignCenter)
        self.operationText.setFont(QFont('Impact',20))
        self.operationText.setStyleSheet("QLabel { color: grey; }")

        self.subTitletext = QLabel()
        self.subTitletext.setText("Result")
        self.subTitletext.setAlignment(Qt.AlignCenter)
        self.subTitletext.setFont(QFont('Arial',12))
        self.subTitletext.setStyleSheet("QLabel { color: grey; }")

        self.messageField = QLineEdit()
        self.messageField.setPlaceholderText("Type Message here...")

        self.keyField = QLineEdit()
        self.keyField.setPlaceholderText("Type Background Text here...")

        textFieldsMenu = QHBoxLayout()
        textFieldsMenu.addWidget(self.messageField)
        textFieldsMenu.addWidget(self.keyField)
        textFieldsMenuW = QWidget()
        textFieldsMenuW.setLayout(textFieldsMenu)

        self.messageFileButton = QFileDialog()
        self.keyFileButton = QFileDialog()

        messageFileButton = QPushButton()
        messageFileButton.setText("Set Message from file")
        messageFileButton.clicked.connect(self.messageFileClicked)

        keyFileButton = QPushButton()
        keyFileButton.setText("Set Background Text from file")
        keyFileButton.clicked.connect(self.keyFileClicked)

        buttonsFileLayout = QHBoxLayout()
        buttonsFileLayout.addWidget(messageFileButton)
        buttonsFileLayout.addWidget(keyFileButton)
        buttonsFileLayoutW = QWidget()
        buttonsFileLayoutW.setLayout(buttonsFileLayout)

        self.saveFileButton = QPushButton()
        self.saveFileButton.setText("Save to File")
        self.saveFileButton.clicked.connect(self.saveFileClicked)
        self.saveFileButton.setEnabled(False)

        encryptButtonG = QPushButton()
        encryptButtonG.setText("Encrypt")
        encryptButtonG.clicked.connect(self.encryptClickedG)

        decryptButtonG = QPushButton()
        decryptButtonG.setText("Decrypt")
        decryptButtonG.clicked.connect(self.decryptClickedG)

        self.generateButton = QPushButton()
        self.generateButton.setText("Generate random Background Text")
        self.generateButton.clicked.connect(self.generateClicked)

        self.helpButton = QPushButton()
        self.helpButton.setText("Help")
        self.helpButton.clicked.connect(self.helpClicked)

        buttonsLayoutG = QHBoxLayout()
        buttonsLayoutG.addWidget(encryptButtonG)
        buttonsLayoutG.addWidget(decryptButtonG)
        buttonsLayoutGW = QWidget()
        buttonsLayoutGW.setLayout(buttonsLayoutG)

        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(titletext)
        mainMenu.addWidget(self.operationText)
        mainMenu.addWidget(self.subTitletext)
        mainMenu.addWidget(textFieldsMenuW)
        mainMenu.addWidget(buttonsLayoutGW)
        mainMenu.addWidget(buttonsFileLayoutW)
        mainMenu.addWidget(self.saveFileButton)
        mainMenu.addWidget(self.generateButton)
        mainMenu.addWidget(self.helpButton)
        

        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)
  
    def encryptG(self): 
        #message = self.messageField.text().lower()
        message = self.messageField.text()
        key = self.keyField.text().replace(' ','')
        cipher = '' 
        for letter in message: 
            try:
                if(letter != ' '): 
                    print(letter + " " + lookup[letter])
                    cipher += lookup[letter] 
                else: 
                    cipher += ' '
            except:
                print(letter)
        pos = 0
        helper = ""
        while pos < len(cipher):
            try:
                if cipher[pos] == ' ':
                    helper += ' '
                elif cipher[pos] == 'a':
                    helper += key[pos]
                elif cipher[pos] == 'b':
                    helper += key[pos].upper()
            except:
                print(cipher[pos])
            pos += 1
        return helper
    
    def decryptG(self): 
        message = self.keyField.text()
        decipher = '' 
        i = 0
        print(message)

        while True : 
            if(i < len(message)-5): 
                substr = message[i:i + 6] 
                helper = ''
                if(substr[0] != ' '): 
                    for k in substr:
                        try:
                            if k.isupper():
                                helper += 'b'
                            else:
                                helper += 'a'
                        except:
                            print(k)
                    substr = ''.join(list(helper))
                    decipher += list(lookup.keys())[list(lookup.values()).index(substr)] 
                    i += 6
                else: 
                    decipher += ' '
                    i += 1 
            else: 
                break 
    
        return decipher 

    def encryptClickedG(self):
        #self.subTitletext.setText("Encrypting: " + self.messageField.text() + " Result: " + self.encrypt())
        self.operationText.setText("Encrypting Message with Key")
        #self.subTitletext.setText(self.encrypt())
        self.subTitletext.setText(self.encryptG())
        self.saveFileButton.setEnabled(True)

    def decryptClickedG(self): 
        #self.subTitletext.setText("Decrypting: " + self.keyField.text() + " Result: " + self.decrypt())
        self.operationText.setText("Decrypting Key")
        #self.subTitletext.setText(self.decrypt())
        self.subTitletext.setText(self.decryptG())
        self.saveFileButton.setEnabled(True)

    def messageFileClicked(self):
        self.keyFileButton.hide()
        self.messageFileButton.show()
        if self.messageFileButton.exec():
            files = self.messageFileButton.selectedFiles()
            f = open(files[0], 'r')
            with f:
                data = f.read()
                self.messageField.setText(data)
        pass

    def keyFileClicked(self):
        self.messageFileButton.hide()
        self.keyFileButton.show()
        if self.keyFileButton.exec():
            files = self.keyFileButton.selectedFiles()
            f = open(files[0], 'r')
            with f:
                data = f.read()
                self.keyField.setText(data)
        pass


    def infoClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Help")
        info.setStyleSheet("QMessageBox {background-color : #89EAEE}")
        f = open("info.txt", "r")
        data = f.read()
        f.close()
        info.setText(data)
        info.setFont(QFont('Arial', 8))
        info.setStyleSheet("QLabel{min-width: 1600px;}")
        info.exec_()

    
    def generateClicked(self):
        spaces = self.messageField.text().count(' ')
        i = len(self.messageField.text().replace(' ',''))
        self.keyField.setText('')
        j = 0
        while i > 0:
            while j < 6:
                self.keyField.setText(self.keyField.text() + random.choice(string.ascii_letters))
                j += 1
            j = 0
            i -= 1
        while spaces > 0:
            self.keyField.setText(self.keyField.text() + random.choice(string.ascii_letters))
            spaces -= 1
    
    def helpClicked(self):
        self.infoClicked()
        self.helpButton.setEnabled(True)
        pass

    def saveFileClicked(self):
        fileName = QFileDialog.getSaveFileName(self,self.tr("Choose file"),"", self.tr("(*.txt)"))[0]
        f = open(fileName, 'w')
        message = self.subTitletext.text()
        f.write(message)
        f.close()
        pass


app = QApplication(sys.argv)

window = Okno()
#window.setFixedSize(800,600)
window.setStyleSheet("background-color: rgb(245,245,220);")
window.show()

app.exec_()