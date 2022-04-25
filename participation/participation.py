# check the number from csv whether in the list


def check_in(file, ori_list):
    """
    Check the number from a list whether in the list
    """
    absence_list =[]
    for stud in ori_list:
        # check stud whether in the list

        if stud in file:
            pass
        else:
            absence_list.append(stud)
    return absence_list


if __name__ == '__main__':
    filename = 'Apr06.csv'
    # choose the last whole column in csv 
    file = [line.split(',')[-1].strip() for line in open(filename, 'r').readlines()]
    print(file)
    # stud list
    list = ['"8893265"', '"8833196"', '"8162638"', '"4814356"', 
    '"8042210"', '"8664351"', '"8639296"', '"5486899"', '"3755113"',
    '"8719254"', '"4486205"', '"4469284"', '"5966502"', '"4405635"',
    '"8039802"', '"5138359"', '"4481826"', '"3985272"', '"X304183"']
    
    print(check_in(file, list))