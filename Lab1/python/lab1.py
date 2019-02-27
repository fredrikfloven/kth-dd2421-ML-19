import monkdata as m
import dtree as d
import random

sets = [m.monk1,m.monk2,m.monk3]

def assignment1():
    print("Assignment 1")
    for x in sets:
        print(d.entropy(x))
    print("")

def assignment3():
    print("Assignment 3")
    i = 1
    for x in sets:
        for y in range(6):
            print("monk" + str(i) + " attribute " + str(y+1))
            avggain = d.averageGain(x,m.attributes[y])
            print("Information Gain: " + str(avggain))
        i += 1
        print("Best attribute: " + str(d.bestAttribute(x,m.attributes)) + "\n")
    print("")
    

def assignment5pre():
    w, h = 6, 4;
    Matrix = [[0 for x in range(w)] for y in range(h)] 
    print("Assignment 5 pre")
    print(d.bestAttribute(m.monk1,m.attributes))
    for attr in range(4):
        print("monk1subset where attribute a5 = " + str(attr+1))
        entropy = d.entropy(d.select(m.monk1,m.attributes[4],attr+1))
        print("Entropy for subset after 1 split: " + str(entropy))

        if(entropy != 0):
            for x in range(6):
                avggain = d.averageGain(d.select(m.monk1,m.attributes[4],attr+1),m.attributes[x])
                Matrix[attr][x] = avggain
            subset = d.select(m.monk1,m.attributes[4],attr+1)
            print("Best attribute: " + str(d.bestAttribute(subset, m.attributes)) + "\n")
        print("")

def assignment5():
    print("Assignment 5")
    t=d.buildTree(m.monk1,m.attributes)
    print("\n Monk1:")
    #print(t)
    print("Correctly classified training data: ")
    print(d.check(t, m.monk1))
    print("Correctly classified  test data: ")
    print(d.check(t, m.monk1test))
    print("most common: ")
    print(d.mostCommon(m.monk1))

    t2=d.buildTree(m.monk2,m.attributes)
    print("\n Monk2:")
    #print(t2)
    print("Correctly classified  training data: ")
    print(d.check(t2, m.monk2))
    print("Correctly classified  test data: ")
    print(d.check(t2, m.monk2test))
    print("most common: ")
    print(d.mostCommon(m.monk2))

    t3=d.buildTree(m.monk3,m.attributes)
    print("\n Monk3:")
    #print(t3)
    print("Correctly classified  training data: ")
    print(d.check(t3, m.monk3))
    print("Correctly classified  test data: ")
    print(d.check(t3, m.monk3test))
    print("most common: ")
    print(d.mostCommon(m.monk3))

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata)*fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def possibleTrees(tree):
    ldata = list(tree)
    return ldata

def assignment6():
    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    besttree1 = d.check(d.buildTree(m.monk1, m.attributes), m.monk1test)
    besttree3 = d.check(d.buildTree(m.monk3, m.attributes), m.monk3test)
    for fraction in fractions:
        for times in range(100):
            monk1train, monk1val = partition(m.monk1, fraction)
            monk3train, monk3val = partition(m.monk3, fraction)
            tree1 = d.buildTree(monk1train, m.attributes)
            tree3 = d.buildTree(monk3train, m.attributes)
            treelist1 = possibleTrees(d.allPruned(tree1))
            treelist3 = possibleTrees(d.allPruned(tree3))
            for prunedTree in treelist1:
                if(d.check(prunedTree, monk1val) > besttree1):
                    besttree1 = prunedTree
            for prunedTree in treelist3:
                if(d.check(prunedTree, monk3val) > besttree3):
                    besttree3 = prunedTree

    print(d.check(besttree1, m.monk1test))
    print(d.check(besttree3, m.monk3test))


def assignment6_2():
    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    bestFracArray = [0, 0, 0, 0, 0, 0]
    #besttree1 = d.check(d.buildTree(m.monk1, m.attributes), m.monk1test)
    #besttree3 = d.check(d.buildTree(m.monk3, m.attributes), m.monk3test)
    for times in range(100):
        bestFrac, tree = bestFractionAndAmountCorrectlyClassified(m.monk1, fractions, m.monk1test)
        bestFracArray[bestFrac] += 1
    print("List of fractions returning a good result for dataset 1: " + str(bestFracArray))
    for times in range(100):
        bestFrac, tree = bestFractionAndAmountCorrectlyClassified(m.monk3, fractions, m.monk3test)
        bestFracArray[bestFrac] += 1
    print("List of fractions returning a good result for dataset 3: " + str(bestFracArray))

def bestFractionAndAmountCorrectlyClassified(sampleData, fractions, testData):
    bestFraction = 0.0
    correctlyClassified = 0.0
    bestTree = d.check(d.buildTree(sampleData, m.attributes), testData)

    for fraction in range(len(fractions)):
        trainingData, valuationData = partition(sampleData, fractions[fraction])
        tree = d.buildTree(trainingData, m.attributes)
        prunedTreeList = possibleTrees(d.allPruned(tree))
        for prunedTree in prunedTreeList:
                if(d.check(prunedTree, valuationData) > correctlyClassified):
                    correctlyClassified = d.check(prunedTree, valuationData)
                    bestFraction = fraction
                    bestTree = prunedTree
    return bestFraction, bestTree


def testprune():
    tree = d.buildTree(m.monk1, m.attributes)
    print("Original tree correct: " + str(d.check(tree, m.monk1test)))
    treelist = possibleTrees(d.allPruned(tree))
    i = 0
    for prunedTree in treelist:
        i = i + 1
        print(i)
        print(d.check(prunedTree, m.monk1test))
#testprune()
assignment6_2()