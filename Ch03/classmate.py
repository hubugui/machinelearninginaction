# coding=utf-8

import os, sys
import trees, treePlotter

# name   industry   profession    sex    摄影     自驾游    SNS达人   github   翻墙   常阅读   科幻迷  兴趣广泛    吹牛    分类

def getTrainingDatas():
    dataSet = [
        ["it", "gm",       "man", 1, 1, 0, 0, 0, 0, 0, 1, 0, "liver"],
        ["it", "engineer", "man", 0, 1, 0, 0, 0, 0, 0, 0, 0, "empty"],
        ["it", "sale",     "man", 0, 1, 0, 0, 0, 0, 0, 0, 1, "liver"],
        ["it", "founder",  "man", 0, 1, 1, 0, 0, 0, 0, 1, 0, "boss"],
        ["it", "phd",      "man", 1, 0, 0, 0, 0, 1, 0, 1, 0, "liver, fake hacker"],
        ["it", "engineer", "man", 0, 1, 0, 1, 1, 1, 1, 1, 0, "fake hacker"],
        ["it", "engineer", "man", 0, 0, 0, 0, 0, 1, 0, 1, 0, "fake hacker"],
        ["it", "engineer", "man", 0, 0, 0, 1, 1, 1, 1, 1, 0, "fake hacker"],
    ]
    labels = ["industry", "profession", "sex", "camera", "drive tour", 
            "SNS", "github", "over GFW", "reader", "Science fiction fan","hobby","brag"]
    return dataSet, labels

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # classify test, tortoise
        classmate = ["tortoise", "it", "engineer",       "man", 1, 0, 0, 0, 0, 1, 0, 1, 1]
        dataSet, labels = getTrainingDatas()
        tree = trees.grabTree("cm_tree.txt")
        print "{} is \"{}\"".format(classmate[0], trees.classify(tree, labels, classmate[1:]))
    else:
        # training
        dataSet, labels = getTrainingDatas()
        tree = trees.createTree(dataSet, list(labels))
        trees.storeTree(tree, "cm_tree.txt")
        treePlotter.createPlot(tree)