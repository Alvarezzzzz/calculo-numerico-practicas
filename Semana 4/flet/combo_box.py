import flet as ft 
def main(page: ft.Page):
    def button_clicked(e):
        if not color_dropdown.value:
            color_dropdown.error_text = "Che flaco, seleccioname algo viste"
        else:
            output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit" , on_click= button_clicked )
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
        value= "Red"
    )
    page.add(color_dropdown , submit_btn , output_text)
ft.app(target=main)