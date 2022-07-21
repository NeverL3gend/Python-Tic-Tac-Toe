#### 
# This is going to be the start of my first project
# 
# Plan:
# 
# Greet the players that are playing. 
#
# I want to have a Heads or Tales logic to determine who goes first 
#
# I want the following table to look like this:
# 
# _|_|_
# _|_|_
#  | |
# 
# How I think this should work is that each spot are going to be put in a list
# first row = [0,1,2]
# Second row =[3,4,5]
# Third row = [6,7,8]
# 
# From there we will have a logic that will determine the winner
# 
# Winning logic 
#  Straight across: [0,1,2] , [3,4,5] , [6,7,8]
#  Diagonal: [0,4,8] , [2,4,6]
#  Vertical: [0,3,6] , [1,4,7] , [2,5,8]
# ####
import random

#Greating the players
print ("Welcome to Tic Tac Toe!")

#heads or tail logic
coinflip = ['heads', 'tails']
question = input("Choose Heads or Tails to see who goes first! -> ")
result = random.choice(coinflip)
print (result)

#coin Flip winner:

#player chooses if they want to be X or O