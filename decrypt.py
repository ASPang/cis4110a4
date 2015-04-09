#!/usr/bin/evn

###########################################
# Program: E-Voting with Paillier Encryption
# File Name: decrypt.py
#
# Authors: Maame Adwoa Bempomaa, Melissa Neubert, Angela Pang
# Date Created: 2015/04/08
#
# Description:
# 
###########################################
#from math import floor 
import math
import constantVar as const
   
#--- Tally Function ---#

#------------------------------------------   
# tallyVotes
#------------------------------------------
# Counts all the encrypted votes which is the 
# product of all encrypted votes modulo n^2
#------------------------------------------
def tallyVotes():
   print("Tallying votes")
   product = 1
   
   #Go through all the encrypted votes
   for val in const.encVotes:
      product *= val
   
   result = product % const.n2   
   print(result, " ", const.n2)
   decryptTally(result)

#--- Decrypt ---#
#------------------------------------------   
# decryptTally
#------------------------------------------
# Decrypts the tallied counted votes  
#------------------------------------------
# Parameters:
#  tally - The encrypted tally of votes
#
# Returns:
#  
#-------------------------------------------
def decryptTally(encTally):
   print("Decrypting tally result")
   
   divisor = 10
   numVote = 0 #Tempoarily stores the number of votes for one candidate
   decryptTally = ((encTally**const.lamda % const.n2 - 1) / const.n) * const.mew % const.n
   print(decryptTally, " ", const.n2)
   
   #Initialize array where all candiates currently have 0 votes
   tallyResult = [0 for i in range(const.nCandi)] 
      
   #Get the votes starting with the last listed candiate first
   for i in range(const.nCandi-1, -1, -1):
      tallyResult[i] = int(math.floor(decryptTally / divisor**i))
      decryptTally = decryptTally - (tallyResult[i] * divisor**i)
      print tallyResult, decryptTally
      
   return tallyResult
   