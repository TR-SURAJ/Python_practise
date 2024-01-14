test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
test_list = ['gfg', 'is', 'best']

res = []

for i in test_list:
    res.append(test_str.count(i))

x = max(res)
print(x)
i = res.index(x)
print(i)