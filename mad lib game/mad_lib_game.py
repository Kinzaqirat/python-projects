# make a adventure  story by taking input from user

name= input("Enter a name: ")
adjective= input("Enter adjective like (amazing, horrify): ")
animal=input("Enter an animal name: ")
place=input("Enter a place nume: ")
verb=input("Enter a verb like (Run,jump,Eat,sing): ")
weapon = input("Enter a weapon name: ")
story = f"""
    One day, {name} went on a {adjective} adventure. 
    Along the way, they encountered a fierce {animal} in the middle of {place}. 
    With great courage, {name} decided to {verb} using a {weapon}.
    It was a thrilling experience that would be remembered forever!
    """
    
print("\n--- Your Adventure Story ---")
print(story)