# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.
master_class_list =  {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'], 'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(master_class_list): 
    max_count = 0
    most_busy_teacher = ''
    for teacher in master_class_list:
        classes = master_class_list[teacher]
        if len(classes) > max_count:
            max_count = len(classes)
            most_busy_teacher = teacher
    print(most_busy_teacher)
    print(max_count)
    return most_busy_teacher

def num_teachers(dict): 
    count = 0
    for teacher in dict:  # <-- changed to dict
        count +=1 
    print(count)
    return count
  
def stats(dict):
    theList = [] 
    for key in dict: 
        theList.append([key, len(dict[key])])
    return theList
  
def courses(master_class_list):
  class_list = []
  for value in master_class_list.values():
    class_list.append(value)
    print(class_list)
  return class_list
    
    
    
courses(master_class_list)
