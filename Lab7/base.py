class Vehicle:
    vid = "asd"
    model = "asd"
    year = 0000

    def __init__(self, _vid,_model, _year):
        self.vid = _vid
        self.model = _model
        self.year = _year

    def __str__(self):
        return "VID: ", self.vid, " Model: ", self.model, " Year: ", self.year

    def __EQ__(self, other):
        if self.vid == other.vid:
            return True
        else: return False

    def is_new(self,n):
        newYear = 2026 - n
        if self.year > newYear & self.year < 2026 :
            return True
        else: return False

class Car (Vehicle):
    fuel_type = "electric"
    doors = 4

    def __str__(self):
        return "Car ", super.__str__(self), " Fuel type: ", self.fuel_type, " Doors: ", self.doors
    
    def __init__(self, _vid, _model, _year, _fuel, _doors):
        super().__init__(_vid, _model, _year)
        self.fuel_type = _fuel
        self.doors = _doors

class Truck (Vehicle):
    max_load = 0
    axles = 0

    def __str__(self):
        return "Truck ", super.__str__(self), " Max load: ", self.max_load, " Axles: ", self.axles
    
    def __init__(self, _vid, _model, _year, _load, _axles):
        super().__init__(_vid, _model, _year)
        self.load = _load
        self.load = _axles
    
class Motorcyle (Vehicle):
    engine_cc = 0
    type = "sport"

    def __str__(self):
    # super() fonksiyonunu çağırıp sonra metoduna erişmelisin
        return f"Motorcyle {super().__str__()} Engine cc: {self.engine_cc} Type: {self.type}"

    def __init__(self, _vid, _model, _year, _engine, _type):
        super().__init__(_vid, _model, _year)
        self.engine_cc = _engine
        self.type = _type

def save_fleet_to_file(vehicles, filename):
    try:
        f = open(filename,encoding = 'utf-8',mode="w")
        for thing in vehicles:
            f.write(str(thing) + "\n")
    finally:
        f.close

def load_fleet_from_file(filename):
    newList = []
    try:
        f = open(filename,encoding = 'utf-8')
        lines = f.readlinez()
        for line in lines:
            words = line.split()
            if words[0] == "Car":    
                newList.append(Car(words[1], words[2], words[3], words[4], words[5]))
            elif words[0] == "Truck":
                newList.append(Truck(words[1], words[2], words[3], words[4], words[5]))
            elif words[0] == "Motorcyle":
                newList.append(Motorcyle(words[1], words[2], words[3], words[4], words[5]))
    finally:
        f.close
    return newList

mylist = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Car("V002", "Tesla Model 3", 2023, "Electric", 4),
    Truck("V003", "Tesla Model 4", 2023, 500, 4),
    Truck("V004", "Tesla Model 4", 2023, 500, 4),
    Motorcyle("V005", "Tesla Model 3", 2023, 250, "Sport"),
    Motorcyle("V006", "Tesla Model 3", 2023, 250, "Sport")]

save_fleet_to_file(mylist, "fleet.txt")

newList = load_fleet_from_file("fleet.txt")

for thing in newList:
    print(thing)

for thing in newList:
    if thing.is_new(4):
        print(thing)

for thing in newList:
    if type(thing) == "Car" & thing.fuel_type == "Electric":
        print(thing)