def homework(my_list: list):
    new_list = []
    for index in range(len(my_list)):
        if index % 2 == 0:
            new_list.append(my_list[index][::-1])
        else:
            new_list.append(my_list[index][::])
    return new_list


def home(my_list: list):
    new_list = []
    for element in my_list:
        if element[0] == 'a':
            new_list.append(element)
    return new_list


def work(my_list: list):
    new_list = [newlist for newlist in my_list if 'а' in newlist]
    return new_list


def hwork(my_list: list):
    new_list = []
    for element in my_list:
        if type(element) is str:
            new_list.append(element)
    return new_list


def homew(my_str):
    new_list = []
    [new_list.append(i) for i in my_str if my_str.count(i) == 1]
    return new_list


def hw(my_str, my_str2):
    new_list = []
    for i in my_str:
        k = my_str.find(i) - my_str2.rfind(i)
        if k == 0:
            if i in my_str2 and my_str2.find(i) - my_str2.rfind(i) == 0:
                print(i)
                new_list.append(i)
    return new_list


from random import randint

random_number = random.randint(100, 1000)
random_word = ''.join(chr(randint(ord('a'), ord('z'))) for j in range(randint(5, 7)))

email = surnames + "." + str(random_number) + "@" + str(random_word) + "." + domen_name
print(email)
