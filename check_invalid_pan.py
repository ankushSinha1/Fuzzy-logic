import pandas as pd
import re
def check_invalid_pan(val):
    # Empty check
    if(pd.isna(val) or val is None):
        return False
    if(len(str(val).strip()) != 10):
        return True
    # For checking AAAAA9999A format
    elif not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', str(val).strip()):
        return True
    # Val is valid
    else:
        return False