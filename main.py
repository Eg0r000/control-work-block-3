import flet as ft
a = open("C:/Users/Unicum_Student/Documents/Папка/save.txt",'+++')
def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value=a.read(), text_align=ft.TextAlign.RIGHT, width=100)

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def zero_click(e):
        txt_number.value = str(int(txt_number.value) * 0)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.EXPOSURE_ZERO, on_click=zero_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)