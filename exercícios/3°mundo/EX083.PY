exp = str(input('Digite uma expressão: '))
con = []
for par in exp:
    if par == '(':
        con.append('(')
    elif par == (')'):
        if len(con) > 0:
            con.pop()
        else:
            con.append(')')
            break
if len(con) == 0:
    print('\033[1;32mExpressão valida\033[m')
else:
    print('\033[1;31mExpressão invalida\033[m')