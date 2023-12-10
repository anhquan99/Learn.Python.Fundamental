from UI.BaseUI import BaseUI

class HistoryUI(BaseUI):
    def input_history_info(self):
        global cars
        car_id = self.input_car_id()
        history = History(cars)
        file = history.export_history_of_car(car_id)
        print(f"History exported to {file}.")