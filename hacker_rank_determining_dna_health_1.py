#!/bin/python3

import math
import os
import random
import re
import sys

def match(a, b):
    if len(a)!=len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i]!=b[i]:
                return False
        return True

def dna_health(genes, health, first, last, d):
    total = 0
    for i in range(first, last+1):
        gene = genes[i]
        if len(gene)<=len(d):
            for j in range(len(d)-len(gene)+1):
                if match(gene, d[j:j+len(gene)]):
                    total += health[i]
    return total

if __name__ == '__main__':
    n = int(input())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    s = int(input())

    h_min = 100000000000000
    h_max = 0

    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]
        
        t = dna_health(genes, health, first, last, d)
        if t < h_min:
            h_min = t
        if t > h_max:
            h_max = t
    
    print (h_min, h_max)