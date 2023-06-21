from Student import *

if __name__ == "__main__":
    name= "Paolo"
    surname = "Rossi"

    studentA = Student(name,surname,1992)
    studentA.setDegree("Master")
    #studentA.show()

    studentB = Student("Marco", "Grandi",1998)
    studentB.setDegree("Bachelor")
    
    studentA.save("StudentA.txt")
    studentB.save("StudentB.txt")

    studentList = []
    studentList.append(studentA)
    studentList.append(studentB)

    for s in studentList:
        s.show()
        print(f"\tMy age is: {s.age(2023)}", end="")
        if s.isBachelor() == True:
            print(" -> Bachelor Degree student")
        elif s.isMaster() == True:
            print(" -> Master Degree student")    

    
    
    studentA.readStudentVotes("studentAVotes.txt")
    studentA.printVotes()

    studentB.readStudentVotes("studentBVotes.txt")
    studentB.printVotes()
    
    studentA.printVotesFile("StudentA.txt")
    studentB.printVotesFile("StudentB.txt")
    
    studentA.asDictionary("StudentA.json")
    studentB.asDictionary("StudentB.json")
    
    studentC = Student("","",0)
    studentC.createStudentFromJSON("newStudent.json")
    
    studentC.asDictionary("StudentC.json")
    