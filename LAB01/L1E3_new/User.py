##SUBCLASS 1 USER

    
class User:
    def __init__ (self):
        self.userName = ""
        self.userID = -1
        self.chatID = -1    #integer
        self.houseList = [] ##The houseID is identified by an integer

    #getter and setter methods    

    def getName(self):
        return self.userName

    def setName(self, newName):
        self.userName = newName
        return

    def getUserID(self):
        return self.userID

    def setUserID(self, newUserID):
        self.userID = int(newUserID)
        return

    def getChatID(self):
        return self.chatID

    def setChatID(self, newID):
        self.chatID = int(newID)
        return
    
    ## ADD methods for list
    
    def addHouse(self, value):
        hID = int(value)
        #TODO: controllo su casa già esistente
        self.houseList.append(hID)
        self.houseList.sort()       #ascending order to maintain correct order
        return
    
    ## ADD NEW methods (when input value come from user)
    

    ## PRINT methods, to print info
    
    def printHouses(self):
        for i in self.houseList:
            print(f"\t\thouseID: {i}")
        return
    
    def printAllInfo(self):
        print(f"\tuserName: {self.userName}")
        print(f"\tuserID:    {self.userID}")
        print(f"\tchatID:    {self.chatID}")
        print("\tList of houses ID: ", end='')
        for i in self.houseList:
            print(f"{i} ", end='')
        print('')
        return
            
    #OTHERS  methods
    
    def popHouse(self):
        return self.houseList.pop()

    def popHouseByID(self, index):
        "return an integer as ID"
        #TODO: controllo errore index non esistente
        return self.houseList.pop(index)
    
    def getUser(self):
        selfUser = {}
        selfUser["userName"] = self.userName
        selfUser["userID"] = self.userID
        selfUser["chatID"] = self.chatID = -1    #integer
        lista = []
        for h in self.houseList:
            casa = {}
            casa["houseID"] = h
            lista.append(casa)
        selfUser["houses"] = lista
        return selfUser