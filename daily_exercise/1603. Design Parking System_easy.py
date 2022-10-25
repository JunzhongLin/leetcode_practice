class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park_lot_dict = {}
        self.park_lot_dict[1] = big
        self.park_lot_dict[2] = medium
        self.park_lot_dict[3] = small

    def addCar(self, carType: int) -> bool:
        if self.park_lot_dict[carType] != 0:
            self.park_lot_dict[carType] -= 1
            return True
        else:
            return False