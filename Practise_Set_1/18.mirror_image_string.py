def mirror_image(test_str,mir_dict):

    res = ''

    for i in test_str:
        if i in mir_dict:
            res += mir_dict[i]  
        else:
            res = 'Not possible'
            break 
    print(res)  

test_str = 'void'
mir_dict = {'b':'d', 'd':'b', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}

mirror_image(test_str, mir_dict)