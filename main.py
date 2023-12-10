# import datetime as dt
from Utils.ImportCsv import ImportParkingPriceList
from Utils import FileHelper
# from Business import Park, Pickup, History
# from Data import Car, ParkingTicket
from UI.MainUI import MainUI
def initialize():
    global price_list
    global cars 
    cars = FileHelper.read_from_file()
    importer = ImportParkingPriceList()
    price_list = importer.import_parking_price_list("SampleData.csv")

if __name__ == '__main__':
    MainUI.action()
    # initialize()
    # park = Park.Park(cars)
    # car = Car.Car("50A-123456")
    # ticket = ParkingTicket.ParkingTicket(dt.datetime.now(), "")
    # park.park_car(car, ticket)
    # print("Parking:")
    # for i in cars:
    #     for o in i.parking_tickets:
    #         print(i.identity, o.fqn, o.arrive_time)
    # pickup = Pickup.Pickup(cars, price_list)
    # exist_time = dt.datetime.now() + dt.timedelta(hours=1)
    # print("Pick up:")
    # temp_ticket = pickup.get_pickup_ticket("50A-12345", exist_time)
    # print(temp_ticket.arrive_time, temp_ticket.exist_time, temp_ticket.fqn, temp_ticket.price)
    # pickup.checkout(10)
    # print("Result:")
    # for i in cars:
    #     for o in i.parking_tickets:
    #         print(i.identity, i.available_credit, o.fqn, o.arrive_time, o.exist_time, o.price)
    # history = History.History(cars)
    # history.export_history_of_car("50A-12345")