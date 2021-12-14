import random
from Cells import Cell, Property, Tax, Community, Chance, GoToJail



class Board:
    
    def __init__(self, players):
        
        """
        Board is a data for plots
        name: does not really matter, just convenience
        base_cost: used when buying plot, mortgage
        base_rent: used for rent and monopoly rent
         (for utilities and rail - in calculateRent method)
        house_cost: price of one house (or a hotel)
        house_rent: list of rent price with 1,2,3,4 houses and a hotel
        group: used to determine monopoly
        """

        # I know it is messy, but I need this for players to pay each other
        self.players = players

        self.b = []
        # 0-4
        self.b.append(Cell("Go"))
        self.b.append(Property("A1 Mediterraneal Avenue", 60,
                               2, 50, (10, 30, 90, 160, 250), "brown"))
        self.b.append(Community("Community Chest"))
        self.b.append(Property("A2 Baltic Avenue", 60, 4,
                               50, (20, 60, 180, 320, 450), "brown"))
        self.b.append(Tax("Property Tax", 200)) #changed from the GitHub repo
        # 5-9
        self.b.append(Property("R1 Reading railroad",
                               200, 0, 0, (0, 0, 0, 0, 0), "rail"))
        self.b.append(Property("B1 Oriental Avenue", 100, 6,
                               50, (30, 90, 270, 400, 550), "lightblue"))
        self.b.append(Chance("Chance"))
        self.b.append(Property("B2 Vermont Avenue", 100, 6, 50,
                               (30, 90, 270, 400, 550), "lightblue"))
        self.b.append(Property("B3 Connecticut Avenue", 120, 8,
                               50, (40, 100, 300, 450, 600), "lightblue"))
        # 10-14
        self.b.append(Cell("Prison"))
        self.b.append(Property("C1 St.Charle's Place", 140, 10,
                               100, (50, 150, 450, 625, 750), "pink"))
        self.b.append(Property("U1 Electric Company",
                               150, 0, 0, (0, 0, 0, 0, 0), "util"))
        self.b.append(Property("C2 States Avenue", 140, 10,
                               100, (50, 150, 450, 625, 750), "pink"))
        self.b.append(Property("C3 Virginia Avenue", 160, 12,
                               100, (60, 180, 500, 700, 900), "pink"))
        # 15-19
        self.b.append(Property("R2 Pennsylvania Railroad",
                               200, 0, 0, (0, 0, 0, 0, 0), "rail"))
        self.b.append(Property("D1 St.James Place", 180, 14,
                               100, (70, 200, 550, 700, 950), "orange"))
        self.b.append(Community("Community Chest"))
        self.b.append(Property("D2 Tennessee Avenue", 180, 14,
                               100, (70, 200, 550, 700, 950), "orange"))
        self.b.append(Property("D3 New York Avenue", 200, 16,
                               100, (80, 220, 600, 800, 1000), "orange"))
        # 20-24
        self.b.append(Cell("Free Parking"))
        self.b.append(Property("E1 Kentucky Avenue", 220, 18,
                               150, (90, 250, 700, 875, 1050), "red"))
        self.b.append(Chance("Chance"))
        self.b.append(Property("E2 Indiana Avenue", 220, 18,
                               150, (90, 250, 700, 875, 1050), "red"))
        self.b.append(Property("E3 Illinois Avenue", 240, 20,
                               150, (100, 300, 750, 925, 1100), "red"))
        # 25-29
        self.b.append(Property("R3 BnO Railroad", 200,
                               0, 0, (0, 0, 0, 0, 0), "rail"))
        self.b.append(Property("F1 Atlantic Avenue", 260, 22,
                               150, (110, 330, 800, 975, 1150), "yellow"))
        self.b.append(Property("F2 Ventinor Avenue", 260, 22,
                               150, (110, 330, 800, 975, 1150), "yellow"))
        self.b.append(Property("U2 Waterworks", 150,
                               0, 0, (0, 0, 0, 0, 0), "util"))
        self.b.append(Property("F3 Martin Gardens", 280, 24, 150,
                               (120, 360, 850, 1025, 1200), "yellow"))
        # 30-34
        self.b.append(GoToJail("Go To Jail"))
        self.b.append(Property("G1 Pacific Avenue", 300, 26,
                               200, (130, 390, 900, 1100, 1275), "green"))
        self.b.append(Property("G2 North Carolina Avenue", 300,
                               26, 200, (130, 390, 900, 1100, 1275), "green"))
        self.b.append(Community("Community Chest"))
        self.b.append(Property("G3 Pennsylvania Avenue", 320, 28,
                               200, (150, 450, 100, 1200, 1400), "green"))
        # 35-39
        self.b.append(Property("R4 Short Line", 200,
                               0, 0, (0, 0, 0, 0, 0), "rail"))
        self.b.append(Chance("Chance"))
        self.b.append(Property("H1 Park Place", 350, 35, 200,
                               (175, 500, 1100, 1300, 1500), "indigo"))
        self.b.append(Tax("Luxury Tax", 100)) #changed from the GitHub repo
        self.b.append(Property("H2 Boardwalk", 400, 50, 200,
                               (200, 600, 1400, 1700, 2000), "indigo"))
        
        
        self.chance_cards = [i for i in range(2)] #this will be 16 in the real version of the game
        random.shuffle(self.chance_cards)

        # Community Chest
        self.community_cards = [i for i in range(2)]
        random.shuffle(self.community_cards)
    
    
    
    def calculate_rent(self, position, special=""):
        if type(self.b[position]) == Property:
            rent = 0

            # utility
            if self.b[position].group == "util":
                if self.b[position].monopoly or special == "from_chance":
                    rent = (random.randint(1, 6)+random.randint(1, 6)) * 10
                else:
                    rent = (random.randint(1, 6)+random.randint(1, 6)) * 4

            # rail
            elif self.b[position].group == "rail":
                #rails = self.countRails(position)
                rent = 0 #if rails == 0 else 25 * 2**(rails) COME BACK TO THIS LATER
                #if special == "from_chance":
                    #rent *= 2 not quite sure how this bit works yet 

            # usual property
            else:
                if self.b[position].houses > 0:
                    if self.b[position].houses-1 > 5:
                        print(self.b[position].houses-1)
                        print(position)
                        self.printMap()
                    rent = self.b[position].house_rent[self.b[position].houses-1]
                elif self.b[position].monopoly:
                    rent = 2*self.b[position].base_rent
                else:
                    rent = self.b[position].base_rent
        else:  # not a Property
            rent = 0
        return rent
        
    
    
    def action(self, player, position, special = ""):
        

        # Landed on a property - calculate rent first
        if type(self.b[position]) == Property:
            # pass action to to the cell
            self.b[position].action(player, self)
        # landed on a chance, pass board, to track the chance cards
        elif type(self.b[position]) == Chance or type(self.b[position]) == Community:
            self.b[position].action(player, self)
        elif type(self.b[position]) == Tax:
            self.b[position].action(player)
        # other cells
        else:
            self.b[position].action(player)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    