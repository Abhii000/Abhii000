'''import re
list1=[]
def is_valid_email(email):
    # Define a regex pattern for a valid email address
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use the re.match function to match the pattern against the email address
    if re.match(pattern, email):
        return True
    else:
        return False

# Test with an email address
for a in range(int(input())):
    email_address = input()
    
if is_valid_email(email_address):
    list1.append(email_address)
print(list1)
'''
import re
def fun(s):
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use the re.match function to match the pattern against the email address
    if re.match(pattern, s):
        return True
    else:
        return False
# return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(lambda x: fun(x), emails))
if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
