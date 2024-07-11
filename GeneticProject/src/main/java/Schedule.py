from Timeslot import *
from Individual import *
from Classroom import *
from Professor import *
from Course import *
from Studentgroup import *
from Class import *

class Schedule:
    def __init__(self, schedule=None):
        if(schedule == None):
            self.rooms = {}
            self.professors = {}
            self.courses = {}
            self.groups = {}
            self.timeslots = {}
            self.roomMap = {}
            self.profMap = {}
            self.courseMap = {}
            self.groupMap = {}
            self.classes = []
            self.numClasses = 0
        else:
            self.rooms = schedule.rooms
            self.professors = schedule.professors
            self.courses = schedule.courses
            self.groups = schedule.groups
            self.timeslots = schedule.timeslots
            self.roomMap = schedule.roomMap
            self.profMap = schedule.profMap
            self.courseMap = schedule.courseMap
            self.groupMap = schedule.groupMap
            self.classes = schedule.classes
            self.numClasses = schedule.numClasses




    def getRoomMap(self):
        return self.roomMap

    def getProfMap(self):
        return self.profMap

    def getCourseMap(self):
        return self.courseMap

    def getGroupMap(self):
        return self.groupMap

    def getGroups(self):
        return self.groups

    def getTimeslots(self):
        return self.timeslots

    def getCourses(self):
        return self.courses

    def getProfessors(self):
        return self.professors

    def addRoom(self, roomId, roomName, capacity):
        self.rooms[roomId] = Classroom(roomId, roomName, capacity)

    def addProfessor(self, professorId, professorName, preferedroom=0, preferedtime=0):
        self.professors[professorId] = Professor(professorId, professorName, preferedroom, preferedtime)

    def addCourse(self, courseId, courseCode, course, professorIds,numStu):
        self.courses[courseId] = Course(courseId, courseCode, course, professorIds,numStu)

    def addGroup(self, groupId, groupname, courseIds):
        self.groups[groupId] = Studentgroup(groupId,groupname, courseIds)
        self.numClasses = 0

    def addTimeslot(self, timeslotId, timeslot):
        self.timeslots[timeslotId] = Timeslot(timeslotId, timeslot)

    def createClasses(self, individual):
        classes = []
        chromosome = individual.getChromosome()
        chromosomePos = 0
        classIndex = 0

        for group in self.getGroupsAsArray():
            courseIds = group.getCourseIds()
            for courseId in courseIds:
                newClass = Class(classIndex, group.getGroupId(), courseId)

                newClass.setTimeslot(chromosome[chromosomePos])
                chromosomePos += 1

                newClass.setRoomId(chromosome[chromosomePos])
                chromosomePos += 1

                newClass.setProfessor(chromosome[chromosomePos])
                chromosomePos += 1

                self.roomMap.setdefault(newClass.getRoomId(), []).append(newClass)
                self.groupMap.setdefault(newClass.getGroupId(), []).append(newClass)
                self.courseMap.setdefault(newClass.getCourseId(), []).append(newClass)
                self.profMap.setdefault(newClass.getProfessorId(), []).append(newClass)

                classes.append(newClass)
                classIndex += 1

        self.classes = classes

    def getRoom(self, roomId):
        if roomId not in self.rooms:
            print("Rooms doesn't contain key " + str(roomId))
        return self.rooms.get(roomId)

    def getRooms(self):
        return self.rooms

    def getRandomRoom(self):
        roomsArray = list(self.rooms.values())
        room = random.choice(roomsArray)
        return room

    def getProfessor(self, professorId):
        return self.professors.get(professorId)

    def getCourse(self, courseId):
        return self.courses.get(courseId)

    def getGroupCourses(self, groupId):
        group = self.groups.get(groupId)
        return group.getCourseIds()

    def getGroup(self, groupId):
        return self.groups.get(groupId)

    def getGroupsAsArray(self):
        return list(self.groups.values())

    def getTimeslot(self, timeslotId):
        return self.timeslots.get(timeslotId)

    def getRandomTimeslot(self):
        timeslotArray = list(self.timeslots.values())
        timeslot = random.choice(timeslotArray)
        return timeslot

    def getClasses(self):
        return self.classes

    def getNumClasses(self):
        if self.numClasses > 0:
            return self.numClasses
        numClasses = 0
        groups = list(self.groups.values())
        for group in groups:
            numClasses += len(group.getCourseIds())
        self.numClasses = numClasses
        return self.numClasses

    def calcClashes(self, size):
        clashes = 100
        for classA in self.classes:
            roomCapacity = self.getRoom(classA.getRoomId()).getRoomCapacity()
            numStu = self.getCourse(classA.getCourseId()).getStudentnumber()
            if roomCapacity < numStu:
                clashes -= 33 * size

            for classB in self.classes:
                if classA.getClassId() != classB.getClassId():  # Check only once per pair
                    if classA.getRoomId() == classB.getRoomId() and classA.getTimeslotId() == classB.getTimeslotId():
                        clashes -= 33 * size
                        break

                    if classA.getProfessorId() == classB.getProfessorId() and classA.getTimeslotId() == classB.getTimeslotId():
                        clashes -= 33 * size
                        break

                    # Check for group clash
                    if classA.getGroupId() == classB.getGroupId() and classA.getTimeslotId() == classB.getTimeslotId():
                        clashes -= 33 * size
                        break

            for classB in self.classes:
                tmp_Prof = classB.getProfessorId()
                tmp_Room = classB.getRoomId()
                if self.getProfessor(tmp_Prof).getPreferedroom() == tmp_Room:
                    clashes += 1

            for classB in self.classes:
                tmp_Prof = classB.getProfessorId()
                tmp_Time = classB.getTimeslotId()
                if self.getProfessor(tmp_Prof).getPreferedtime() == tmp_Time:
                    clashes += 2

        return clashes
