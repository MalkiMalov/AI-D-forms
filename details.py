from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.dialog import MDDialog
import words
import time

class Error(Screen):
    def reconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

class times(Screen):
    def times_button_press(self,id):
          t = time.time()
          self.ids[id].text= time.strftime('%H:%M', time.localtime(t))
          self.ids[id].text_color=(0.7764705882, 0, 0, 1)

class demographic(Screen):
    def fill_box(self):
        fields = {"שם פרטי","שם משפחה","גיל","תז","תעודת זהות","מגדר","מין"}
        fields_dict = {"שם פרטי": 'FirstName', "שם משפחה": 'LastName', "גיל": 'Age', "תז": 'ID', "תעודת זהות": 'ID',"מגדר": "Gender", "מין": 'Gender'}
        words.fill_box(self,fields,fields_dict)

class menu(Screen):
    pass

class measures1(Screen):
    def fill_box(self):
        fields = {"דופק", "לחץ דם", "הכרה", "ידיים", "חיוך"}
        fields_dict = {"דופק": 'BPM', "לחץ דם": 'BP', "הכרה": 'Alert', "ידיים": 'Hands', "חיוך": 'Smile'}
        words.fill_box(self,fields,fields_dict)

class measures2(Screen):
    def fill_box(self):
        fields = {"אישונים", "דיבור", "נשימה", "קצב נשימה", "סטורציה"}
        fields_dict = {"אישונים": 'Pupils', "דיבור": 'Speech', "נשימה": 'Breathing', "קצב נשימה": 'RespiratoryRate', "סטורציה": 'OS%'}
        words.fill_box(self,fields,fields_dict)

class medicalHistory(Screen):
    def fill_box(self):
        fields = {"מחלות רקע", "מחלות זיהומיות", "רגישויות", "טיפול תרופתי"}
        fields_dict = {"מחלות רקע": 'BackgroundDiseases', "מחלות זיהומיות": 'InfectiousDiseases', "רגישויות": 'Allergies', "טיפול תרופתי": 'Medications'}
        words.fill_box(self,fields,fields_dict)


class birth(Screen):
    def fill_box(self):
        fields = {"ילודים", "מצג", "שליה", "מצב בהגעה", "שבוע הריון", "מספר הריון", "מספר לידה"}
        fields_dict = {"ילודים": 'Newborn', "מצג": 'Presentation', "שליה": 'Placenta', "מצב בהגעה": 'StatusUponArrival', "שבוע הריון": 'PregnancyWeek',"מספר הריון": "PregnancyNumber", "מספר לידה": 'BirthNumber'}
        words.fill_box(self,fields,fields_dict)
