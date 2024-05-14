import flet as ft
class MyButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.colors.DEEP_PURPLE_ACCENT_700 # Color del fondo del boton
        self.color = ft.colors.WHITE #Color de la letra
        self.text = text

def main(page: ft.Page):

    page.add(MyButton(text="OK"), MyButton(text="Cancel"))

ft.app(target=main)

#Si quiere que un controlador customizado realice un evento, tengo que ponerlo de parametro en la clase customizada
class MyButton(ft.ElevatedButton):
    def __init__(self , text , on_click):
        super().__init__()
        self.bgcolor = ft.colors.TEAL_400
        self.color = ft.colors.BLACK
        self.text  = text
        self.on_click = on_click
def main(page: ft.Page):

    def ok_clicked(e):
        print("OK clicked")
    
    def cancel_clicked(e):
        print("Cancel clicked")

    page.add(
        MyButton(text="OK", on_click=ok_clicked),
        MyButton(text="Cancel", on_click=cancel_clicked),
    )
ft.app(main)

class Task(ft.Row):
    def __init__(self , text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text , visible=True)
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT , on_click=self.evento2)
        self.save_button = ft.IconButton(
            visible=True , icon=ft.icons.SAVE , on_click=self.evento
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]
    def evento(self , e):
        self.text_edit.visible = False
        self.update()
    def evento2(self, e):
        self.controls.append(ft.TextField("Multi destino, saliendo Ujaaap!!"))
        self.update()

def main(page: ft.Page):
    page.add(
        Task(text="Do Laundry")
    )
ft.app(main)


#Los elementos con visible = False, no ocupan hitbox
class Task(ft.Row):
    def __init__(self , text):
        super().__init__()
        self.isolated = True # aislamos la renderavilisidad de este elemento con los demas
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text , visible=False)
        self.edit_button = ft.IconButton(visible= True , icon=ft.icons.EDIT , on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False , icon=ft.icons.SAVE , on_click=self.save
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]
    def edit(self , e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()
    
    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

def main(page: ft.Page):
    page.add(
        Task(text="Do Laundry"),
        Task(text= "Multidestino, saliendo Ujaap!")
    )
ft.app(main)

