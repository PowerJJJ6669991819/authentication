import re
def GetIdAndPwd(post_data):
    id_key = list(post_data.keys())[0]
    password_key = list(post_data.values())[0][0]
    id_value = re.findall("= (.*) ", id_key)[0]
    password_value = re.findall("= (.*) ", password_key)[0]
    value = {id_value:password_value}
    return(value)

if __name__ == '__main__':
    post_data1 = {" id = Lemonade ": [" password = 1023 "]}
    value1 = GetIdAndPwd(post_data1)
    print(value1)