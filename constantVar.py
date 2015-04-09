#!/usr/bin/evn

###########################################
# Program: E-Voting with Paillier Encryption
# File Name: gVariables.py
#
# Authors: Maame Adwoa Bempomaa, Melissa Neubert, Angela Pang
# Date Created: 2015/04/08
#
# Description:
#  This file contains all the global variables in the program
###########################################


#--- (Constant) Global Variables ---#
nVoters = 9
nCandi = 5

p = 293
q = 433

n = p*q
n2 = n*n

#lamda = 31536
lamda = 0
g = 6497955158
#mew = 53022
mew = 0

base = 10

votes = [10, 10100, 0, 1000, 1001, 1010, 1100, 1010, 1]
encVotes = [13039287935, 848742150, 7185465039, 80933260, 722036441, 350667930, 4980449314, 7412822644, 3033281324]
tally = 0
