# Sammaches

sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'peanut butter', 'turkey', 'pastrami', 'roast beef', 'ham']
finished_sandwiches = []

print("\nWe've run out of Pastrami! Please remove all Pastrami orders!")

while sandwich_orders:
    if "pastrami" in sandwich_orders:
        sandwich_orders.remove('pastrami')
        
    current_sandwich = sandwich_orders.pop()

    print("\nCurrently making a " + current_sandwich.title() + " sandwich.")
    finished_sandwiches.append(current_sandwich)


# Sandwich orders completed
print("\nThe following sandwiches are completed: ")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())
                   
          
                   
