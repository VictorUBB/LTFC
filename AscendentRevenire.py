#Configuratie:
#(s,i,a,b)
# -s- starea automatului
# – q – stare normala
# – r – stare de revenire (sau b – back)
# – t – stare de terminare (terminare cu succes)
# – e – stare de eroare
# • i – pozitia (urmatoare) in secventa de intrare
# • a – stiva de lucru (de istorie): istoria r.p. aplicate
# • b – stiva de intrare:
class AscendentRevenire:
    def __init__(self,s,i,a,b,n):
        self.stare=s
        self.poz= i
        #contains elements of TerminalPoz
        self.workQueue = a
        self.enterQueue = b
        #marimea sirului de verificat
        self.sizeIn = n +1

    def getVarfB(self):
        return self.enterQueue[0]

    def popB(self):
        return self.enterQueue.pop(0)

    def popBRule(self,rule):
        rule = rule[::-1]
        for i in range(len(rule)):
            self.enterQueue.pop(0)
    def popA(self):
        return self.workQueue.pop(0)
    def pushA(self,elem):
        self.workQueue.insert(0,elem)

    def pushB(self,elem):
        elem.terminal = elem.terminal[::-1]
        for el in elem.terminal:
            self.enterQueue.insert(0,el)


    def getVarfA(self):
        return self.workQueue[0]
        # def checkSucces(self):
    #     if self.stare == "":
    #         if self.poz == int(self.sizeIn +1):
    #             if self.enterQueue.size()==0:
    #                 return True
    #
    #     return False
    #
    # def checkRevenire