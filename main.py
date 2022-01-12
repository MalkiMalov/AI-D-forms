from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp

import os
from details1 import *
from send_email import send_mail
import smtplib
from email.message import EmailMessage

Window.size = (400, 500)

#The login screen department that includes functions related to logging in to the system
class Login(Screen):
    #The login function - receives a username and password from the Gui
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        app.username = loginText #insert the user name text into the appropriate variable
        app.password = passwordText #insert the password text into the appropriate variable
        names = {"user": "12345"}

        if app.username in names.keys() and app.password == names[app.username]: #Check whether the username and password entered in the system are correct and authorized to enter
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = 'times'
        else: #issues an error message that it is not possible to log in because a username or password is incorrect / unauthorized
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = 'error'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self): #rester function to the  user name and password fields
        self.ids['login'].text = ""
        self.ids['password'].text = ""

#Program Login Department
class LoginApp(MDApp):
    username = StringProperty(None)
    password = StringProperty(None)
    dialog=None
    
    #function Build program windows so we can access them from the main window and grab the desired window each time
    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Error(name='error'))
        manager.add_widget(times(name='times'))
        manager.add_widget(demographic(name='demographic'))
        manager.add_widget(menu(name='menu'))
        manager.add_widget(measures1(name='measures1'))
        manager.add_widget(measures2(name='measures2'))
        manager.add_widget(medicalHistory(name='medicalHistory'))
        manager.add_widget(birth(name='birth'))
        return manager

    def get_application_config(self):
        if not self.username:
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if not os.path.exists(conf_directory):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config('%s/config.cfg' % conf_directory)
    
    #function responsible for ending the program and doing things in parallel with the end of the run
    def end_button_press(self):

        screenList=['demographic','measures1','measures2','medicalHistory']
        f=open("summaryReport.txt","w") #file to fill in the details from the fields and transfer them to a file to send

        for id in self.root.get_screen('times').ids: #loop that passes through the fields of times
            if 'Label' not in id:
                field = self.root.get_screen('times').ids[id+"Label"].text[::-1]
                print(field)
                value = self.root.get_screen('times').ids[id].text
                if value != "": #check if all the fields of the times are full
                    f.write(field + ":" + value + "\n")
                else: #issues an error message that it is necessary to fill in the blanks
                    self.show_alert_dialog()
                    return

        for screen in screenList: #loop that goes over the fields and outputs the field values to transfer the details to the file to be sent
            for id in self.root.get_screen(screen).ids:
                field=self.root.get_screen(screen).ids[id].hint_text[::-1] #turns the text because it's in Hebrew
                value=self.root.get_screen(screen).ids[id].text[::-1]
                if value!="" or screen=='birth' or screen=='medicalHistory': #check if the fields are not rake and gives the possibility to continue the program even if it is spoken on the Lida screen or medical history because it is not mandatory to fill
                    if value.isdigit(): #turns the text if it is a digit 
                        value=value[::-1]
                    f.write(field+":"+value+"\n")
                else: #issues an error message that the fields are required to be filled in
                    self.show_alert_dialog()
                    return

        f.close()
        send_mail() #send the form by email
        self.reset_all()
        return
    
    #function that initializes the fields so that they can use another event without exiting the program
    def reset_all(self): 
        screenList = ['demographic', 'measures1', 'measures2', 'medicalHistory','birth']

        for id in self.root.get_screen('times').ids:
            if 'Label' not in id:
                self.root.get_screen('times').ids[id].text="העש דעת"

        for screen in screenList:
            for id in self.root.get_screen(screen).ids:
                self.root.get_screen(screen).ids[id].text=""

    #alert Windows function
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title= "Error",
                text= "You have missing fields",

            buttons=[
                    MDRectangleFlatButton(
                        text="OK",
                        text_color = (0.7764705882, 0, 0, 1),
                        line_color= (0.7764705882, 0, 0, 1),
                        on_release= self.close_dialog
                        )
                    ]
            )

        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()


#start the program run
if __name__ == '__main__':
    LoginApp().run()
