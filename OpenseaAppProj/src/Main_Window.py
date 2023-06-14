# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:18:42 2023

@author: joaquin
"""
from Execute_Command import Execute_Command
from Update_Database import Update_Database

class Main_Window(object):
    def __init__(self):
        self.custom = True

    def execute():
        # print('executing Main Window...\n\n')
        program_runnning = True
        collection_list = set()
        while program_runnning:
            user_choice = input('1. execute command\n2. update data\n0. the end\n\nenter response here $')
            user_choice = user_choice.strip()
            if user_choice == '1' or user_choice == '2' or user_choice == '3':
                user_choice = int(user_choice)
                
                # END
                if user_choice == 0:
                    program_runnning = False
                
                
                elif user_choice == 1:
                    Execute_Command(collection_list)
                    
                    
                elif user_choice == 2:
                    Update_Database()
                    
                elif user_choice == 3:
                    # Find collection stats
                    pass
                
                elif user_choice == 4:
                    # compare collections stats to each other
                    pass
                
                elif user_choice == 5:
                    # see/compare graph diagrams
                    pass
                
                elif user_choice == 6:
                    # see the delta's of a paticular list (i.e. alien nft's, famous people nft's, pokemon nft's, gamming, pfp nft's, memberships, trendings...) 
                    pass
                    
                elif user_choice == 7:
                    # see upcoming high potentional nft's to mint
                    pass
                
                elif user_choice == 8:
                    # see trending NFT's on opensea using web scraping
                    pass
                
                elif user_choice == 9:
                    # add/remove/search database
                    pass
                
                elif user_choice == 10:
                    # compare collection stats to database
                    pass
                    
            else:
                print('Error: please enter 1, 2 or 3\n')
                
    
   

    



