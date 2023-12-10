from UI.ParkUI import ParkUI
from UI.PickupUI import PickupUI
from UI.HistoryUI import HistoryUI
class MainUI:
    def action():
        def select_menu():
            print("1. Park car")
            print("2. Pickup car")
            print("3. View parking history")
            print("4. Exit")
        def input_menu():
            while True:
                try:
                    menu = int(input("Choose menu: "))
                    if menu < 1 or menu > 4:
                        raise InputException("menu")
                    return menu
                except InputException as ex:
                    print(ex.message)
        while True:
            select_menu()
            menu = input_menu()
            if menu == 1:
                ui = ParkUI()
                ui.input_park_info()
            elif menu == 2:
                ui = PickupUI()
                input_pickup_info()
            elif menu == 3:
                ui = HistoryUI()
                ui.input_history_info()
            elif menu == 4:
                exit()