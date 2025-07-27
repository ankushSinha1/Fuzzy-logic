from clean_name import CleanName
def compare_name(val1, val2):
    # cleaning both the names
    name1 = CleanName(val1).clean_name()
    name2 = CleanName(val2).clean_name()
    # Empty check
    if(name1 == '' or name2 == ''):
        return False
    # Equal check
    # Add fuzzy logic
    elif(name1 == name2):
        return True
    # Not equal check
    else:
        return False
    

