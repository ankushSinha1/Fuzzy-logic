import pandas as pd
def check_invalid_phone(val):
    if(pd.isna(val) or val is None):
        return False
    # Not len == 10 condition check
    elif(len(str(val).strip()) != 10):
        return True
    # Not numeric check
    elif(not str(val).strip().isdigit()):
        return True
    # Not starting with 6, 7, 8, or 9 check
    elif(str(val).strip()[0] not in ['6', '7', '8', '9']):
        return True
    else:
        return False