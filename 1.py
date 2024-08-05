import flet as ft

def main(page: ft.Page):
    page.title = 'Mehdi'
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = ft.colors.GREY_900
    page.window.top = 10
    page.window.left = 1150
    page.window.resizable=True
    page.window.title_bar_hidden
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.scroll = "auto"
    page.window_full_screen= True

    page.update()
    
ft.app(main)