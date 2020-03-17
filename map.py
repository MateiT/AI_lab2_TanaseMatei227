from collections import defaultdict


class Map():
    def __init__(self, nrNoduri):
        self.nrNoduri = nrNoduri
        self.muchii=defaultdict(list)
        self.cost=defaultdict(int)


    def addEdge(self, u, v, c):
        self.muchii[u].append(v)
        self.cost[(u,v)]=c

    def addFromMatrix(self,list):
        index = 1
        for l in list:
            j = 1
            for el in l:
                if int(el) != 0:
                    self.addEdge(index, j, int(el))
                j += 1
            index += 1
    def deleteEdge(self,u,v):
        if self.muchii[u].__len__()>1:
            self.muchii[u].remove(v)
            self.muchii[v].remove(u)
        else:
            self.muchii[u].remove(v)
            self.muchii[v].remove(u)

    def giveAsList(self):
        l = []
        for x in range(0, self.nrNoduri):
            l.append([])
        for e in l:
            for x in range(0, self.nrNoduri):
                e.append(0)
        for i in self.muchii:
            for j in self.muchii[i]:
                l[i-1][j-1] = self.cost[(i,j)]
        return l

    def printAsMatrix(self):
        print(self.giveAsList())

    def minNeigb(self,i):
        min=999999
        t=()
        for j in self.muchii[i]:
            if self.cost[(i,j)]<min:
                min=self.cost[(i,j)]
                t=(i,j)
        return min,t
