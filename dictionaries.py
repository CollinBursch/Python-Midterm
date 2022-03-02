# Dictionary = collection of key value pairs
# - Keys are always strings
# - Values can be whatever we want, even another dictionary. Dictionary inception!
# - Different values in a dictionary don't have to be the same type
dict = {"Carson": 23, "Collin": 21, "Grace": 19} # This dictionary holds names and ages, with names being the keys and ages being values

# ***Printing***
print('Dict Type:',type(dict)) # Type of dict
print(dict) # Print whole dictionary
for key in dict: # Print whole dictionary, fancy
    print('Key:', key, 'Value:', dict.get(key))

# ***Looking at values***
print(dict['Carson']) # You can use direct reference like this, 
# print(dict['Tommy']) # but this can cause errors if the key doesn't exist in the dictionary

print(dict.get('Carson')) # You can use indirect reference like this,
print(dict.get('Tommy')) # Now this won't throw an error but rather return None 


# ***Assigning***
dict['Becca'] = 22 # Add new key value pair to dictionary
dict['Grace'] = '16' # Changing a keys value, you can even change the value to another type1
print(dict)

# ***Deleting***
del dict['Becca'] # Delete the key from the dictionary
print(dict)
