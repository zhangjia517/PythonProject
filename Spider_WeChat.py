import itchat
import time

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]

# # 微信群发信息
# for friend in friends:
#     print(friend['RemarkName'] + '! 祝你新年快乐啦！')
#     # itchat.send(friend['RemarkName'] + '祝你新年快乐啦！')
#     time.sleep(1)


# # 获取朋友性别比
# male = female = other = 0
# for i in friends[1:]:
#     sex = i["Sex"]
#     if sex == 1:
#         male += 1
#     elif sex == 2:
#         female += 1
#     else:
#         other += 1

# total = len(friends[1:])
# print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
#       "女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
#       "不明性别好友： %.2f%%" % (float(other) / total * 100))


# # 获取朋友资料
# def get_var(var):
#     variable = []
#     for i in friends:
#         value = i[var]
#         variable.append(value)
#     return variable

# RemarkName = get_var("RemarkName")
# NickName = get_var("NickName")
# Sex = get_var('Sex')
# Province = get_var('Province')
# City = get_var('City')
# Signature = get_var('Signature')

# from pandas import DataFrame
# data = {'RemarkName': RemarkName, 'NickName': NickName, 'Sex': Sex, 'Province': Province,
#         'City': City, 'Signature': Signature}
# frame = DataFrame(data)
# frame.to_csv('data.csv', index=True)
