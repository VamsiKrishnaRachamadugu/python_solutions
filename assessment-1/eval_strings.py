ip_list=['five plus three','seven minus two','two plus eight minus five','eight divide four']
ref_dict={'plus':'+','minus':'-','divide':'/','two':'2','three':'3','four':'4','five':'5','seven':'7','eight':'8'}
p_list=[]
for i in ip_list:
    str_list=i.split(' ')
    string=''
    for i in str_list:
        string=string+ref_dict[i]
    p_list.append(string)
op_list=[]
for i in p_list:
    op_list.append(eval(i))
print(op_list)

