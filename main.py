# This is a sample Python script.
from AscendentRevenire import AscendentRevenire
from Gram import Grammar
from Rule import TerminalPoz

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


f = open("in.txt", "r")

gram = Grammar()

lines= f.readlines()
for line in lines :
    rule = line.split("->")
    rule[1]= rule[1][:len(rule[1])-1]
    combined = rule[0]+rule[1]
    gram.addRule(rule[0],rule[1])
    for c in combined:
        if c.isupper():
            if not (gram.containsNonTerminal(c)) and (c != 'E') and (c in rule[0]):
                gram.addNonterminal(c)
        else :
            if not gram.containsTemrinal(c):
                gram.addTerminal(c)

print("Terminals")
for el in gram.getTerminal():
    print(el)
print("Nonterminals")
for el in gram.getnonTerminal():
    print(el)

print("Rules:")
for el in gram.rules:
    print(el)

sequence = input("Enter the sequence:")

lst = []
for el in gram.rules[0].right:
    lst.append(el)
ASDR = AscendentRevenire("q",1,[TerminalPoz(gram.rules[0].left,1)],lst,len(sequence))
while ASDR.stare != "t" and ASDR.stare != "e":
    if ASDR.stare == "q":
        if len(ASDR.enterQueue)==0:
            if ASDR.poz == ASDR.sizeIn:
                ASDR.stare = "t"
            else:
                ASDR.stare = "r"
        else:
            varfB = ASDR.getVarfB()
            if gram.containsNonTerminal(varfB):
                #pop(β, A);
                A = ASDR.popB()
                ASDR.pushA(TerminalPoz(A,1))
                ASDR.pushB(TerminalPoz(gram.getRule(A,1).right,-1))
            else:
                if gram.containsTemrinal(varfB):
                    ASDR.poz = ASDR.poz + 1
                    xi = ASDR.popB()
                    ASDR.pushA(TerminalPoz(xi,-1))
                else:
                    ASDR.stare = "r"
    else:
        if ASDR.stare == "r":
            varf = ASDR.getVarfA()
            #terminal
            if varf.poz == -1:
                ASDR.poz = ASDR.poz - 1
                a = ASDR.popA()
                ASDR.pushB(a)
            else:
                varfA = ASDR.getVarfA()
                rule = gram.getRule(varfA.terminal,varfA.poz + 1)
                if rule != None:
                    #exists Aj+1
                    ASDR.stare = "q"
                    ASDR.popA()
                    ASDR.pushA(TerminalPoz(varfA.terminal,varfA.poz + 1))
                    ASDR.popBRule()
                    ASDR.pushB(TerminalPoz(rule.right,-1))
                else:
                    if ASDR.poz == 1 and len(ASDR.enterQueue) == 0:
                        s= "e"
                    else:
                        Aj = ASDR.popA()
                        ASDR.pushB(Aj)

if ASDR.stare == 'e':
    print("Errror")
else:
    print("Succes")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
