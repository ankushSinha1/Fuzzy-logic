import pandas as pd

def compare_phone(val1, val2):
        # Blank check
        if(pd.isna(val1) or len(str(val1).strip()) == 0
           or pd.isna(val2) or len(str(val2).strip()) == 0):
            return False
        # Equal check
        elif(str(val1).strip() == str(val2).strip()):
            return True
        # Not equal check
        else:
            return False