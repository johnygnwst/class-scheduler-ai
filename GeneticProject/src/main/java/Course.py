import random


class Course:
    def __init__(self, courseId, courseCode, course, professorIds,numStu):
        self.courseId = courseId
        self.courseCode = courseCode
        self.course = course
        self.professorIds = professorIds
        self.numStu = numStu

    def getCourseId(self):
        return self.courseId

    def getCourseCode(self):
        return self.courseCode

    def getCourseName(self):
        return self.course

    def getRandomProfessorId(self):
        professorId = random.choice(self.professorIds)
        return professorId

    def getStudentnumber(self):
        return self.numStu
