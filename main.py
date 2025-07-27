import pandas as pd
from Can_Be_Considered import CanBeConsidered
from clean_address import CleanAddress
from clean_name import CleanName
from check_invalid_aadhar import check_invalid_aadhar
from check_invalid_pan import check_invalid_pan
from check_invalid_phone import check_invalid_phone
from check_invalid_ckyc import check_invalid_ckyc

# customer_id_generator.py

customer_id_counter = 1  # Global counter for generating IDs


def generate_customer_id(prefix="CUST20250727", width=6):
    global customer_id_counter
    customer_id = f"{prefix}{str(customer_id_counter).zfill(width)}"
    customer_id_counter += 1
    return customer_id

df = pd.read_csv('Customer id created sample data.csv')

# Code for creating block mapping
invalid_data = []
block_map = {}
for idx, record in df.iterrows():
    if check_invalid_aadhar(record['fip_ct_aadhar']) or \
       check_invalid_pan(record['fip_ct_pan_no']) or \
       check_invalid_phone(record['fip_ct_mobile_primary']) or \
       check_invalid_ckyc(record['fip_ct_kyc']):
        invalid_data.append(record)
    else:
        name = CleanName(record['fip_ct_name']).clean_name()
        phone = record['fip_ct_mobile_primary']
        block_key = name[:3] + str(phone)[:5]  # Using first 3 chars of name and 5 for phone for block key

        if block_key not in block_map:
            block_map[block_key] = []
        block_map[block_key].append(record)

for block_key, records in block_map.items():
    # print(f"Block Key: {block_key}" + f" - Number of Records: {len(records)}")
    if(len(block_map[block_key]) > 1):
        for i in range(len(records)):
            found_match = False
            for j in range(i + 1, len(records)):
                comparator_test = CanBeConsidered(records[i], records[j]).comparison()
                if(comparator_test['as per rule '] == 'to be considered'):
                    found_match = True
                    # logic to push jth records in new_csv
                    # cust_id = current if found_match is True; else next_id
                print(comparator_test)
            # logic to push ith record in new_csv
            # if found_match:
                # same cust_id
            # else:
                # new cust_id
    # else:
        # logic to push records as not to be considered
                
# for invalid_record in invalid_data:
#     print(f"Invalid Record: {invalid_record.to_dict()}")


