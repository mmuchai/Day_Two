class Car(object):

    def __init__(self,car_type,model='GM',name = 'General'):
        self.car_type = str (car_type)
        self.model=str(model)
        self.name=str(name)
        self.num_of_doors = []
        self.num_of_wheels = []

    def car_doors (self):
        for door in num_of_doors
            if (self.name=='Porshe' or self.name=='Koenigsegg'):
                self.num_of_doors.append(2)
                return self.num_of_doors
            else:
                self.num_of_doors.append(4)
                return self.num_of_doors
    def car_wheels (self):

        if self.car_type=='trailer':
            num_of_wheels.append(8)
        else:
            num_of_wheels.append(4)
    def car_speed(self, speed = 0):
        self.speed = int (speed)
toyota = Car('Corolla')
print (toyota.car_doors(), porshe.car_doors())
print (vars(toyota))