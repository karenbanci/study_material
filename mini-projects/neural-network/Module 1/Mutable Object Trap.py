def append_first_letter(string: str, list_to_append=[]):
    list_to_append.append(string[0])
    return list_to_append


my_list = [ "amor", "beijo" ]
append_first_letter("coração", my_list)
print(my_list)

# aqui estou deixando uma lista vazia para ter a letra d salvo
my_new_list = append_first_letter("doce")
print(my_new_list)

# neste caso o list_to_append já foi criado quando eu criei my_new_list
my_new_list2 = append_first_letter("eletricidade")
print(my_new_list2)


def append_first_letter(string: str, list_to_append=None):
    if list_to_append is None:
        list_to_append = []
    list_to_append.append(string[0])
    return list_to_append

print("\ntestando -----------------------------------------")
my_list = [ "amor", "beijo" ]
append_first_letter("coração", my_list)
print(my_list)

# aqui estou deixando uma lista vazia para ter a letra d salvo
my_new_list = append_first_letter("doce")
print(my_new_list)

# neste caso o list_to_append já foi criado quando eu criei my_new_list
my_new_list2 = append_first_letter("eletricidade")
print(my_new_list2)