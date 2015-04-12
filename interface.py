#!/usr/bin/evn

###########################################
# Program: E-Voting with Paillier Encryption
# File Name: interface.py
#
# Authors: Maame Apenteng, Melissa Neubert, Angela Pang
# Date Created: 2015/04/08
#
# Description:
#  This program provides the interface to the
#  simulation voting system. It allows the user
#  to authenticate him/herself.
#  Once the vote has been encrypted it will
#  record it to "vote.txt" file on the server.
###########################################
import constantVar as const
import encrypt
import decrypt
import sys
  

############### User Input ###############
#------------------------------------------   
# getVote
#------------------------------------------
# The function prompts the user to make a vote   
#------------------------------------------
# Returns:
#  The vote message which is number calculated
#-------------------------------------------
def getVote():
   prompt = True
   candidate = ""
   ans = ["1", "2", "3", "4", "5", "", " ", "\n"]  #Possible choices that the user can enter
   
   #Prompt to select one candidate
   while(prompt == True):
      #Prompt the user on whom they want to vote for
      print "The following candidates are running for this election: "
      print "\t 1) Alice"
      print "\t 2) Bob"
      print "\t 3) Charlie"
      print "\t 4) David"
      print "\t 5) Elliot"
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
    
#------------------------------------------   
# checkVote
#------------------------------------------
# Double check with user if they want to continue with selection
#------------------------------------------
# Parameters:
#  candi - The candidate number that was selected 
#
# Returns:
#  True  - The user wants to continue with their vote
#  False - User wants to make a different selection
#-------------------------------------------
def checkVote(candi):
   userInput = ""
   ans = ["y", "Y", "n", "N"] #Possible choices user can enter
   
   #Get the user input
   print "\nAre you sure you want to vote for candidate #", candi, "?"
   print "Please enter 'y' if you would like to continue with choice, or 'n' if you want to reselect."
   sys.stdout.flush()
   userInput = raw_input("")
   
   #Check what user has inputted is a correct value
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

#------------------------------------------   
# getVoterID
#------------------------------------------
# Determine if the user can vote
#------------------------------------------
# Parameters:
#  candi - The candidated number that was selected 
#
# Returns:
#  True  - The user is validated
#  False - Failed to validate user
#-------------------------------------------
def getVoterID():   
   prompt = 0
   candidate = ""
   ans = ["123", "111", "222", "333", "444", "555", "666", "777", "888"]   #List of possible voters
   
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

#------------------------------------------   
# saveEncVote
#------------------------------------------
# Save encrypted vote to file
#------------------------------------------
# Parameters:
#  encVote - Encrypted vote
#-------------------------------------------
def saveEncVote(encVote):
   with open("vote.txt", "a") as myfile:
      myfile.write(str(encVote))
      myfile.write("\n")

      
############### Main Function ###############
def main():
   #Calculate the lamda and mew used for private key
   encrypt.callLamda()
   encrypt.calMew()
   
   #Determine if the person can vote
   if (getVoterID()):
      vote = getVote()
      encVote = encrypt.encryptVote(vote)
      
      #Store the vote
      saveEncVote(encVote)
   
if __name__ == "__main__":
   main()