class Class:
    def __init__(self, classId, studentGroupId, courseId):
        self.classId = classId
        self.courseId = courseId
        self.studentGroupId = studentGroupId
        self.professorId = None
        self.timeslotId = None
        self.roomId = None

    def setProfessor(self, professorId):
        self.professorId = professorId

    def setTimeslot(self, timeslotId):
        self.timeslotId = timeslotId

    def setRoomId(self, roomId):
        self.roomId = roomId

    def getClassId(self):
        return self.classId

    def getGroupId(self):
        return self.studentGroupId

    def getCourseId(self):
        return self.courseId

    def getProfessorId(self):
        return self.professorId

    def getTimeslotId(self):
        return self.timeslotId

    def getRoomId(self):
        return self.roomId
