import flet as ft

def main(page: ft.Page):
    my_dict = {}

    def btn_click(e):
        if not sstid.value:
            sstid.error_text = "err"
            page.update()
        else:
            my_dict["sstid"] = sstid.value
            sstid.set_value("")  # clear the value of sstid
            page.update()

    sstid = ft.TextField(label="SSTID", name="sstid")

    page.add(
        ft.Container(
            height=250,
            bgcolor="white10",
            border=border.all(1,"#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    sstid,
                    ft.ElevatedButton("Add", on_click=btn_click),
                ],
            ),
        )
    )
ft.app(target=main)