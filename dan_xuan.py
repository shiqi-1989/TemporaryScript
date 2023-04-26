import copy

result_list = []
correct_answer = 'b'
options_mata = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0
}
while True:
    my_answer = input(f"请输入答案: \n")
    if my_answer:
        result_list.append(my_answer)
    else:
        continue
    total = len(result_list)
    print(f"第{len(result_list)}次答题结果：")
    options = copy.deepcopy(options_mata)
    correct_no = 0
    for i in result_list:
        if i == correct_answer:
            correct_no += 1
        for key in options:
            options[key] += i.count(key)
    print(f"正确率:{correct_no / total}")
    for key in options:
        if key != correct_answer:
            if options[key] / total:
                print(f"{key}的错误率{options[key] / total}")
    print(f"难度系数:{1 - correct_no / total}")
    print("-----------------------------------")
