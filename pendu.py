import random

words = ["sang", "hacher", "cyclique", "entre", "stupefaction","evoquer", "sinistre", "catastrophe", "creatif", "baron", "consultant", "fournisseur", "pieces" "fidele" "dupliquer" "promettre", "ambition", "aveuglant", " poisson", "ordinateur", "portatif", "football", "zebre"]
run = True
number = random.randrange(0, words.__len__())
response = list(words[number])
response_to_print = words[number]
case_to_print = ("__" + "  ") * response.__len__()
list_case = list(case_to_print[::2])
list_case = list_case[::2]
nbr_of_try = 10


while run:
    print(f'essais: {nbr_of_try} \n')
    print(case_to_print + "\n")
    tried = input(">> ")
    tried.upper()
    if(tried.__len__() > 1 or tried.__len__() == 0):
        print("Une seule lettre à la fois !")
        continue
    elif response.__contains__(tried.lower()):
        while response.__contains__(tried.lower()):
            index = response.index(tried)
            response[index] = " "
            rest = response.__len__() - index - 1
            list_case[index] = tried
            if("_" not in list_case):
                print('\nYOU WIN !!!\n')
                print(response_to_print.upper() + '\n')
                run = False
                break
            case_to_print = ""
            for letter in list_case:
                if(letter == '_'):
                    case_to_print += f"{letter}_  "
                else:
                    case_to_print += f"{letter.upper()}  "
            if nbr_of_try == 0 and run :
                print("\n YOU LOSE !! \n")
                print(response_to_print.upper() + '\n')
                run = False
                break
        
    else:
        nbr_of_try -= 1
        if nbr_of_try == 0 :
            print("\n YOU LOSE !! \n")
            print(response_to_print.upper() + '\n')
            break
