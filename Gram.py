from Rule import Rule


class Grammar:
    def __init__(self):
        self.terminals=[]
        self.nonterminals = []
        self.rules = []

    def addTerminal(self,c):
        self.terminals.append(c)

    def addNonterminal(self,c):
        self.nonterminals.append(c)

    def containsTemrinal(self,c):
        return c in self.terminals

    def containsNonTerminal(self, c):
        return (c in self.nonterminals)

    def getTerminal(self):
        return self.terminals

    def getnonTerminal(self):
        return self.nonterminals

    def addRule(self,left,right):
        rule = Rule(left,right)
        self.rules.append(rule)

    def getRule(self,terminal,poz):
        pozList = 0
        for rule in self.rules:
            if terminal ==  rule.left:
                pozList = pozList + 1
                if pozList == poz:
                    #return the whole rule
                    return rule
        return None
