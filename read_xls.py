from xlrd import open_workbook


def get_xls(user):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # get xls file's path
    # open xls file
    file = open_workbook('/Users/shiyanlei/Downloads/北京办公地人员表-2.xlsx')
    # get sheet by name
    sheet = file.sheet_by_name('Sheet0')
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(1, nrows):
        if sheet.row_values(i)[6] == user:
            num = str(int(sheet.row_values(i)[1])).lstrip('0')
            # print(num)
            cls.append([sheet.row_values(i)[0], num])
    # print(cls)
    print(f"total: {len(cls)}")
    return cls


if __name__ == '__main__':
    get_xls('石延磊')
