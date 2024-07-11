from Schedule import *
from GeneticAlgorithm import *
import time
from prettytable import PrettyTable

class ScheduleAlgo:
    @staticmethod
    def initializeSchedule() -> Schedule:
        schedule = Schedule()

        schedule.addRoom(1, "A1", 25)
        schedule.addRoom(2, "B2", 26)
        schedule.addRoom(3, "C3", 30)
        schedule.addRoom(4, "D4", 30)
      #  schedule.addRoom(5, "E5", 25)
      #  schedule.addRoom(6, "F6", 26)
       # schedule.addRoom(7, "G7", 30)
       # schedule.addRoom(8, "H8", 30)
       # schedule.addRoom(9, "I9", 15)
       # schedule.addRoom(10, "J10", 30)
      #  schedule.addRoom(11, "K11", 20)
       # schedule.addRoom(12, "L12", 25)
        #schedule.addRoom(13, "M13", 26)
       # schedule.addRoom(14, "N14", 20)
        #schedule.addRoom(15, "O15", 30)




        schedule.addTimeslot(1, "Monday 9:00 - 11:00")
        schedule.addTimeslot(2, "Monday 11:00 - 13:00")
        schedule.addTimeslot(3, "Monday 13:00 - 15:00")
        schedule.addTimeslot(4, "Monday 15:00 - 17:00")
        schedule.addTimeslot(5, "Monday 17:00 - 19:00")
        schedule.addTimeslot(5, "Monday 19:00 - 21:00")
        schedule.addTimeslot(6, "Tuesday 9:00 - 11:00")
        schedule.addTimeslot(7, "Tuesday 11:00 - 13:00")
        schedule.addTimeslot(8, "Tuesday 13:00 - 15:00")
        schedule.addTimeslot(9, "Tuesday 15:00 - 17:00")
        schedule.addTimeslot(10, "Tuesday 17:00 - 19:00")
        schedule.addTimeslot(11, "Tuesday 19:00 - 21:00")
        schedule.addTimeslot(12, "Wednesday 9:00 - 11:00")
        schedule.addTimeslot(13, "Wednesday 11:00 - 13:00")
        schedule.addTimeslot(14, "Wednesday 13:00 - 15:00")
        schedule.addTimeslot(15, "Wednesday 15:00 - 17:00")
        schedule.addTimeslot(16, "Wednesday 17:00 - 19:00")
        schedule.addTimeslot(17, "Wednesday 19:00 - 21:00")
        schedule.addTimeslot(18, "Thursday 9:00 - 11:00")
        schedule.addTimeslot(19, "Thursday 11:00 - 13:00")
        schedule.addTimeslot(20, "Thursday 13:00 - 15:00")
        schedule.addTimeslot(21, "Thursday 15:00 - 17:00")
        schedule.addTimeslot(22, "Thursday 17:00 - 19:00")
        schedule.addTimeslot(23, "Thursday 19:00 - 21:00")
        schedule.addTimeslot(24, "Friday 9:00 - 11:00")
        schedule.addTimeslot(25, "Friday 11:00 - 13:00")
        schedule.addTimeslot(26, "Friday 13:00 - 15:00")
        schedule.addTimeslot(27, "Friday 15:00 - 17:00")
        schedule.addTimeslot(28, "Friday 17:00 - 19:00")
        schedule.addTimeslot(29, "Friday 19:00 - 21:00")

        schedule.addProfessor(0, "James Web")
        schedule.addProfessor(1, "Mike Brown")
        schedule.addProfessor(2, "Steve Day")
        schedule.addProfessor(3, "George Miller")
        schedule.addProfessor(4, "Lily Johns")
        schedule.addProfessor(5, "Jannifer Dickens")
        schedule.addProfessor(6, "Jane Doe")
        schedule.addProfessor(7, "Andrew Lively")
        schedule.addProfessor(8, "John Drake")
        schedule.addProfessor(9, "Mila Kasper")
        schedule.addProfessor(10, "Katherine Balvin")
        schedule.addProfessor(11, "Stamatia Papa")
        schedule.addProfessor(12, "Austin Day")
        schedule.addProfessor(13, "Helena Kosta")
        schedule.addProfessor(14, "Eirini Best")



        schedule.addCourse(1, "AA", "Algorithms", [0,11,8],30)
        schedule.addCourse(2, "DD", "Database", [4,8,10],19)
        schedule.addCourse(3, "CC", "Cloud Computing", [10,0,8],30)
        schedule.addCourse(4, "WD", "Web Development", [4,0,10],30)
        schedule.addCourse(5, "AE", "Application Engineering", [4,8,11],25)
        schedule.addCourse(6, "DS", "Data Science", [4,11,10],25)
        schedule.addCourse(7, "BI", "Business Intelligence", [8,11,10],30)
        schedule.addCourse(8, "JA", "JAVA", [8,0,4],22)
        schedule.addCourse(9, "PP", "Python", [0,11,8],26)
        schedule.addCourse(10, "CC", "C++", [11,4,8],30)
        schedule.addCourse(11, "MM", "Mathematics 2", [10,0,11],30)
        schedule.addCourse(12, "ML", "Matlab", [8,10,11],26)
        schedule.addCourse(13, "SQL", "SQL", [10,8,11],15)
        schedule.addCourse(14, "JV", "Javascript", [8,11,4],20)
        schedule.addCourse(15, "HTML", "HTML", [0,8,4],30)
        schedule.addCourse(16, "MM", "Mathematics 3", [4, 11,0], 30)
        schedule.addCourse(17, "ML", "Matlab 2 (Epilogis)", [0,10,11], 26)
        schedule.addCourse(18, "SQL", "SQL 2", [0, 11,10], 15)
        schedule.addCourse(19, "JV", "Javascript 2 (Epilogis)", [0,11,4], 30)
        schedule.addCourse(20, "HTML", "HTML 2 (Epilogis)", [0,10,4], 30)
        schedule.addCourse(21, "AA", "Algorithms 2", [14, 4,8], 30)
        schedule.addCourse(22, "DD", "Database 2 (Epilogis)", [14,7,11], 30)
        schedule.addCourse(23, "CC", "Cloud Computing 2 (Epilogis)", [10, 11,7], 20)
        schedule.addCourse(24, "WD", "Web Development 2", [7,8,14], 30)
        schedule.addCourse(25, "AE", "Application Engineering 2 (Epilogis)", [7,14,4], 30)
        schedule.addCourse(26, "DP", "Python Practice", [0,11,8],26)
        schedule.addCourse(27, "DP", "C++ Practice", [11,4,8],30)
        schedule.addCourse(28, "DP", "SQL Practice", [10,8,11],15)
        schedule.addCourse(29, "ML", "Matlab 2 (Epilogis) Practice", [0,10,11], 26)
        schedule.addCourse(30, "SQL", "SQL 2 Practice", [0, 10,11], 15)
        schedule.addCourse(31, "JV", "Javascript 2 (Epilogis) Practice", [0,4,11], 30)
        schedule.addCourse(32, "HTML", "HTML 2 (Epilogis) Practice", [0,10,4], 30)
        schedule.addCourse(33, "JA", "JAVA Practice", [8,0,4], 22)
        schedule.addCourse(34, "ML", "Matlab Practice", [8,10,11], 26)
        schedule.addCourse(35, "JV", "Javascript Practice", [8,11,4], 20)
        schedule.addCourse(36, "HTML", "HTML Practice", [0,8,4], 30)
        schedule.addCourse(37, "DD", "Database 2 (Epilogis) Practice", [14,7,11], 30)
        schedule.addCourse(38, "WD", "Web Development 2 Practice", [7,8,14], 30)
        schedule.addCourse(39, "AE", "Application Engineering 2 (Epilogis) Practice", [7,14,4], 30)
        schedule.addCourse(40, "AA", "Algorithms 2 Practice", [6, 4, 8], 30)
        schedule.addCourse(41, "CC", "Cloud Computing 2 (Epilogis) Practice", [10,11,7], 20)
        schedule.addCourse(42, "DD", "Database Practice", [4,10,8], 19)
        schedule.addCourse(43, "AA", "Algorithms Practice", [0, 8,11], 30)
        schedule.addCourse(44, "CC", "Cloud Computing Practice", [10,0,8], 30)
        schedule.addCourse(45, "AE", "Application Engineering Practice", [4,8,11], 25)
        schedule.addCourse(46, "WD", "Web Development Practice", [4,10,0], 30)
        schedule.addCourse(47, "DS", "Data Science Practice", [11, 10,4], 25)
        schedule.addCourse(48, "BI", "Business Intelligence Practice", [8,10,11], 30)
        schedule.addCourse(49, "MM", "Mathematics 2 Practice", [10,0,11],30)
        schedule.addCourse(50, "AA", "Algorithms 3", [0, 14, 2], 30)
        schedule.addCourse(51, "DD", "Database 3 (Epilogis)", [2, 8, 7], 30)
        schedule.addCourse(52, "CC", "Cloud Computing 3 (Epilogis)", [0,2,7], 20)
        schedule.addCourse(53, "WD", "Web Development 3", [7,10,2], 30)
        schedule.addCourse(54, "AE", "Application Engineering 3 (Epilogis)", [7, 0, 11], 30)
        schedule.addCourse(55, "MM", "Mathematics 3 Practice", [4,11,5], 30)
        schedule.addCourse(56, "WD", "Web Development 3 Practice", [7,10, 1], 30)
        schedule.addCourse(57, "CC", "Cloud Computing 3 (Epilogis) Practice", [0,2,7], 20)
        schedule.addCourse(58, "AE", "Application Engineering 3 (Epilogis) Practice", [7, 0, 11], 30)
        schedule.addCourse(59, "DD", "Database 3 (Epilogis) Practice", [2, 8, 7], 30)
        schedule.addCourse(60, "AA", "Algorithms 3 Practice", [0, 6, 1], 30)

        schedule.addGroup(1,"1st Year",[1,7,5,4,45,45,46,46,48,48])
        schedule.addGroup(2,"2nd Year",[9,26,26,3,44,44,15,36,36,12,34,34])
        schedule.addGroup(3,"3rd Year",[11,13,28,28,8,33,33,6])
        schedule.addGroup(4,"4th Year",[2,14,35,35,17,29,29,10,27,27])
        schedule.addGroup(5,"5th Year",[18,30,30,16,19,31,31,20,32,32])



        return schedule

    @staticmethod
    def PrintClassAll(schedule):
        classes = schedule.getClasses()
        weekly_schedule = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

        for bestClass in classes:
            timeslot = schedule.getTimeslot(bestClass.getTimeslotId()).getTimeslot()
            day = timeslot.split()[0]

            class_details = {
                "course": schedule.getCourse(bestClass.getCourseId()).getCourseName(),
                "student_group": schedule.getGroup(bestClass.getGroupId()).getGroupname(),
                "room": schedule.getRoom(bestClass.getRoomId()).getRoomNumber(),
                "professor": schedule.getProfessor(bestClass.getProfessorId()).getProfessorName(),
                "timeslot": timeslot
            }
            if day in weekly_schedule:
                weekly_schedule[day].append(class_details)
            else:
                weekly_schedule.setdefault("Unknown", []).append(class_details)

        # Print the organized schedule using pretty tables
        for day, classes in weekly_schedule.items():
            if classes:  # Only print the table if there are classes on that day
                table = PrettyTable()
                table.field_names = ["Course", "Group", "Room", "Professor", "Timeslot"]
                for class_detail in classes:
                    table.add_row([class_detail["course"], class_detail["student_group"], class_detail["room"],
                                   class_detail["professor"], class_detail["timeslot"]])

                print(f"---- {day} ----")
                print(table)
                print("*****************************************************************")


if __name__ == "__main__":

    stime = time.perf_counter()
    schedule = ScheduleAlgo.initializeSchedule()

    ga = GeneticAlgorithm(1000, 0.01, 0.9, 2, 5)

    population = ga.initializingPopulation(schedule)

    ga.calcPopulation(population, schedule)

    generation = 1
    maxGen = 1000

    while not (generation > maxGen or ga.isTerminating(population)):
        print("Generation No." + str(generation) + " Best fitness: " + str(population.getFittest(0).getFitness()))

        population = ga.crossoverPopulation(population)

        population = ga.mutatingPopulation(population, schedule)

        ga.calcPopulation(population, schedule)

        generation += 1

    # Print fitness
    schedule.createClasses(population.getFittest(0))
    print()
    print("Solution found in " + str(generation) + " generations")
    print("Final solution fitness: " + str(population.getFittest(0).getFitness()))
    print("Clashes: " + str(schedule.calcClashes(100)))

    ScheduleAlgo.PrintClassAll(schedule)

    print(time.perf_counter() - stime)
