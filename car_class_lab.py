class Car(object):
    num_of_doors = []
    num_of_wheels = []
    def __init__(self,car_type,model='GM',name = 'General'):
        self.car_type = str (car_type)
        self.model=str(model)
        self.name=str(name)

    def car_doors (self):
        if (self.name=='Porshe' or self.name=='Koenigsegg'):
            num_of_doors.append(2)
        else:
            num_of_doors.append(4)
    def car_wheels (self):
        if self.car_type=='trailer':
            num_of_wheels.append(8)
        else:
            num_of_wheels.append(4)
    another = car_doors('trailer')
    print (another)