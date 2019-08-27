from datetime import time

class Courses:
    _profList = []

    def __init__(self, courseID, professor, daysOfWeek, startTime, endTime, \
                 courseName = ''):
        self._courseID = courseID
        self._prof = professor
        self._days = daysOfWeek
        self._start = startTime
        self._end = endTime
        self._courseName = courseName

        if self._prof not in Courses._profList:
            Courses._profList.append(self._prof)
    
    def __str__(self):
        tmpStr = "Course ID: " + self._courseID
        optStr = "\nProfessor: " + self._prof + "\nMeeting Days: " + self._days +\
                 "\nStart Time: " + self._start.strftime("%I:%M %p") + "\nEnd Time: " +\
                 self._end.strftime("%I:%M %p")

        if len(self._courseName) != 0:
            print(len(self._courseName))
            tmpStr += "\nCourse Name: " + self._courseName + optStr
            return tmpStr
        else:
            return tmpStr + optStr
    
    def getProfessor(self):
        return self._prof
    
    def getDaysOfWeek(self):
        return self._days
    
    def getStartTime(self):
        return self._start

    def setCourseName(self, courseName):
        self._courseName  = courseName

    def calcMeetingLength(self):
        print("Class length: ", self._end - self._start)
