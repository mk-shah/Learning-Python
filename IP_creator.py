'''
Write a function called create_ip_address_4()
Has default parameters of a='172', b='16', c='254', d='1'
 'a' must be exactly length of 3 and contains ONLY strings of digits
'b' must be exactly length 2 and contains ONLY strings of digits
'c' must be exactly length 3 and contains ONLY strings of digits
'd' must be exactly length 1 and contains ONLY strings of digits
If any of the following conditions are invalid then a ValueError() exception will be raised.
Research how to raise a ValueError
'''

import string

def check_octect(ip, ip_len):
        if type(ip) == str and ip.isdigit() and int(ip) <= 255 and len(ip) == ip_len:
            return True
        else:
            raise ValueError ("Invalid IP address")

def create_ip_address_4(a='172', b='16', c ='254', d='1'):
        if check_octect(a,3) :
            if check_octect(b,2):
                if check_octect(c,3):
                    if check_octect(d,1):
                        print(f"{a}.{b}.{c}.{d}")

#create_ip_address_4()
create_ip_address_4(a='20')
# create_ip_address_4(a='172', b='168')
# create_ip_address_4(a='172', b='16', c='10')
# create_ip_address_4(a='300', b='16', c='100', d="20")
# create_ip_address_4(a='172', b='16', c='100', d="1")

