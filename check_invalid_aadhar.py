import pandas as pd
def check_invalid_aadhar(val):
    # Not len == 12 condition check
    if(pd.isna(val) or val is None):
        return False
    elif(len(str(val).strip()) != 12):
        return True
    # Not numeric check
    elif(not str(val).strip().isdigit()):
        return True
    # Val is valid
    else:
        return False