##3 CH9 Classes - Labs

### Lab 9.11.1 Car Value (classes)
# class Car:
#     def __init__(self):
#         self.model_year = 0
#         # TODO: Declare purchase_price attribute
#         self.purchase_price= 0
#         self.current_value = 0
# #Given:
#     def calc_current_value(self, current_year):
#         depreciation_rate = 0.15
#         # Car depreciation formula
#         car_age = current_year - self.model_year
#         self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    
#     # TODO: Define print_info() method to output model_year, purchase_price, and current_value
#     def print_info(self):
#         print('Car\'s information:')
#         print(f'  Model year: {self.model_year}')
#         print(f'  Purchase price: ${self.purchase_price}')
#         print(f'  Current value: ${self.current_value}')

# #Given:
# if __name__ == "__main__":    
#     year = int(input()) 
#     price = int(input())
#     current_year = int(input())
    
#     my_car = Car()
#     my_car.model_year = year
#     my_car.purchase_price = price
#     my_car.calc_current_value(current_year)
#     my_car.print_info()



### Lab 9.12.1 Nutritional Information
# class FoodItem:
#     # TODO: Define constructor with parameters to initialize instance 
#     #       attributes (name, fat, carbs, protein)
#     def __init__(self, name='Water', fat=0, carbs=0, protein=0):
#         self.name = name
#         self.fat = fat
#         self.carbs = carbs
#         self.protein = protein
    
#     def get_calories(self, num_servings):
#         # Calorie formula
#         calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
#         return calories
       
#     def print_info(self):
#         print(f'Nutritional information per serving of {self.name}:')
#         print(f'  Fat: {self.fat:.2f} g')
#         print(f'  Carbohydrates: {self.carbs:.2f} g')
#         print(f'  Protein: {self.protein:.2f} g')

# if __name__ == "__main__":
       
#     item_name = input()
#     if item_name == 'Water' or item_name == 'water':
#         food_item = FoodItem()
#         food_item.print_info()
#         print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')                       
    
#     else:
#         amount_fat = float(input())
#         amount_carbs = float(input())
#         amount_protein = float(input())
#         num_servings = float(input())
        
#         food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
#         food_item.print_info()
#         print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
#         print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')



### Lab 9.13 Artists
##Input an artist name, birth and death year (-1 for present), title of artwork and its date.
#The program will spit out a result in an organized format.
# class Artist:
#     # TODO: Define constructor with parameters to initialize instance attributes
#     #       (name, birth_year, death_year)
#     def __init__(self, name='unknown', birth_year=-1, death_year=-1):
#         self.name = name
#         self.birth_year = birth_year
#         self.death_year = death_year

#     # TODO: Define print_info() method
#     def print_info(self):
#         if self.birth_year >= 0 and self.death_year >= 0:
#             print(f'Artist: {self.name} ({self.birth_year} to {self.death_year})')
#         elif self.birth_year >= 0 and self.death_year < 0:
#             print(f'Artist: {self.name} ({self.birth_year} to present)')
#         else:
#             print(f'Artist: {self.name} (unknown)')
      
# class Artwork:
#     # TODO: Define constructor with parameters to initialize instance attributes
#     #       (title, year_created, artist)
#     def __init__(self, title='unknown', year_created=-1, artist='unknown'):
#         self.title = title
#         self.year_created = year_created
#         self.artist = artist

#     # TODO: Define print_info() method
#     def print_info(self):
#         print(f'Title: {self.title}, {self.year_created}')

# if __name__ == "__main__":
#     user_artist_name = input()
#     user_birth_year = int(input())
#     user_death_year = int(input())
#     user_title = input()
#     user_year_created = int(input())

#     user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

#     new_artwork = Artwork(user_title, user_year_created, user_artist)
#     user_artist.print_info()
#     new_artwork.print_info()




###Lab 9.14 Compare two triangles

# class Triangle:   
#     def __init__(self):
#         self.base = 0
#         self.height = 0

#     def set_base(self, user_base):
#         self.base = user_base

#     def set_height(self, user_height):
#         self.height = user_height
   
#     def get_area(self):
#         area = 0.5 * self.base * self.height
#         return area
   
#     def print_info(self):
#         print(f'Base: {self.base:.2f}')
#         print(f'Height: {self.height:.2f}')
#         print(f'Area: {self.get_area():.2f}')

# if __name__ == "__main__":
#     triangle1 = Triangle()
#     triangle2 = Triangle()

#     # TODO: Read and set base and height for triangle1 (use set_base() and set_height())
#     set_base1 = float(input()) #These are the inputs
#     set_height1 = float(input())
#     triangle1.set_base(set_base1) #These assign input to the triangle1 object
#     triangle1.set_height(set_height1)
    
#     # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
#     set_base2 = float(input())
#     set_height2 = float(input())
#     triangle2.set_base(set_base2)
#     triangle2.set_height(set_height2)
      
#     print('Triangle with smaller area:')  
    
#     # TODO: Determine smaller triangle (use get_area())
#     #       and output smaller triangle's info (use print_info())
#     area1 = triangle1.get_area()
#     area2 = triangle2.get_area()
#     if area1 < area2:
#         #print('Triangle 1:') #zyBooks doesn't ask to identify which triangle, just its b and h.
#         triangle1.print_info()
#     elif area2 < area1:
#         #print('Triangle 2:')
#         triangle2.print_info()
#     else:
#         print('Both triangles have the same area')



###Lab 9.15 Get Team Win percentage
# class Team:
#     def __init__(self):
#         self.name = 'none'
#         self.wins = 0
#         self.losses = 0

#     # TODO: Define get_win_percentage()
#     def get_win_percentage(self):
#         return self.wins / (self.wins + self.losses)
        
    
#     # TODO: Define print_standing()
#     def print_standing(self):
#         print(f'Win percentage: {self.get_win_percentage():.2f}')
#         if self.get_win_percentage() >= .5:
#             print(f'Congratulations, Team {self.name} has a winning average!')
#         else:
#             print(f'Team {self.name} has a losing average.')


# if __name__ == "__main__":
#     team = Team()
   
#     user_name = input()
#     user_wins = int(input())
#     user_losses = int(input())
    
#     team.name = user_name
#     team.wins = user_wins
#     team.losses = user_losses
    
#     team.print_standing()


### Lab 9.1.6
class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    vending_machine = VendingMachine()
    # TODO: Purchase input number of drinks
    drinks = int(input())
    vending_machine.purchase(drinks)
    # TODO: Restock input number of bottles
    restock = int(input())
    vending_machine.restock(restock)
    # TODO: Report inventory
    vending_machine.report()