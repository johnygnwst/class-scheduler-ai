class Professor:
    def __init__(self, professorId, professorName, preferedroom=0, preferedtime=0):
        self.professorId = professorId
        self.professorName = professorName
        self.preferedroom = preferedroom
        self.preferedtime = preferedtime

    def getProfessorId(self):
        return self.professorId

    def getProfessorName(self):
        return self.professorName

    def getPreferedroom(self):
        return self.preferedroom

    def getPreferedtime(self):
        return self.preferedtime
