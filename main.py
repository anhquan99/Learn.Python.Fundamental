import datetime as dt
from Utils.ImportCsv import ImportParkingPriceList
from Business import Park, Pickup
from Data import Car, ParkingTicket
def initialize():
    global price_list
    global cars 
    cars = []
    importer = ImportParkingPriceList()
    price_list = importer.import_parking_price_list("SampleData.csv")

if __name__ == '__main__':
    initialize()
    park = Park.Park(cars)
    car = Car.Car("50A-12345")
    ticket = ParkingTicket.ParkingTicket(dt.datetime.now(), "")
    park.park_car(car, ticket)
    print("Parking:")
    for i in cars:
        for o in i.parking_tickets:
            print(i.identity, o.fqn, o.arrive_time)
    pickup = Pickup.Pickup(cars, price_list)
    exist_time = dt.datetime.now() + dt.timedelta(hours=1)
    print("Pick up:")
    temp_ticket = pickup.get_pickup_ticket("50A-12345", exist_time)
    print(temp_ticket.arrive_time, temp_ticket.exist_time, temp_ticket.fqn, temp_ticket.price)
    pickup.checkout(10)
    print("Result:")
    for i in cars:
        for o in i.parking_tickets:
            print(i.identity, i.available_credit, o.fqn, o.arrive_time, o.exist_time, o.price)