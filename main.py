
# creea unei liste de float uri prin intermediul listei final_list


def creat_list():
    final_list = []
    initial_list = input("elementele din lista sunt ")
    for elem_list in initial_list.split(" "):
        elem = float(elem_list)
        final_list.append(elem)
    return final_list

# Functia returneaza o lista formata din partea intreaga a elementelor din lista citita prin parcurgearea fiecarui element din lista iniiala
# convertindu l in parte intreaga si adaugandu l in lista finala

def get_int(lista):
    final_lista = []
    for index in lista:
        var = int(index)
        final_lista.append(var)
    return final_lista


def test_get_int(lista):
    assert get_int([1.2, 2.4, 3.2]) == [1, 2, 3]
    assert get_int([-3.3, 2]) == [-3, 2]


# functia are ca parametrii left_margin si right_margin capetele intevalului
# variabila ok are rolul de a verifica daca exita elemente in intervalul dat
# index ul parcurge elemetele din lista data si verifica fiecare element daca exista sau nu in nintervaluld dat


def get_interval(left_margin, right_margin, lista):
    final_lista = []
    ok = False
    for index in lista:
        if index > left_margin and index < right_margin:
            final_lista.append(index)
            ok = True
    if ok is False:
        return "nu exista elemente aflate in interval"
    return final_lista


def test_get_interval():
    assert get_interval(2, 3, [1.1, 2.5, 4.5]) == [2.5]
    assert get_interval(0, 10, [-3.3, 1, 2]) == [1,2]




#functia are rolul de a verifica daca partea intreaga a numarului divide partea fractiionara a acestuia
#variabila ok are rolul de a verifaca daca exista minim un termen care respecta aceasta conditie si afiseaza
# un mesaj in caz contrar
#functia ia numerele negative si cele pozitive pe 2 cazuri deoarece in convveria in string indexare este diferita
# var_int este partea intreaga var_str este termenul sub forma de string


def get_div_test(lista):
    assert get_div([3.3, 2.1]) == [3.3]
    assert get_div([2.4]) == [2.4]


def get_div(lista):
    final_lista = []
    ok = False
    for index in lista:
        if index > 0:
            var = index
            var_int = int(index)
            var_str = str(index)
            var_str.split(".")
            if int(var_str[2]) % var_int == 0:
                final_lista.append(var)
                ok = True
        else:
            var = index
            var_int = int(index)
            var_str = str(index)
            var_str.split(".")
            if int(var_str[3]) % var_int == 0:
                final_lista.append(var)
                ok = True
    if ok is False:
        return "nu exista elemente care sa respecte cerinta data"
    return final_lista


#functia primeste ca date de intrare float uri pe care le converteste in stringuri
#parcurge string ul element cu element adaugand intr un string aux forma cifrei ca si cuvant
#verifica fiecare termen din string cu o anumita cifra iar apoi adauga in string_aux forma acesteia ca si cuvant


def get_var_written(lista):
    final_lista = []
    for index in lista:
        string_aux = ""
        var_str = str(index)
        for index2 in var_str:
            if index2 == '-':
                string_aux = string_aux + "minus"
            elif index2 == '.':
                string_aux = string_aux + "virgula"
            elif index2 == '1':
                string_aux = string_aux + "unu"
            elif index2 == '2':
                string_aux = string_aux + "doi"
            elif index2 == '3':
                string_aux = string_aux + "trei"
            elif index2 == '4':
                string_aux = string_aux + "patru"
            elif index2 == '5':
                string_aux = string_aux + "cinci"
            elif index2 == '6':
                string_aux = string_aux + "sase"
            elif index2 == '7':
                string_aux = string_aux + "sapte"
            elif index2 == '8':
                string_aux = string_aux + "opt"
            elif index2 == '9':
                string_aux = string_aux + "noua"
            elif index2 == '0':
                string_aux = string_aux + "zero"
        final_lista.append(string_aux)
    return final_lista

def main():
    my_list = []
    verif = True
    print("""""
        1 citeste elementele multimii
        2 afiseaza partea intreaga a numerelor din lista
        3 afisarea elementelor existente intr un anumit interval dat
        4 afisarea elem entului a carui parte intreaga divide partea fractionara
        5 formateaza cifrelor in cuvinte 
        x iesi din program
    """)
    while verif is True:
        opt = input("selecteaza optiunea ")
        if opt == '1':
            my_list = creat_list()
        elif opt == '2':
            print(get_int(my_list))
        elif opt == '3':
            left_margin = int(input("marginea din stanga este",))
            right_margin = int(input("marginea din dreapta este",))
            print(get_interval(left_margin,right_margin,my_list))
        elif opt == "4":
            print(get_div(my_list))
        elif opt == "5":
            print(get_var_written(my_list))
        elif opt == "x":
            verif = False
            print("Ati iesit din program")
        else:
            break


if __name__ == '__main__':
    main()
