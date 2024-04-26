import re

def extract(filename):
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    with open(filename, 'r') as file:
        text = file.read()
        email_addresses = re.findall(email_pattern, text)
        for email in email_addresses:
            print(email)

filename = input("please input the file name you would like to read: ")
extract(filename)
