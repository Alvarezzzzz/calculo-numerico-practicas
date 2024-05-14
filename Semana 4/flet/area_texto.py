import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
ft.app(main)