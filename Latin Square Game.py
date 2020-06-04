# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:05:48 2020

@author: samdw
"""

# Need to create clearly defined rules at some point.
# Basic idea: Two player game in which player one plays characters 1,2 or 3 followed by player two player a 1,2 or 3. Player one and 
# Player two must place moves in such as way as to not violate the Latin square property. 
# Player one wins if player one and two's moves lead to a latin square within the array. Player two wins if there is 
# no way to achive a latin square at some point during the game.

# To do list.
# Create a function to define to create an nxn board
# Possibly create a GUI (Tkinter Package....need to look into this)

import numpy as np
import  pandas as pd
import matplotlib as plt
import random as rd


board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])

def player_one(row,col,char):
    board[row][col] = char
    print(board)
    

def player_two(row,col,char):
    board[row][col] = char
    print(board)    
    
    
def Latin_Sq_Pop_Rows():
     for i in range(0,3):
         if board[i][0] != '-' and board[i][1] != '-' and board[i][2] == '-':
             temp = 3 - (int(board[i][0]) + int(board[i][1]))
             temp = str(temp)
             board[i][2] = temp
             print(board)
         if board[i][1] != '-' and board[i][2] != '-' and board[i][0] == '-':
             temp = 3 - (int(board[i][1]) + int(board[i][2]))
             temp = str(temp)
             board[i][0] = temp             
             print(board)
         if board[i][0] != '-' and board[i][2] != '-' and board[i][1] == '-':
             temp = 3 - (int(board[i][0]) + int(board[i][2]))
             temp = str(temp)
             board[i][1] = temp             
             print(board) 
 
    
# This is a cool capability but I think I need to omit for the game. The player blocking the Latin Square needs more options to work with. 
def Latin_Sq_Pop_Cols():
     for i in range(0,3):
         if board[0][i] != '-' and board[1][i] != '-' and board[2][i] == '-':
             temp = 3 - (int(board[0][i]) + int(board[1][i]))
             temp = str(temp)
             board[2][i] = temp
             print(board) 
         if board[1][i] != '-' and board[2][i] != '-' and board[0][i] == '-':
             temp = 3 - (int(board[1][i]) + int(board[2][i]))
             temp = str(temp)
             board[0][i] = temp             
             print(board) 
         if board[0][i] != '-' and board[2][i] != '-' and board[1][i] == '-':
             temp = 3 - (int(board[0][i]) + int(board[2][i]))
             temp = str(temp)
             board[1][i] = temp             
             print(board) 

             
          
                   
         
def invalid_move(row,col,char):
    if any(item == board[row][col] for item in ['0','1','2']):
        return True
    for j in range(0,3):
        if j != col and any(item == board[row][j] for item in ['0','1','2']) and str(char) == board[row][j]:
            return True
            break
    for i in range(0,3):
        if i != row and any(item == board[i][col] for item in ['0','1','2']) and str(char) == board[i][col]:
            return True
            break
    else:
        return False
 
def game_over():
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == '-':
                return False
                break
            elif board[i][j] != '-':
                continue
            else:
                return False
                break
    return True

def initialize_latin_square_game():
    while game_over() == False:
        row,col,char = map(int,input("Player one enter row, column, and number: "))
        while invalid_move(row,col,char) == True:
            row,col,char = map(int,input("Invalid move please re-enter row, column, and number: "))
        player_one(row,col,char)
        while Latin_Sq_Pop_Rows() == True:
            if Latin_Sq_Pop_Rows() == True:
                Latin_Sq_Pop_Rows()
                print(board)
            else:
                break
        while Latin_Sq_Pop_Cols() == True:
            if Latin_Sq_Pop_Cols() == True:
                Latin_Sq_Pop_Cols()
                print(board)
            else:
                break
        if game_over() == True:
            break
        row,col,char = map(int,input("Player two enter row, column, and number: "))
        while invalid_move(row,col,char) == True:
            row,col,char = map(int,input("Invalid move please re-enter row, column, and number: "))
        player_two(row,col,char)
        while Latin_Sq_Pop_Rows() == True:
            if Latin_Sq_Pop_Rows() == True:
                Latin_Sq_Pop_Rows()
                print(board)
            else:
                break
        while Latin_Sq_Pop_Cols() == True:
           if Latin_Sq_Pop_Cols() == True:
               Latin_Sq_Pop_Cols()
               print(board)
           else:
                break
        if game_over() == True:
            print("Game Over!")
            break                
    
 
initialize_latin_square_game()
         
            
         
            
         
            
         
            
         
            
         
