#!/bin/python3

import math
import os
import random
import re
import sys



class Gene():
    def __init__(self, gene_health_tuple):
        self.gene = gene_health_tuple[0]
        self.health = gene_health_tuple[1]
        self.subsequent = None
        self.next = None






if __name__ == '__main__':
    n = int(input())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    s = int(input())

    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]


    # list of (gene, health) sorted by gene
    dna = sorted(list(zip(genes, health)))

    # init the root of the gene-health tree
    gene_tree = Gene(dna[0])

    # construct the gene-health tree
    # if this == prev then add up health
    # elif this starts with prev add right child with the right part of the string
    # else add left child with this

    for i in range(1, len(dna)):
        gn = dna[i]
        if gn ==




