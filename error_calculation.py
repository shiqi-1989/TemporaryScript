import copy
from pprint import pprint

import requests


# 小数点后N位四舍五入
def rounding(num, n=0):
    """
    功能：优化Python内置的round()函数有时出现四舍六入的问题，实现真正的四舍五入。
    实现原理：当需要四舍五入的小数点后一位是5时，加1变成6，即可顺利利用round()函数，实现真正的四舍五入。
    参数：
        num: 需要四舍五入的数字；
        n: 保留的小数点位数，默认取整。
    """

    if '.' in str(num):
        if len(str(num).split('.')[1]) > n and str(num).split('.')[1][n] == '5':
            num += 1 * 10 ** -(n + 1)
    if n:
        return round(num, n)
    else:
        return round(num)


# 获取接口 正确率相关信息
def get_request(qid):
    options_mata = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'J'
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=399B93B228E4E94E344FEBEB0E00080E; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2213716610001%22%2C%22first_id%22%3A%22186e911c285620-0aa7938f5890668-1e525634-2073600-186e911c286448%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22%24device_id%22%3A%22186e911c285620-0aa7938f5890668-1e525634-2073600-186e911c286448%22%7D; _const_huatu_jsession_id_=1682390550324.ea2b43c3-ce31-468d-96e1-ccb9c7fb11fb.pre-tiku.htexam.com/frontEnd',
        'Referer': 'https://pre-tiku.htexam.com/frontEnd/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'id': qid,
        'withParent': 'false',
        'subjectId': '200100178',
        'mode': '1',
    }

    response = requests.get('https://tiku.htexam.com/pand/question/v1', params=params,
                            headers=headers)
    result = response.json()['data']['questionMateDTO']
    options = ' '.join(options_mata[i] for i in result['errorChoices'])
    print(
        f"接口: 答题次数:{result['answerNum']}  正确率:{result['accuracy']}%  易错项:{options}(错误率{result['errorChoiceRates'][0]}%)  "
        f"难度系数: {result['difficulty']}%")


class Accuracy:
    """

    :param my_answer: 用户输入的作答答案
    :param result_list:  定义一个结果收集列表
    :param is_Single:  是否=单选题  true：单选   false：多选/不定项选择
    :param correct_answer:  定义正确答案
    :param options_mata: 定义选项：次数 map。用来记录每个选项的选择次数
    :return:  返回相关 正确率/错误率/易错项等相关数据输入你
    """

    def __init__(self):
        self.result_list = []

    def get_accuracy(self, is_single=None, correct_answer=None, options_mata=None, answers=None, qid=None,
                     on_off=None):
        self.result_list.append(answers)
        total = len(self.result_list)
        options = copy.deepcopy(options_mata)
        correct_no = 0

        for i in self.result_list:
            if i == correct_answer:
                correct_no += 1
            for key in options:
                options[key] += i.count(key)
        print(f"正确率:{rounding(correct_no / total * 100, 2)}%")
        for key in options:
            if not is_single:
                if key in correct_answer:
                    if 1 - options[key] / total:
                        print(f"{key.upper()} 的错误率{rounding((1 - options[key] / total) * 100, 2)}%")
                elif options[key]:
                    print(f"{key.upper()} 的错误率{rounding(options[key] / total * 100, 2)}%")
            elif key != correct_answer and options[key] / total:
                print(f"{key.upper()} 的错误率{rounding(options[key] / total * 100, 2)}%")
        print(f"难度系数:{rounding((1 - correct_no / total) * 100, 2)}%")
        if on_off is None:
            get_request(qid)

    def get_accuracy_list(self, is_single=None, correct_answer=None, options_mata=None, answers=None, qid=None):
        for index, answer in enumerate(answers):
            print(f"第{index + 1}次答题结果：")
            print(f"作答：{answer.upper()}")
            self.get_accuracy(is_single, correct_answer, options_mata, answer, on_off=1)
            print("-" * 80)
        get_request(qid)

    def run(self, *args, **kwargs):
        if isinstance(kwargs.get('answers'), list):
            self.get_accuracy_list(*args, **kwargs)

        elif not kwargs.get('answers'):
            while True:
                my_answer = input(f"请输入答案: \n")
                if my_answer == 'exit':
                    break
                if my_answer:
                    kwargs['answers'] = my_answer
                    accuracy.get_accuracy(**kwargs)
                    print("输入 'exit' 结束程序".center(80, '-'))
                else:
                    continue
        else:
            print("答案参数异常!")


if __name__ == '__main__':
    params = {
        "is_single": False,
        "correct_answer": 'b',
        "options_mata": {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0
        },
        "qid": 43918449
    }
    accuracy = Accuracy()
    params['answers'] = 'a'
    # params['answers'] = ['a', 'b', 'c', 'd', 'e', 'f']
    accuracy.run(**params)
