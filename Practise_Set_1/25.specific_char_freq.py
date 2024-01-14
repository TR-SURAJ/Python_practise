test_list = ["geeksforgeeks is best for geeks"]
d = {}
chr_list = ['e', 'b', 'g'] 

s = test_list[0].split()

for i in s:
    for j in i:
        if j in chr_list:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1

print(d)
