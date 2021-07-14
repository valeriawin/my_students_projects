depart_pass,arrive_pass,date_pass = map(str,input("Введите место вылета, место прибытия, дату ").split ( ))
    

def pass_seats():# ввод количества мест
    pass_seats = int(input("введите количество мест "))
    return pass_seats

def pass_data():# ввод данных пассажира для заказ билета
    name, surname, email = map(str,input("Введите Имя Фамилию e-mail ").split ())
    return name, surname, email

class Flight:
    def __init__(self, depart,arrive,date,time,seats,price):

        self.depart = depart
        self.arrive = arrive
        self.date = date
        self.seats = seats
        self.price = price
        self.time = time

    

    def ticket_count(self,other): #минусует место от общего количества мест при заказе билета
        self.other = other
        self.seats -= other
        return self.seats

    def checkin_seats(self):#Проверка на количество мест
        if self.seats != 0:
            return self.seats
        else:
            return False


################################################################################################################

minskMoskow = Flight("Минск","Москва","30.04.2021", "13:20", 3, 200) # создаем рейс depart,arrive,date,seats,price
minskParis = Flight("Минск","Париж","01.05.2021","17:20", 2, 400)# создаем рейс depart,arrive,date,seats,price
flight_list = [minskMoskow, minskParis]#список всех рейсов

def check_in_fligt():# осуществляет поиск рейса ????как выводить оба результата, разные по времени?????
    for flight in flight_list:
        if depart_pass == flight.depart and arrive_pass == flight.arrive and date_pass == flight.date:
            return flight
                    #f"аэропорт вылета: {flight.depart}, аэропорт прибытия: {flight.arrive}, дата: {flight.date}, время: {flight.time}, стоимость: {flight.price}"
        else: 
            return 0
#################################################################################################################################

def main():
    if check_in_fligt() !=0:
        myFlight = check_in_fligt()#присваиваем новой переменной нужный экземпляр класса
        print(f"РЕЙС: {myFlight.depart} - {myFlight.arrive}, дата и врем вылета:{myFlight.date} {myFlight.time}, стоимость {myFlight.price}")
        mySeats = pass_seats()#вводим количество мест pass_seats

        if myFlight.checkin_seats()>=mySeats:
            myData = pass_data()
            print(f"Билет\n Пассажир: {myData[0]} {myData[1]}\n рейс: {myFlight.depart} -  {myFlight.arrive}, дата и врем вылета:{myFlight.date} {myFlight.time}")
            myFlight.ticket_count(mySeats)
            #print(myFlight.__dict__)# видно, что количество мест отнимается
        else:
            print(f"Мест недостаточно, осталось {myFlight.seats} места")

    
    else:
        print("По заданному маршруту или в заданную дату полеты не осуществляются")



main()


    

    

    

    
   



    
