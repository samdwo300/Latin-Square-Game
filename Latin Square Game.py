# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:05:48 2020

@author: samdw
"""
import numpy as np
import  pandas as pd
import matplotlib as plt
import random as rd


board

def player_one(ro,col,char):
    board[row][col] = char
    print(board)
    

def player_two(ro,col,char):
    board[row][col] = char
    print(board)    
    
    
def Latin_Sq_Prop_Rows():
     for i in range(0,3):
         if board[i][0] != '-' and board[i][1] != '-':
             temp = 3 - (int(board[i][0]) - int(board[i][1]))
             temp = str(temp)
             board[i][2] = temp
             return True
             print(board)
             break
         if board[i][1] != '-' and board[i][2] != '-':
             temp = 3 - (int(board[i][1]) - int(board[i][2]))
             temp = str(temp)
             board[i][0] = temp             
             return True
             print(board)
             break
         if board[i][0] != '-' and board[i][2] != '-':
             temp = 3 - (int(board[i][0]) - int(board[i][2]))
             temp = str(temp)
             board[i][1] = temp             
             return True
             print(board)
             break
      else:
        return False

def Latin_Sq_Prop_Cols():
     for i in range(0,3):
         if board[0][i] != '-' and board[1][i] != '-':
             temp = 3 - (int(board[i][0]) - int(board[i][1]))
             temp = str(temp)
             board[2][i] = temp
             return True
             print(board)
             break
         if board[1][i] != '-' and board[2][i] != '-':
             temp = 3 - (int(board[1][i]) - int(board[2][i]))
             temp = str(temp)
             board[0][i] = temp             
             return True
             print(board)
             break
         if board[0][i] != '-' and board[2][i] != '-':
             temp = 3 - (int(board[0][i]) - int(board[2][i]))
             temp = str(temp)
             board[1][i] = temp             
             return True
             print(board)
             break
      else:
        return False
          
                   
         
def invalid_move(row,col,char):
    if any(item -- board[row][col] for item in ['0','1','2']):
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
            elif break[i][j] != '-':
                continue
            else:
                return False
            break
    return True

def initialize_latin_square_game():
    while game_over() == False:
        row,col,char = map(int,input("Player one enter row col number: "))
        while invalid_move(row,col,char) == True:
            row,col,char = map(int,input("Player one enter row col number: "))
        player_one(row,col,char)
        while Latin_Sq_Prop_Rows == True:
            Latin_Sq_Prop_Rows
        while Latin_Sq_Prop_Rows == True:
            Latin_Sq_Prop_Rows
        if game_over() == True:
            break
        row,col,char = map(int,input("Player one enter row col number: "))
        while invalid_move(row,col,char) == True:
            row,col,char = map(int,input("Player one enter row col number: "))
        player_one(row,col,char)
        while Latin_Sq_Prop_Rows == True:
            Latin_Sq_Prop_Rows
        while Latin_Sq_Prop_Rows == True:
            Latin_Sq_Prop_Rows
        if game_over() == True:
            break                
    
    
    
    
            
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         