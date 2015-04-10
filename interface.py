#!/usr/bin/evn

###########################################
# Program: E-Voting with Paillier Encryption
# File Name: interface.py
#
# Authors: Maame Adwoa Bempomaa, Melissa Neubert, Angela Pang
# Date Created: 2015/04/08
#
# Description:
# 
###########################################
import constantVar as const
import encrypt
import decrypt
import sys

#--- Tally conversion ---#
#------------------------------------------   
# prepareTallyEncMsg
#------------------------------------------
# The function calculates prepares the user's tally message   
#------------------------------------------
# Parameters:
#  num - The number 
#
# Returns:
#  1  - Number passed over is prime.
#  0  - Number checked is not prime.
#-------------------------------------------
def prepareTallyEncMsg(tallyStr):
   sum = 0  #Stores all the user's voting result
   vote = 0 #stores a single vote result either 0 (no) or 1 (yes)
   
   #Go through the entire tally string to determine whom was voted
   for c in range(len(tallyStr)):
      vote = tallyStr[c]
      print(vote, " ", c, " ", sum, " ", const.base)
      if (int(vote) == 1):
         sum = sum + const.base**c
   
   print("tally message = ", sum)
   return sum
   

#--- User Input ---#
def getVote():
   prompt = True
   candidate = ""
   ans = ["1", "2", "3", "4", "5", "", " ", "\n"]
   
   while(prompt == True):
      #Prompt the user on whom they want to vote for
      print "The following candidates are running for this election: "
      print "\t 1) A"
      print "\t 2) B"
      print "\t 3) C"
      print "\t 4) D"
      print "\t 5) E"
      print "Note: Only one candidate can be selected. \n"
      
      print "Enter candidate coresponding number: "
      
      #Get user input
      sys.stdout.flush()
      candidate = raw_input("")
      
      #Check what user has inputed is a correct value
      for a in ans:
         if (a == candidate):
            #Double check if the user really wants to continue with the selectino
            if (checkVote(candidate)):
               #Yes the user has made their decision
               print "\nYou ballet has been casted. Thank you for voting!"
               prompt = False
               if (candidate != "" or len(candidate) > 0):
                  return const.base**(int(candidate)-1)
               else:
                  return 0
            else:
               #No user wants to reselect
               print "\nPlease re-enter your choice."
               prompt = True
               candidate = ""
               break
         elif(a == ans[len(ans)-1]):
            print "\n***Input wasn't accepted. Please enter the number beside the candidate's name you wish to vote for.***"
   return 0
   
   
#Double check with user if they want to continue with selection
def checkVote(candi):
   userInput = ""
   ans = ["y", "Y", "n", "N"]
   
   print "\nAre you sure you want to vote for candidate #", candi, "?"
   print "Please enter 'y' if you would like to continue with choice, or 'n' if you want to reselect."
   sys.stdout.flush()
   userInput = raw_input("")
   
   #Check what user has inputed is a correct value
   for a in ans:
      if (a == userInput):         
         #Check to see if the answer was yes or no
         if (userInput == "Y" or userInput == "y"):
            return True
         else:
            return False
      elif (a == ans[len(ans)-1]):
         #Re-prompt the user 
         print "\n***Input wasn't accepted. Please enter 'y' if you would like to continue with choice, or 'n' if you want to reselect.***"
         return checkVote(candi)
   

#Determine if the user can vote
def getVoterID():   
   prompt = 0
   candidate = ""
   ans = ["123456", "111", "222", "333", "444"]
   
   while(prompt < 3):
      #Prompt the user for their voter's ID
      print "Enter your voter's ID:"
      
      #Get user input
      sys.stdout.flush()
      candidate = raw_input("")
      
      #Check what user has inputed is a correct value
      for a in ans:
         if (a == candidate):
            #Voter is valididated
            print "\nYou have been verified.\n"
            prompt = 3
            return True
         elif(a == ans[len(ans)-1]):
            print "\nYou have entered an invalid voters ID please try again."
      prompt += 1

   print "Your have reached the max number of attempts."
   return False
   
#--- Main Function ---#
def main():
   print("--Main()--")
   
   encrypt.genG()
   encrypt.callLamda()
   encrypt.calMew()
   
   if (getVoterID()):
      const.votes[0] = getVote()
     
   
   # decrypt.tallyVotes()
   
if __name__ == "__main__":
   main()