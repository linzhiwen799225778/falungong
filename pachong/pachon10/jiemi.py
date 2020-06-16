import execjs
with open('1.js','r') as w:
    js=w.read()
ele=execjs.compile(js)
print(ele.call('get', '123456'))
# 17a5e0bb17485016ff8ea7e2e8ab9668cd85aab84728e0cb821c171bebbfb47d8cd4e1b4c7208d4f56cf2759803bbc260c955019e3b3e1371b58b0b31c25b7d231f15dced9e9f79e443769676eed2a1caa16638152ef5267d35373edb0c4139cbc752a9aa28220f6b5b5d36442387b994b668a7fe08d7393b3f90b0905501cd5












