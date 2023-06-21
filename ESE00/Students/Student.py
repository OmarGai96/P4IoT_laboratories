import json
class Student:
    def __init__(self, Name, Surname, birthYear):
        self.Name = Name
        self.Surname = Surname
        self.birthYear = birthYear
        self.bachelor = False
        self.master = False
        self.votesList = []

    def show(self):
        print(f"Hi, I'm {self.Name} {self.Surname}", end="")

    def age(self, currentYear):
        return currentYear-self.birthYear
    
    def save(self, filename):
        fp = open(filename, 'w')
        stringa = self.Name+","+self.Surname+","+str(self.birthYear)+"\n" #birthYear is an integer
        fp.write(stringa)
        fp.close()

    def isBachelor(self):
        return self.bachelor
    
    def isMaster(self):
        return self.master
    
    def setDegree(self, stringa):
        if stringa == "Master":
            self.master = True
        elif stringa == "master degree":
            self.master = True
        elif stringa == "Bachelor":
            self.bachelor = True
        elif stringa == "Bachelor degree":
            self.bachelor = True

    def readStudentVotes(self, studentFile):
        fp = open(studentFile, "r")
        fileContent = fp.readline()
        self.votesList = fileContent.split(',')
        fp.close()

    def printVotes(self):
        print(f"Votes for student: {self.Name} {self.Surname}")
        for v in self.votesList:
            print(f"\t{v}")
            
    def printVotesFile(self,filename):
        fp = open(filename, 'a')
        fp.write("List of votes\n")
        for s in self.votesList:
            stringa = str(s)+" "
            fp.write(stringa)
        fp.close()
        
    def asDictionary(self,filename):
        myDict = {}
        myDict["name"] = self.Name
        myDict["surname"] = self.Surname
        myDict["birthYear"] = self.birthYear
        myDict["votes"] = self.votesList
        json.dump(myDict, open(filename, "w"), indent=4)
        
    def createStudentFromJSON(self,filename):
        myDict = json.load(open(filename))
        self.Name = myDict["name"]
        self.Surname = myDict["surname"]
        self.birthYear = myDict["birthYear"]
        self.bachelor = False
        self.master = False
        self.votesList = myDict["votes"]
