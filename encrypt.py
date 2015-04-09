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
#import Fraction
from fractions import gcd
import constantVar as const
import decrypt

#--- Encryption Functions ---#
#Encrypt the votes
def encrypt():
   print("Starting to encrypt")

def createVote():
   print("Creating a vote")

#Generate g value
def genG():
   g = genRamdom(3, const.n2)
   prime = gcd(g,const.n2)
   if (prime == 1):
      print("New g value is: ", g)
      return g
   else:
      genG()
      
#Generates a random number   
def genRamdom(a, b):
   num = random.randrange(a, b)
   #num = random.random()
   print("Random number = ", num)
   return num
   
#--- Math Functions ---#
def callLamda():
   print("Calculating Lamda")
   lamda = (const.p-1) * (const.q-1) / gcd(const.p-1,const.q-1)
   const.lamda = lamda
   
   print(const.lamda)
   return lamda

def calMew():   
   print("Calculating Mew")
   a = (const.g**const.lamda % const.n2 - 1) / const.n
   b = const.n
   mew = egcd(a, b)
   const.mew = mew[1]

   print(const.mew)
   return mew[1]

#------------------------------------------   
# checkPime
#------------------------------------------
# Checks to see if the number is prime   
#------------------------------------------
# Parameters:
#  num - The number 
#
# Returns:
#  1  - Number passed over is prime.
#  0  - Number checked is not prime.
#-------------------------------------------
# Code Snippet: http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
#
def checkPime(num):   
   print("Checking if number is prime")
   return all(num % i for i in xrange(2, num))

# Reference:https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
   if a == 0:
      return (b, 0, 1)
   else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b // a) * y, y)

# Reference: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm        
def modinv(a, m):
   gcd, x, y = egcd(a, m)
   if gcd != 1:
      return None  # modular inverse does not exist
   else:
      return x % m
        
#--- Main Function ---#
def main():
   print("--Main()--")
   
   genG()
   callLamda()
   calMew()
   
   decrypt.tallyVotes()
   
if __name__ == "__main__":
   main()