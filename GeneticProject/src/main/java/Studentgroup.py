class Studentgroup:
    def __init__(self, groupId,groupname, courseIds):
        self.groupId = groupId
        self.groupname = groupname
        self.courseIds = courseIds

    def getGroupId(self):
         return self.groupId

    def getGroupname(self):
      return self.groupname



    def getCourseIds(self):
        return self.courseIds
