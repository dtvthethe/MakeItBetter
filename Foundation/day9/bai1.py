import re

re_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
arr_data_test_case = ['192.168.255.255', '12.18.55.25', '192.18.255.255', '0.0.0.0', '192.168. 255.255', '192.a68.255.255',
                 '192.168.25?5.255', '19.255.255']

for ip in arr_data_test_case:
    if re.match(re_pattern, ip):
        print('%s -> OK' %ip)
    else:
        print('%s -> Wrong format' % ip)