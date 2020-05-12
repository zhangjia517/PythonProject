import xlrd


def extract(inpath):

    data = xlrd.open_workbook(inpath, encoding_override='utf-8')
    table = data.sheets()[0]  # 选择Sheet0
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号

    for i in range(1, nrows):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result0 = alldata[0]  # 取出表中第1列数据
        result1 = alldata[1]  # 取出表中第2列数据
        result3 = xlrd.xldate_as_datetime(result1, 0)  # 转换第二列数据为日期类型
        print(str(result0) + '    ' + str(result3))


inpath = 'D:\\Project\\CodeProject\\Github\\PythonTrialProject\\LC\\lc.xlsx'  # excel文件所在路径
extract(inpath)

input()
