from map import Map
def readData(file):
    f=open(file,"r")
    nodes = int(f.readline())
    j = nodes
    list = []
    for x in f:
        l = x.split(",")
        l[-1] = l[-1].split("\n")[0]
        list.append(l)
        j -= 1
        if j == 0:
            break
    first = int(f.readline())
    last = int(f.readline())
    return nodes, list, first, last


def greedy(m, i, visited, suma, first,mergiPrinToate):
    min, t = m.minNeigb(i)
    if t == ():
        print("Nu mai exista muchii!")

    if visited.__contains__(t[1]):
        if t[1] == first:
            ok=False
            if mergiPrinToate==False:
                ok=True
            elif visited.__len__() == m.nrNoduri:
                ok = True
            if ok==True:
                suma += min
                visited[t[1]]=True
                return suma, visited
        m.deleteEdge(t[0], t[1])
        return greedy(m, i, visited, suma, first, mergiPrinToate)
    else:
        suma += min
        visited[t[1]]=True
        if t[1] == first and mergiPrinToate==False:
            return suma, visited
        return greedy(m, int(t[1]), visited, suma, first, mergiPrinToate)


def resolve(m, i,end):
    l=[]
    vis={}
    vis[i]=True
    mergiPrinToate=False
    if i==end:
        mergiPrinToate=True
    suma,v=greedy(m, i, vis, 0, end,mergiPrinToate)
    for j in v.keys():
        l.append(j)
    return suma,l


def main():
    nrNoduri, list, first, last = readData("testeGrele")
    m = Map(nrNoduri)
    m.addFromMatrix(list)
    min, v = resolve(m, 1,1)
    print(nrNoduri)
    print(v)
    print(min)

    m = Map(nrNoduri)
    m.addFromMatrix(list)
    min2, v2 = resolve(m, 2, 4)
    print(v2.__len__())
    print(v2)
    print(min2)
    tests()

def tests():
    nrNoduri, list, first, last = readData("testeGrele")
    m = Map(nrNoduri)
    m.addFromMatrix(list)
    min, v = resolve(m, 1, 1)
    assert min==31
    assert v==[1, 3, 8, 4, 2, 7, 5, 6]

    m = Map(nrNoduri)
    m.addFromMatrix(list)
    min2, v2 = resolve(m, 2, 4)
    assert min2 == 12
    assert v2 == [2, 3, 1, 7, 4]

    nrNoduri, list, first, last = readData("testeMedii")
    m = Map(nrNoduri)
    m.addFromMatrix(list)
    min, v = resolve(m, 1, 1)
    assert min == 27
    assert v == [1, 3, 2, 4, 6, 5]

    m = Map(nrNoduri)
    m.addFromMatrix(list)
    min2, v2 = resolve(m, 2, 4)
    assert min2 == 22
    assert v2 == [2, 3, 1, 5, 6, 4]

    nrNoduri, list, first, last = readData("testeUsoare")
    m = Map(nrNoduri)
    m.addFromMatrix(list)
    min, v = resolve(m, 1, 1)
    assert min == 140
    assert v == [1, 2, 3, 4]

    m = Map(nrNoduri)
    m.addFromMatrix(list)
    min2, v2 = resolve(m, 2, 4)
    assert min2 == 90
    assert v2 == [2, 1, 3, 4]

main()
