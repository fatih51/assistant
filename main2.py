import locale
import main
from PyQt5 import QtCore
from PyQt5.QtWidgets import*
from ui_main import Ui_MainWindow #burada 'notlar' kısmı ui dosyasının py olmuş hali olacak
import datetime
import webbrowser
import random
from playsound import playsound
from gtts import gTTS
import os 


def say(string):
    try:
        tts = gTTS(string,lang='tr')
        rand = random.randint(1,100000)
        file = "ses-"+str(rand)+".mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)
    except ValueError:
        pass




class a(QMainWindow,Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setupUi(self)
              
        say("Ne Yapmak İstersiniz")
        
        self.label_1.setText("Ne Yapmak İstersiniz")
        self.label_2.setText("Fonksiyonlar \n(Arama,Müzik,Saat,Lig,Hava,Kapat,\nTakvim,Çeviri,Hesap Makinesi,Youtube,Wikipedia)")
        

        self.lineEdit_1.textEdited.connect(self.fonksiyon)
        self.lineEdit_1.setText("")
        self.lineEdit_2.hide()
        
    def arama_fonksiyonu(self):
        if self.text =="arama":
            self.text2 = self.lineEdit_2.text().lower()
            url = "https://www.google.com/search?q=" + self.text2
            webbrowser.get().open(url)
            say(self.text2 +"için bulduklarım")
        

    def music_fonksiyonu(self):
        if self.text =="müzik":
            self.text2 = self.lineEdit_2.text().lower()
            if self.text2 =="spotify":
                say("Spotify Açılıyor")
                webbrowser.open("https://www.spotify.com/tr")
            elif self.text2 =="youtube müzik":
                say("Youtube Müzik Açılıyor")
                webbrowser.open("https://music.youtube.com")

    def hava_fonksiyonu(self):
        if self.text =="hava":
            self.text2 = self.lineEdit_2.text().lower()
            url_a = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=" + self.text2
            webbrowser.get().open(url_a)
            say(self.text2 +"hava durumu")
        

    def youtube_fonksiyonu(self):
        if self.text=="youtube":
            self.text2 = self.lineEdit_2.text().lower()
            url_4 = "https://www.youtube.com/results?search_query=" + self.text2
            webbrowser.get().open(url_4)
            say(self.text2 +"için bulduklarım")
        

    def wikipedia_fonksiyonu(self):
        if self.text=="wikipedia":
            self.text2 = self.lineEdit_2.text().lower()
            url_1 = "https://tr.wikipedia.org/w/index.php?search={}&title=%C3%96zel%3AAra&go=Git".format(self.text2)
            webbrowser.get().open(url_1)
            say(self.text2 +"için bulduklarım")

    def fonksiyon(self):
        self.text = self.lineEdit_1.text().lower()
        
        if self.text =="arama":
            say("Ne Aramak İstersin")
            self.label_1.setText("Ne Aramak İstersin")
            self.lineEdit_2.show()
            self.lineEdit_2.editingFinished.connect(self.arama_fonksiyonu)

        elif self.text =="müzik":
            say("Spotify mı Youtube Müzik mi")
            self.lineEdit_2.show()
            self.label_1.setText("Spotify mı Youtube Müzik mi")
            self.lineEdit_2.editingFinished.connect(self.music_fonksiyonu)
    

        elif self.text =="saat":
            self.lineEdit_2.hide()
            locale.setlocale(locale.LC_ALL, '')
            an = datetime.datetime.now()
            tarih = datetime.datetime.strftime(an, '%c')
            self.label_1.setText(tarih)
            say(tarih)

        elif self.text =="lig":
            say("Fikstür Açılıyor")
            self.lineEdit_2.hide()
            webbrowser.open("https://www.tff.org/default.aspx?pageID=198")

        elif self.text =="hava":
            say("Hangi İlde Bulunmaktasınız")
            self.label_1.setText("Hangi İlde Bulunmaktasınız")
            self.lineEdit_2.show()
            self.lineEdit_2.editingFinished.connect(self.hava_fonksiyonu)

        elif self.text=="kapat":
            say("Görüşmek Üzere")
            self.lineEdit_2.hide()
            quit()

        elif self.text=="takvim":
            say("Takvim Açılıyor")
            self.lineEdit_2.hide()
            webbrowser.open("http://takvim.ufgu.com/")

        elif self.text=="çeviri":
            say("Translate Açılıyor")
            self.lineEdit_2.hide()
            webbrowser.open("https://translate.google.com")

        elif self.text=="hesap makinesi":
            say("Hesap Makinesi Açılıyor")
            self.lineEdit_2.hide()
            webbrowser.open("https://www.google.com/search?q=hesap+makinesi&oq=hesap+makinesi&aqs=chrome..69i57j35i39j0j0i433j0l3j5.2488j0j7&sourceid=chrome&ie=UTF-8")

        elif self.text=="youtube":
            say("Ne Aramak İstersin")
            self.label_1.setText("Ne Arayacaksınız")
            self.lineEdit_2.show()
            self.lineEdit_2.editingFinished.connect(self.youtube_fonksiyonu)
            

        elif self.text=="wikipedia":
            say("Ne Aramak İstersin")
            self.label_1.setText("Ne Arayacaksınız")
            self.lineEdit_2.show()
            self.lineEdit_2.editingFinished.connect(self.wikipedia_fonksiyonu)


        else:
            self.lineEdit_2.hide()
            self.label_1.setText("Yanlış Değer Girdiniz..")
      
        
        

uygulama = QApplication([])
pencere = a()
pencere.show()
uygulama.exec_()
