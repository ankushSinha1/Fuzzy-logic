import re
import pandas as pd
from compare_name import compare_name
from compare_address import compare_address
from compare_phone import compare_phone
from compare_pan import compare_pan 
from compare_aadhar import compare_aadhar
from compare_ckyc import compare_ckyc
rules_df = pd.read_csv('rules.csv')
# print(rules_df.info())

class CanBeConsidered():
    record1, record2 = None, None
    masking_array = [False, False, False, False, False, False]  # Name, Address, Phone Number, PAN, Aadhar, CKYC
    def __init__(self, record1, record2):
        self.record1 = record1
        self.record2 = record2

    def comparison(self):
        # check name
        if compare_name(self.record1['fip_ct_name'], self.record2['fip_ct_name']):
            self.masking_array[0] = True
        else:
            self.masking_array[0] = False

        # check address
        if compare_address(self.record1['fip_ct_address_1'], self.record2['fip_ct_address_1']):
            self.masking_array[1] = True
        
        else:
            self.masking_array[1] = False

        # check phone number
        if compare_phone(self.record1['fip_ct_mobile_primary'], self.record2['fip_ct_mobile_primary']):
            self.masking_array[2] = True

        else:
            self.masking_array[2] = False

        # check PAN
        if compare_pan(self.record1['fip_ct_pan_no'], self.record2['fip_ct_pan_no']):
            self.masking_array[3] = True
        else:
            self.masking_array[3] = False

        # check Aadhar
        if compare_aadhar(self.record1['fip_ct_aadhar'], self.record2['fip_ct_aadhar']):
            self.masking_array[4] = True
        else:
            self.masking_array[4] = False

        # check CKYC
        if compare_ckyc(self.record1['fip_ct_kyc'], self.record2['fip_ct_kyc']):
            self.masking_array[5] = True
        else:
            self.masking_array[5] = False

        return self.check_value_from_rules()
        # Read from rules_df which row it aligns with
    
    def check_value_from_rules(self):
        # check from masking_array whether to consider as same or not
         # Convert bools to 1/0
        
        bit_vector = [1 if mask==True else 0 for mask in self.masking_array]
        # print(bit_vector)
        
        # Column names for comparison (exclude 'Sno' and 'as per rule')
        cols_to_check = ['Name', 'Address', 'Mobile', 'Pan', 'Adhaar', 'CKYC']
        rules_df[cols_to_check] = rules_df[cols_to_check].replace({'same': 1, ' same': 1, 'Diff': 0, ' Diff': 0}).astype(int)
        
        # Create a mask by checking each column in rules_df against bit_vector
        mask = (rules_df[cols_to_check].values == bit_vector).all(axis=1)
        
        # Get the matching rule row
        matched_rule = rules_df[mask]
        # print(matched_rule)
        return matched_rule.iloc[0].to_dict()
