#!/usr/bin/evn

###########################################
# Program: E-Voting with Paillier Encryption
# File Name: constantVar.py
#
# Authors: Maame Apenteng, Melissa Neubert, Angela Pang
# Date Created: 2015/04/08
#
# Description:
#  This file contains all the global variables in the program
###########################################


############### (Constant) Global Variables ###############
nVoters = 9
nCandi = 5

base = 10

p = 293
q = 433

n = p*q
n2 = n*n

lamda = 0
g = 6497955158
mew = 0

votes = []
encVotes = []
tally = 0
