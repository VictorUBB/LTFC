class Rule:
    def __init__(self,left,right):
        self.left=left
        self.right=right

    def __str__(self):
        return self.left+"->"+self.right
class TerminalPoz:
    #if poz == -1 then nonterminal
    def __init__(self,terminal,poz):
        self.terminal= terminal
        self.poz = poz