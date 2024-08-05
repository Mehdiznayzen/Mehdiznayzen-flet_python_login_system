from flet import *

def main(page: Page):
    # ##### Window Properties #####
    page.title = "Login System"
    
    page.window.height = 740
    page.window.width = 390 
    
    page.window.top = 10 
    page.window.left = 1100 
    
    page.vertical_alignment = "center"  # Top, Bottom
    page.horizontal_alignment = "center"  # Left, Right
    
    # ##### AppBar #####
    page.appbar = AppBar(
        bgcolor=colors.RED,
        color=colors.WHITE,
        leading=Icon(icons.HOME),
        leading_width=50,
        title=Text('Mehdi Znayzen'),
        center_title=True,
        actions=[
            IconButton(icons.NOTIFICATIONS),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="Profile personally"),
                    PopupMenuItem(text="Parameters"),
                    PopupMenuItem(text="Privacy Policy"),
                    PopupMenuItem(text="About the application"),
                    PopupMenuItem(text="Who us ?"),
                    PopupMenuItem(),
                    PopupMenuItem(text="Close"),
                ],
                bgcolor="black",
            ),
        ]
    )
    
    # ##### The Content #####
    # Add the image
    image = Image(
        src="login-img.png",
        width=160,
        height=160,
    )
    
    # Add Text Description
    text = Text(
        "Login System",
        size=20,
        weight=FontWeight.W_600,
        font_family="Roboto_slab",
    )
    
    # Add Inputs fields
    input_email = TextField(
        label="Email",
        icon=icons.EMAIL,
    )
    input_password = TextField(
        label="Password",
        password=True,
        icon=icons.PASSWORD,
        can_reveal_password=True,
    )
    
    # The validation of Data
    def submit_data(e):
        if input_email.value == "admin@gmail.com" and input_password.value == "admin":
            validModal = AlertDialog(
                modal=True,
                title=Text("Valid Credentials", color=colors.GREEN),
                content=Text("You have successfully logged in!"),
            )
            page.overlay.append(validModal)
            validModal.open = True
            page.update()
        else:
            ErrorModal = AlertDialog(
                modal=True,
                title=Text("Error Login", color=colors.RED),
                content=Text("Please try again email or password invalid !!"),
            )
            page.overlay.append(ErrorModal)
            ErrorModal.open = True
            page.update()
            
    
    # Add The Submit Button
    submit_btn = ElevatedButton(
        text="Login",
        color=colors.WHITE,
        bgcolor=colors.RED,
        width=200,
        on_click=submit_data
    )
    
    page.add(image, text, input_email, input_password, submit_btn)
    
    # ##### Footer #####
    page.navigation_bar = CupertinoNavigationBar(
        bgcolor=colors.RED,
        inactive_color=colors.BLACK,
        destinations=[
            NavigationBarDestination(icon=icons.CALL, label="Call", tooltip="Mehdi"),
            NavigationBarDestination(icon=icons.CAMERA, label="Camera"),
            NavigationBarDestination(icon=icons.CONTACT_PHONE, label="Contact"),
        ]
    )

    page.update()

app(target=main)
