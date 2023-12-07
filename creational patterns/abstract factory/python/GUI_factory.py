from abc import ABC

class Button(ABC):
    def paint(self):
        pass


class CheckBox(ABC):
    def paint(self):
        pass


class Mac_Button(Button):
    def paint(self):
        print("The button is rendered in a MacOS style.")


class Mac_CheckBox(CheckBox):
    def paint(self):
        print("The checkbox is rendered in a MacOS style.")


class Windows_Button(Button):
    def paint(self):
        print("The button is rendered in a Windows style.")


class Windows_CheckBox(CheckBox):
    def paint(self):
        print("The checkbox is rendered in a Windows style.")


class GUI_Factory(ABC):
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> CheckBox:
        pass


class MacOS_Factory(GUI_Factory):
    def create_button(self) -> Button:
        return Mac_Button()
    
    def create_checkbox(self) -> CheckBox:
        return Mac_CheckBox()
    

class Windows_Factory(GUI_Factory):
    def create_button(self) -> Button:
        return Windows_Button()
    
    def create_checkbox(self) -> CheckBox:
        return Windows_CheckBox()
    

class Brand_Manufacturer(ABC):
    button: Button = None
    checkbox: CheckBox = None

    def __init__(self, factory: GUI_Factory) -> None:
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

if __name__ == "__main__":
    mac_manufacturer = MacOS_Factory()
    win_manufacturer = Windows_Factory()

    mac_manufacturer = Brand_Manufacturer(mac_manufacturer)
    win_manufacturer = Brand_Manufacturer(win_manufacturer)

    mac_manufacturer.paint()
    win_manufacturer.paint()