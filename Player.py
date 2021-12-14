import numpy as np
from settings import * # NOQA




class Player:
    
    def __init__(self, name, starting_money):
        """
        Player stores the data of each player in the game
        
        pos: int position on the board
        doubles: int doubles rolled in a row
        money: int player's money
        turns_in_jail: int consecutive days in jail
        
        goj_ch: bool if player has GOOJF card from chance deck
        goj_co: bool if player has GOOJF card from community deck 
        inprison: bool if player is in jail
        bankrupt: bool is the player bankrupt
        
        properties: list logs the properties owned by the player 
        
        """
        self.name = name
        self.money = STARTING_MONEY
        self.pos = 0 
        self.doubles = 0 
        self.turns_in_jail = 0 
        
        self.goj_ch = False 
        self.goj_co = False
        self.inprison = False 
        self.bankrupt = False 
        
        self.properties = [] 

      
    def roll_dice(self):
        return [np.random.randint(1,6+1) for _ in range(2)]
    
    def add_money(self, amount):
        self.money += amount
    
    def take_money(self, amount):
        self.money -= amount
        
    def go_to_jail(self):
        self.pos = 10
        self.inprison = True 
        
    def move_player(self, dice_amount):
        self.pos += dice_amount
        
    def pass_go(self):
        self.pos -= 40
        self.add_money(GO)
        
    def check_bankrupcy(self):
        if self.money <= 0:
            self.bankrupt = True
            print(f"{self.name} is now bankrupt, has {self.money}.")
            return
        
        
    def turn(self, board):
        
        
        
        if self.bankrupt:
            print(f"{self.name} is bankrupt.")
            return
        
        dice = self.roll_dice()
        go_again = True
        
        while go_again:
        
            if dice[0] == dice[1] and self.inprison == False: #rolls a double                
                
                self.doubles += 1
                print(f"{self.name} rolls a double: {self.doubles} in a row")
                
                if self.doubles == 3: #if that's three in a row, go to jail
                    self.go_to_jail()
                    self.doubles = 0
                    print("Three doubles in a row, go to jail")
                    return
            else:
                self.doubles = 0 #no double, 
                go_again = False
                
            if self.inprison:
                if self.goj_ch:
                    self.goj_ch = False
                    go_again = False
                    board.chance_cards.append(1) #return chance to deck
                    print(f"{self.name} used get out of jail free card")
                
                elif self.goj_co:
                    self.goj_co = False
                    go_again = False
                    board.community_cards.append(1)
                    print(f"{self.name} used get out of jail free card")
                    
                
                elif dice[0] != dice[1]:
                    self.turns_in_jail += 1
                    if self.turns_in_jail < 3:
                        print(f"{self.name} stays in jail")
                        return #skip this turn, makes sure player doesn't get his jail status changed
                    else:
                        self.take_money(JAIL_FINE)
                        self.turns_in_jail = 0
                        go_again = False
                        print(f"{self.name} pays fine, get out of jail")
                
                else: #only other option is rolling a double
                    self.turns_in_jail = 0
                    go_again = False
                    print(f"{self.name} rolls a double, get out of jail")
            
            self.inprison = False #get out of prison
            
            self.move_player(dice[0] + dice[1]) #move player

            
            if self.pos >= 40: #check if player passes go
                self.pass_go()
                print(f"{self.name} passes go, collect {GO}")
            
            print(f"{self.name} moves to {self.pos}, rolling {dice[0]} and {dice[1]}")            
            
            board.action(self, self.pos) #act out the cell that the player has landed on
            self.check_bankrupcy()
        
        return
                
            
    
        
    





