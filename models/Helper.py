from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

class Helper():
    dialog = None
    def close_alert_dialog(self, *args):
        print("Fecho modal")
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
    pass