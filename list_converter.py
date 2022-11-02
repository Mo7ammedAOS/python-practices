
def word_converter(list):
    new_fields=[]
    for field in list:
        new =''
        for letter in field:
            if letter == '_':
                letter = ' '
            new += letter
        new_fields.append(new)
    return new_fields


fields = ['first_name','last_name','email_address']

print(word_converter(fields))
