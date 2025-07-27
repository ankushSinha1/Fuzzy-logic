from clean_address import CleanAddress
def compare_address(val1, val2):
    address1 = CleanAddress(val1).clean_address()
    address2 = CleanAddress(val2).clean_address()
    if(address1 == '' or address2 == ''):
        return False
    # Equal check
    # Add fuzzy logic
    elif(address1 == address2):
        return True
    # Not equal check
    else:
        return False