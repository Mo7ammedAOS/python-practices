def find_letter(letters):
    k = 'abcdefghijklmnopqrstuvwxyz'
    n = k.index(letters[0])
    op = []
    for i in k[n:]:
        if i not in letters:
            op.append(i)
            return op
    return f'there no missing letter'

print(find_letter('ace'))

