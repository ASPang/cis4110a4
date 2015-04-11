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
import encrypt
import math
import constantVar as const
   
   
############## Tally Function #############
#------------------------------------------   
# tallyVotes
#------------------------------------------
# Counts all the encrypted votes which is the 
# product of all encrypted votes modulo n^2
#------------------------------------------
def tallyVotes():
   print "---Tallying votes---"
   product = 1
   
   #Go through all the encrypted votes
   for val in const.encVotes:
      if (val != 0):
         product *= val
   
   result = product % const.n2   
   print(result, " ", const.n2)
   decryptTally(result)

################# Decrypt ################
#------------------------------------------   
# decryptTally
#------------------------------------------
# Decrypts the tallied counted votes  
#------------------------------------------
# Parameters:
#  encTally - The encrypted tally of votes
#
# Returns:
#  tallyResult - Tallied votes for each candidate
#-------------------------------------------
def decryptTally(encTally):
   print "---Decrypting tally result---"
   
   divisor = 10
   numVote = 0 #Tempoarily stores the number of votes for one candidate
   decryptTally = ((encTally**const.lamda % const.n2 - 1) / const.n) * const.mew % const.n
   print decryptTally, " ", const.n2
   
   #Initialize array where all candiates currently have 0 votes
   tallyResult = [0 for i in range(const.nCandi)] 
      
   #Get the votes starting with the last listed candiate first
   for i in range(const.nCandi-1, -1, -1):
      tallyResult[i] = int(math.floor(decryptTally / divisor**i))
      decryptTally = decryptTally - (tallyResult[i] * divisor**i)
      print tallyResult, decryptTally
      
   return tallyResult
   
#------------------------------------------   
# getAllEncVotes
#------------------------------------------
# Get all the encrypted votes in a file
#------------------------------------------
# Returns:
#  voteAry  - An array of all the encrypted votes
#-------------------------------------------
def getAllEncVotes():   
   print "---Getting encrypted votes on file---"
   
   #Get all encrypted votes on file
   with open('vote.txt') as voteFile:
      voteAry = voteFile.readlines()   
      
   #Convert the votes into an number
   const.encVotes = [0 for i in range(const.nVoters)]
   
   for i in range(len(voteAry)):
      const.encVotes[i] = int(voteAry[i])
      #print voteAry[i], " ", const.encVotes[i]
      
   #print voteAry, " ", len(voteAry), " ", const.encVotes, "\n"
   
   return voteAry
    
    
#--- Main Function ---#
def main():
   print("--Main()--")   
   
   encrypt.callLamda()
   encrypt.calMew()
   
   #Get all the encrypted votes stored
   getAllEncVotes()
   
   print const.encVotes
   
   #Tally all the votes
   tallyVotes()
   
   
if __name__ == "__main__":
   main()    
   