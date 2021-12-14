
#define the cells for the board 

class Cell:
    
    def __init__(self, name):
        self.name = name
        self.group = "" #like brown, blue, station etc 
        
    def action(self, player):
        pass

class Property(Cell):
    
    def __init__(self, name, cost, base_rent, house_rent, house_price, group):
        self.name = name
        self.cost = cost #cost of buying, mortgaging gives half this
        self.base_rent = base_rent 
        self.house_rent = house_rent #tuple containing all rent prices
        self.house_price = house_price #cost of a house
        self.group = group #colour of property
        self.is_mortgaged = False 
        self.monopoly = False 
        self.houses = 0
        self.owner = ""
    
    
    def action(self, player, board):
        
        if self.owner == player:
            print("No rent")
        
        elif self.owner == "":
            player.take_money(self.cost)
            self.owner = player
            player.properties.append(board.b[player.pos])
            print(f"{player.name} now owns {self.name}")
        
        else:
            rent = board.calculate_rent(player.pos)
            self.owner.add_money(rent)
            player.take_money(rent)
            print(f"{player.name} pays {rent} in rent to {self.owner.name}")
        
        


class Community(Cell):
    
    def action(self, player, board):
        
        community_card = board.community_cards.pop(0)
        
        if community_card == 1: #get out of jail card
            player.goj_co = True
            print("Get out of jail card")
       
        elif community_card == 2: #bank pays you £50
            player.add_money(50)
            print("Collect tax")
            
        if community_card != 1: #if it's not GoJ
            board.community_cards.append(community_card)
    
 
    
class Chance(Cell):
    
    def action(self, player, board):
        
        chance_card = board.chance_cards.pop(0)
        
        if chance_card == 1: #get out of jail card
            player.goj_ch = True
            print("Get out of jail card")
        
        elif chance_card == 2: #bank pays you £50
            player.add_money(50)
            print("Collect tax")
        
        if chance_card != 1: #if it's not GoJ
            board.chance_cards.append(chance_card)

    
    
    
class Tax(Cell):
    
    def __init__(self, name, tax):
        self.name = name
        self.group = "Tax"
        self.tax = tax
        
    def action(self, player):
        player.take_money(self.tax)
        print(f"Player {player.name} pays {self.tax} in tax")


class GoToJail(Cell):
    
    def action(self, player):
        player.go_to_jail()
        print(f"{player.name} goes to jail")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    