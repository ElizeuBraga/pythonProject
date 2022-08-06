from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from models.Db import Db
from models.Helper import Helper
from Pessoa import Pessoa

user = None

class ScreenManager(ScreenManager):
    def transit_screen(self, *args):
        self.manager.current = "register"
        return
    pass

class Login(Screen):

    def passarValorParaLabel(self, *args):
        args_str = ','.join(map(str, args))
        print(args_str)
        home_screem = self.manager.get_screen('home')
        home_screem.ids.user.text = f'Seja bem vindo {args_str}!'
        self.manager.current = 'home'

    def login(self):
        email_or_phone = self.ids.email_or_phone.text
        # pwd = self.ids.pwd.text

        sql = "SELECT * FROM users WHERE email = ? OR phone = ?"
        user_exist = Db.selectOne(None, sql, [email_or_phone, email_or_phone])

        if not user_exist:
            Helper().show_alert_dialog("Email ou senha incorretos")
            return

        print(user_exist)
        self.passarValorParaLabel(user_exist[1])
        # self.manager.current = "home"

        return
    pass
class Register(Screen):
    dialog = None

    def close_alert_dialog(self, *args):
        self.dialog.dismiss(force=True)
        self.dialog = None

    def show_alert_dialog(self, message):
        print(message)
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                        on_release=self.close_alert_dialog
                    )
                ]
            )
        self.dialog.open()

    def save(self):
        name = self.ids.name.text
        email = self.ids.email.text
        phone = self.ids.phone.text
        pwd = self.ids.pwd.text

        sql = "SELECT * FROM users WHERE email = ?"
        user_exist = Db.selectOne(None, sql, [email])

        if len(name) == 0 or len(email) == 0 or len(phone) == 0 or len(pwd) == 0:
            self.show_alert_dialog("Preencha todos os campos.")
            return
        elif len(phone) < 9:
            self.show_alert_dialog("Telefone deve conter 9 dígitos.")
            return
        elif user_exist:
            self.show_alert_dialog("Este usuario já está cadastrado na base de dados")
            return

        #INSERIR USUARIO
        sql = "INSERT INTO users(name, email, phone, password)VALUES(?,?,?,?)"
        Db.insert(None, sql, [name, email, phone, pwd])
        self.show_alert_dialog("Usuário cadastrado com sucesso!")

        self.passarValorParaLabel('Aqui')
    pass

class Home(Screen):

    pass

class LabelMessagem(Screen):

    pass

class Milk(MDApp):
    def build(self):
        return Builder.load_file('menu.kv')

Milk().run();