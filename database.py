#!/usr/bin/evn

###########################################
# Program: E-Voting with Paillier Encryption
# File Name: database.py
#
# Authors: Maame Adwoa Bempomaa, Melissa Neubert, Angela Pang
# Date Created: 2015/04/08
#
# Description:
# 
###########################################
import MySQLdb
      
#--- Main Function ---#
def main():


   db = MySQLdb.connect(host="localhost", # your host, usually localhost
                        user="root", # your username
                         passwd="", # your password
                         db="evotes") # name of the data base

   # you must create a Cursor object. It will let
   #  you execute all the queries you need
   cur = db.cursor() 

   # Use all the SQL you like
   cur.execute("SELECT * FROM evotes.voters")

   # print all the first cell of all the rows
   for row in cur.fetchall() :
       print row[0]
   
if __name__ == "__main__":
   main()