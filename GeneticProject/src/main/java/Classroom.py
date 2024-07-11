class Classroom:
    def __init__(self, roomId, roomNumber, capacity):
        self.roomId = roomId
        self.roomNumber = roomNumber
        self.capacity = capacity

    def getRoomId(self):
        return self.roomId

    def getRoomNumber(self):
        return self.roomNumber

    def getRoomCapacity(self):
        return self.capacity
