import time
import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update() #Con page.update() renderizo todos los cambios que he hecho

    t = ft.Text()
    page.add(t) # con page.add() agrego un nuevo control y se renderiza de una vez

    """
     for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)
    """
    
    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
            ]
        )
    )

    page.add(
        ft.Row(
            controls=[
                ft.TextField(label="Your name"),
                ft.ElevatedButton(text="Say my name!")
            ]
        )
    )

    """
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i> 4:
            page.controls.pop(0) #Pop(n) es para eliminar el n-esimo controlador que este en la pagina
        page.update()
        #time.sleep(1)
    """
    page.controls.append(ft.Text("Estefano"))    
    page.add(ft.TextButton("Gay chamo")) #con page.add tambien renderizo los cambios que se allan hecho antes
    
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
    
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()
    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    #new_task.visible = False , propiedad para no hacer visible el control 
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    
    #dispointed
    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
        ])
    c.disabled = True
    page.add(c)

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name" #Este atributo nos permite lanzar un error
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()
    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski" , value=False , on_change= checkbox_changed)
    page.add(todo_check , output_text)

ft.app(target=main)
