from pprint import pprint
from collections import defaultdict
from lxml import etree
from prettytable import PrettyTable, ALL
from textwrap import fill
from math import log, floor
import sys
import os

def getDict(Fname):
	valuelist = []
	newDict = {}
	capture = 0
	newDictRouter = {}
	newDictNetwork = {}
	newDictSummary = {}
	newDictASBRSum = {}
	newDictOpaqArea = {}
	newDictExtern = {}
	try:
		with open(Fname) as fHandle:
			NewLst = fHandle.readlines()
	except:
		print("Incorrect File name sufficed, please check for correct file name")
		exit()	
	newlist1 = [s.replace("\n", "") for s in NewLst]
	newlist2 = []
	for items in newlist1:
		if "Area 0.0.0.0" in items or "OSPF AS SCOPE" in items or "show ospf database" in items:
			newlist1.remove(items)
		items = " ".join(items.split())
		newlist2.append(items)
	for items in newlist2:		
		if "Type" in items:
			newlist2.remove(items)
	newlist2.pop(0)
	for items in newlist2:
		if items.split(" ")[0] == "Router":
			newDictRouter[items.split(" ")[1]] = items.split(" ")[3]
		elif items.split(" ")[0] == "Network":
			newDictNetwork[items.split(" ")[1]] = items.split(" ")[3]
		elif items.split(" ")[0] == "Summary":
			newDictSummary[items.split(" ")[1]] = items.split(" ")[3]
		elif items.split(" ")[0] == "ASBRSum":
			newDictASBRSum[items.split(" ")[1]] = items.split(" ")[3]
		elif items.split(" ")[0] == "OpaqArea":
			newDictOpaqArea[items.split(" ")[1]] = items.split(" ")[3]
		elif items.split(" ")[0] == "Extern":
			newDictExtern[items.split(" ")[1]] = items.split(" ")[3]
	return newDictRouter, newDictNetwork, newDictSummary, newDictASBRSum, newDictOpaqArea, newDictExtern

def CompDB(Dict1, Dict2):
	newDict = {}
	RmvLst = []
	addLst = []
	for k,v in Dict1.items():
		if k in Dict2.keys():
			if Dict1[k] != Dict2[k]:
				newDict[k] = Dict1[k]+"--"+Dict2[k]
		else:
			RmvLst.append(k)
	for k,v in Dict2.items():
		if k not in Dict1.keys():
			addLst.append(k)
	return newDict,RmvLst,addLst

def IntConv(number):
    units = ['', 'K', 'M', 'G', 'T', 'P']
    k = 1000.0
    if number != 0:
    	magnitude = int(floor(log(number, k)))
    	return '%.2f%s' % (number / k**magnitude, units[magnitude])
    else:
    	return number

#MAIN METHOD
#=====================
if len(sys.argv) < 3:
	print("Enter atleast 2 files for comparision")
	exit()

r1DictRtr, r1DictNtw, r1DictSumm, r1DictASBRSum, r1DictOpq, r1DictExt = getDict(sys.argv[1])
r2DictRtr, r2DictNtw, r2DictSumm, r2DictASBRSum, r2DictOpq, r2DictExt = getDict(sys.argv[2])


print("=============================================================")
print("=                 OSPF RTR DB Seq # Change Diff             =")
print("=============================================================")

DiffRtr, RmvRtr, addRtr = CompDB(r1DictRtr,r2DictRtr)
pprint(DiffRtr)
print(len(r1DictRtr.keys()), len(r2DictRtr.keys()), len(DiffRtr.keys()))
a = input("")
pprint(RmvRtr)
pprint(addRtr)


print("=============================================================")
print("=                 OSPF Ntw DB Seq # Change Diff             =")
print("=============================================================")

DiffNtw, RmvNtw, addNtw = CompDB(r1DictNtw,r2DictNtw)
pprint(DiffNtw)
print(len(r1DictNtw.keys()), len(r2DictNtw.keys()), len(DiffNtw.keys()))
a = input("")
pprint(RmvNtw)
pprint(addNtw)


print("=============================================================")
print("=                 OSPF Summ DB Seq # Change Diff            =")
print("=============================================================")

DiffSumm, RmvSumm, addSumm = CompDB(r1DictSumm,r2DictSumm)
pprint(DiffSumm)
print(len(r1DictSumm.keys()), len(r2DictSumm.keys()), len(DiffSumm.keys()))
a = input("")
pprint(RmvSumm)
pprint(addSumm)


print("=============================================================")
print("=           OSPF ASBR summ DB Seq # Change Diff             =")
print("=============================================================")

DiffASBRsum, RmvASBRSum, addASBRSum = CompDB(r1DictASBRSum,r2DictASBRSum)
pprint(DiffASBRsum)
print(len(r1DictASBRSum.keys()), len(r2DictASBRSum.keys()), len(DiffASBRsum.keys()))
a = input("")
pprint(RmvASBRSum)
pprint(addASBRSum)


print("=============================================================")
print("=            OSPF Opq Area DB Seq # Change Diff             =")
print("=============================================================")

DiffOpq, RmvOpq, addOpq = CompDB(r1DictOpq,r2DictOpq)
pprint(DiffOpq)
print(len(r1DictOpq.keys()), len(r2DictOpq.keys()), len(DiffOpq.keys()))
a = input("")
pprint(RmvOpq)
pprint(addOpq)


print("=============================================================")
print("=             OSPF External DB Seq # Change Diff            =")
print("=============================================================")

DiffExt, RmvExt, addExt = CompDB(r1DictExt,r2DictExt)
pprint(DiffExt)
print(len(r1DictExt.keys()), len(r2DictExt.keys()), len(DiffExt.keys()))
a = input("")
pprint(RmvExt)
pprint(addExt)


