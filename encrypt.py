#!/usr/bin/evn

###########################################
# Program: E-Voting with Paillier Encryption
# File Name: encrypt.py
#
# Authors: Maame Adwoa Bempomaa, Melissa Neubert, Angela Pang
# Date Created: 2015/04/08
#
# Description:
# 
###########################################
import random
from fractions import gcd
import constantVar as const
import decrypt


############# Tally conversion ############
#------------------------------------------   
# prepareTallyEncMsg
#------------------------------------------
# The function calculates prepares the user's tally message   
#------------------------------------------
# Parameters:
#  tallyStr - The tally string value
#
# Returns:
#  sum   - Returns the product of all the votes
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
   
########### Encryption Functions ###########
#------------------------------------------   
# encryptVote
#------------------------------------------
# Encrypts the votes   
#------------------------------------------
# Parameters:
#  vote - The unencrypted vote message value
#
# Returns:
#  encMsg   - Returns the encrypted vote value
#-------------------------------------------
def encryptVote(vote):
   print "---Starting to encrypt---"
   #Generate a r value that is element of n
   r = genR()

   #Encrypt the vote message
   encMsg = const.g**vote * r**const.n % const.n2
   
   print "g = ", const.g, " r = ", r, " vote = ", vote, " encryped message = ", encMsg
   return encMsg

#------------------------------------------   
# encryptVote
#------------------------------------------
# Generate r value used to encrypt the vote
#------------------------------------------
# Returns:
#  r   - Returns a r value that is element of n
#-------------------------------------------   
def genR():
   r = genRamdom(3, const.n - 1)
   return r
   
#------------------------------------------   
# encryptVote
#------------------------------------------
# Generate g value
#------------------------------------------
# Returns:
#  r   - Returns a r value that is element of n
#-------------------------------------------   
def genG():
   #Generate a g value that is an element of n^2
   g = genRamdom(3, const.n2)
   
   #Determine if the number generated is prime
   prime = gcd(g,const.n2)
   
   if (prime == 1):
      #Return new g value
      return g
   else:
      #If not prime generate a different number
      genG()
      
#------------------------------------------   
# genRamdom
#------------------------------------------
# Generates a random number   
#------------------------------------------
# Parameters:
#  a  - The minimum value
#  b  - The maximum value
#
# Returns:
#  r   - Returns a r value that is element of n
#-------------------------------------------  
def genRamdom(a, b):
   num = random.randrange(a, b)
   #print("Random number = ", num)
   return num
   
############# Math Functions #############
#------------------------------------------   
# callLamda
#------------------------------------------
# Calculate the lamda value using Carmichael's function   
#------------------------------------------
# Returns:
#  lamda   - Returns the lamda calculated
#-------------------------------------------  
def callLamda():
   print "---Calculating Lamda---"
   lamda = (const.p-1) * (const.q-1) / gcd(const.p-1,const.q-1)
   const.lamda = lamda
   
   print "Lamda value = ", const.lamda, "\n"
   return lamda

#------------------------------------------   
# calMew
#------------------------------------------
# Calculate the mew value that is used in private key decryption
#------------------------------------------
# Returns:
#  mew   - Returns the mew value
#-------------------------------------------  
def calMew():   
   print "---Calculating Mew---"
   a = (const.g**const.lamda % const.n2 - 1) / const.n
   b = const.n
   mew = egcd(a, b)
   const.mew = mew[1]

   print "Mew value = ", const.mew, "\n"
   return mew[1]

#------------------------------------------   
# checkPime
#------------------------------------------
# Checks to see if the number is prime   
#------------------------------------------
# Code Snippet Reference: 
#  http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
#------------------------------------------
# Parameters:
#  num - The number that is to be checked if it's prime
#
# Returns:
#  1  - Number passed over is prime.
#  0  - Number checked is not prime.
#-------------------------------------------
def checkPime(num):   
   print "---Checking if number is prime---"
   return all(num % i for i in xrange(2, num))

#------------------------------------------   
# egcd
#------------------------------------------
# Calculates the modulus inverse given two different values 
#------------------------------------------
# Code Reference: 
#  Reference:https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
#------------------------------------------
# Parameters:
#  a  - First value in the modulus inverse
#  b  - Second value in the modulus inverse
#
# Returns:
#  
#-------------------------------------------
def egcd(a, b):
   if a == 0:
      return (b, 0, 1)
   else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b // a) * y, y)

#------------------------------------------   
# modinv
#------------------------------------------
# Calculates the modulus inverse given two different values
#------------------------------------------
# Code Reference: 
#  Reference:https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
#------------------------------------------
# Parameters:
#  a  - First value in the modulus inverse
#  b  - Second value in the modulus inverse
#
# Returns:
#  
#-------------------------------------------
# def modinv(a, m):
   # gcd, x, y = egcd(a, m)
   # if gcd != 1:
      # return None  # modular inverse does not exist
   # else:
      # return x % m
        
#--- Main Function ---#
def main():
   print "Please run interface.py program to cast a vote which will be encrypted."
   
if __name__ == "__main__":
   main()