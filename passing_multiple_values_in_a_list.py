#practice and reusable code
original_list=[]

def aplhabetize(original_list=[]):
    """ Pass any list in square brackets, displays a string with items sorted """
# Inside the function make a working copy of the list passed in.
sorted_list = original_list.copy()
# Sort the working copy.
sorted_list.sort()
#make a new empty string for output
final_list = ''
#Loop through sorted list and append name and comma and space.
for name in sorted_list:
    final_list += name + ", "
    #Knock of last comma space if final list is long enough
    final_list = final_list[:-2]
    #print the alphabetized list.
print(final_list)

names = ['Jennifer', "Louis", "Gertude", "Shani",'Rain']
print(names)
aplhabetize(names)
print(names)

#another way of performing the same action
