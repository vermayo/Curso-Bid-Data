import re

pattern = re.compile(r'\w+[.|]\w+@\w+\.\w+')

founded_emails = []

with open('./data.txt',"r") as archivo:
    for linea in archivo:
        correos = re.findall(pattern, linea)
        founded_emails.extend(correos)

for email in founded_emails:
    print(email)

print('Cantidad ',len(founded_emails))





