# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:21:35 2023

@author: joaquin
"""
import sys

class Execute_Command(object):
    def __init__(self, coll_list):
        print('\nyou entered: 1. execute command\n')
        run_commands(coll_list)
        
def run_commands(collection_list):
    flag = True
    print('----++++++-----++++++\n++++------+++++++-------\n-_-_-_-_-_-_-_-_-_-\n-_-_-_-_-_-_-_-_-_-_')
    print('WELCOME TO THE SECRECT CLASSIFIED NFT ANALYZIER:\n')
    while flag:
        user_choice = input('1. navigate to "x" collection\n2.\n3. back to main menu\n0. terminate\n\nenter response here $')
        user_choice = user_choice.strip()
        if user_choice in '1234':
            user_choice = int(user_choice)
            
            if user_choice == 1:
                navigate_to_collection(collection_list)
                
            elif user_choice == 2:
                pass
            
            elif user_choice == 3:
                print('\n-------------------\n----------------back to main menu')
                return
            
            elif user_choice == 0:
                print('terminated')
                sys.exit()
        
        
def navigate_to_collection(collection_list):
    user_coll = input('enter collection slug name $')
    user_coll = user_coll.strip()
    if user_coll in collection_list:
        print("1. number of nft's in collection: ", "insert name here")
        print("2. number of nft's for sale: ", "insert name here.")
        print()
        
        
        
    else:
        print('collection slug name - not found')
    
    
        
        
        