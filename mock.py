
# import numpy as np

# text_array = np.loadtxt('./dist/Results.txt', skiprows=1)
# # print(text_array)
# text_array = text_array[1:, :]
# docNo = text_array[:, 0]
# rank = text_array[:, 1]
# score = text_array[:, 2]
# print(docNo)

result_array = list((line.strip('\n') for line in open(
    "./dist/Results.txt", 'r')))
result_array = result_array[1:4]
print(result_array)
finResult = []
for meet in result_array:
    x = meet.strip()
    my_list = x.split(' ')
    new_list = []
    for jain in my_list:
        print("\n")
        if jain != '':
            new_list.append(jain)
    finResult.append(new_list)

print(finResult)


# txt = " nwrbihbr  bgibwr wgwrgwr  wrg  banana meet    "

# x = txt.strip()
# my_list = []

# my_list = x.split(" ")
# for meet in my_list:
#     if meet == " " or meet == "":
#         my_list.remove(meet)


# print(my_list)
