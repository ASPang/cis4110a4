-----------------------
INTRODUCTION
-----------------------
The following README is for the e-voting simulation system through the Homomorphic Tallying with Paillier Cryptosystem. It allows the user to vote for one of five party members.

The system will display steps it took to encrypt and decrypt voting results.

-----------------------
HOW TO SUBMIT VOTE
-----------------------

RUN:
> python interface.py

The system will prompt you for one of nine voting IDs which can be any of the following listed:
123
111
222
333
444
555
666
777
888

Once the system accepts you, follow the prompts and the votes. At the end the vote will be encrypted and stored in the "vote.txt" file.

----------------------------
HOW TO DECRYPT VOTE TALLY
----------------------------

RUN:
> python decrypt.py

The program will then display the steps it took to calculate the tally result and display the finally distribution of votes.

