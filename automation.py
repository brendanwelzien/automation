import re

def sort_email(unfiltered, filtered):
    # ana@foo.bar
    with open(unfiltered) as pool:
        pool = pool.read()
        email_pool = re.findall(r'[\w-]+@[\w-]+\.(?:org|com|info|net|bizTo)', pool)
        email_pool.sort()
    
    with open(filtered, 'w') as f:
        for single in email_pool:
            f.write(single + '\n')

def sort_phone(unfiltered, filtered):
    with open(unfiltered) as pool:
        pool = pool.read()
        phone_pool = re.findall(r'\d{3}.\d{3}[ .-]\d{4}', pool)
        replace = [number.replace('.', '-') for number in phone_pool]
        replace_two = [number.replace(')', "-") for number in replace]
        replace_two.sort()
            
        
    with open(filtered, 'w+') as f:
        for number in replace_two:
            f.write(number + '\n')


if __name__ == "__main__":
    sort_email('potential-contacts.txt', 'emails.txt')
    sort_phone('potential-contacts.txt', 'phone.txt')