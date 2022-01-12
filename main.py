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

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        app.username = loginText
        app.password = passwordText
        names = {"user": "12345"}

        if app.username in names.keys() and app.password == names[app.username]:
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = 'times'
        else:
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = 'error'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


class LoginApp(MDApp):
    username = StringProperty(None)
    password = StringProperty(None)
    dialog=None

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

    def end_button_press(self):

        screenList=['demographic','measures1','measures2','medicalHistory']
        f=open("summaryReport.txt","w")

        for id in self.root.get_screen('times').ids:
            if 'Label' not in id:
                field = self.root.get_screen('times').ids[id+"Label"].text[::-1]
                print(field)
                value = self.root.get_screen('times').ids[id].text
                if value != "":
                    f.write(field + ":" + value + "\n")
                else:
                    self.show_alert_dialog()
                    return

        for screen in screenList:
            for id in self.root.get_screen(screen).ids:
                field=self.root.get_screen(screen).ids[id].hint_text[::-1]
                value=self.root.get_screen(screen).ids[id].text[::-1]
                if value!="" or screen=='birth' or screen=='medicalHistory':
                    if value.isdigit():
                        value=value[::-1]
                    f.write(field+":"+value+"\n")
                else:
                    self.show_alert_dialog()
                    return

        f.close()
        send_mail()
        self.reset_all()
        return

    def reset_all(self):
        screenList = ['demographic', 'measures1', 'measures2', 'medicalHistory','birth']

        for id in self.root.get_screen('times').ids:
            if 'Label' not in id:
                self.root.get_screen('times').ids[id].text="העש דעת"

        for screen in screenList:
            for id in self.root.get_screen(screen).ids:
                self.root.get_screen(screen).ids[id].text=""


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



if __name__ == '__main__':
    LoginApp().run()