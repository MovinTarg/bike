class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print 'Price: ' + str(self.price) + ' | Max Speed: ' + str(self.max_speed) + 'mph | Miles: ' + str(self.miles)
        return self
    def ride(self):
        self.miles += 10
        print 'Riding'
        return self
    def reverse(self):
        if self.miles >=5:
            self.miles -=5
        else:
            self.miles = 0
        print 'Reversing'
        return self

bike1 = bike(100, 25)
bike2 = bike(90, 20)
bike3 = bike(80, 15)

print bike1.ride().ride().ride().reverse().displayInfo()
print bike2.ride().ride().reverse().reverse().displayInfo()
print bike3.reverse().reverse().reverse().displayInfo()

