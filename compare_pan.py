import pandas as pd
import re
def compare_pan(val1, val2):
    # Empty PAN check
    if((pd.isna(val1) or len(str(val1).strip()) == 0)
        or (pd.isna(val2) or len(str(val2).strip()) == 0)):
        return False
    # Equal check
    elif(str(val1).strip() == str(val2).strip()):
        return True
    # Not equal check
    else:
        return False