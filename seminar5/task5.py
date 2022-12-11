# 5. Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

sp = ['1', 'a', 'b', '2', '3', 'c']
sp1 = list(filter(lambda x: x.isdigit(), sp))
sp2 = list(filter(lambda x: x.isalpha(), sp))
print(sp1, sp2, sep='\n')
