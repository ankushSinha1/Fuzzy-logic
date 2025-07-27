import pandas as pd
def check_invalid_ckyc(val):
    # Not len == 14 condition check
    if(pd.isna(val) or val is None):
        return False
    elif(len(str(val).strip()) != 16):
        return True
    # For checking 16 digit numeric format
    elif not str(val).strip()[:14].isdigit():
        return True
    else:
        return False