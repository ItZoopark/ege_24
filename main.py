# data = [int(el[:-1]) for el in lines]
# print(lines)
# print(lines[1])
# ----------------------------------------
# 27421
# lines = list(open("24_demo.txt"))[0]
# count = 1
# count_max = 0
# for i in range(len(lines)-1):
#     if lines[i] != lines[i + 1]:
#         count += 1
#     else:
#         count_max = max(count_max, count)
#         count = 1
# print(count_max)
# ----------------------------------------
# 27687
# lines = list(open("24_demo_2.txt", 'r'))[0]
# y_str = 'Y'
# while y_str in lines:
#     y_str += 'Y'
# print(len(y_str)-1)
# ------------------------------------------
# 27689
# lines = list(open("24_demo_27689.txt"))[0]
#
# y_str = 'XYZ'
# while y_str in lines:
#     y_str += 'XYZ'
#
# y_str = y_str[:-3]
# if y_str + 'X' in lines:
#     y_str += 'X'
# if y_str + 'Y' in lines:
#     y_str += 'Y'
#
# print(y_str)
# print(len(y_str))
# -----------------------------------------
# 29672
# with open('29672.txt') as file:
#     lines = file.readlines()
#     lines = [line.strip() for line in lines]
# print(sum([int(row.count('E') > row.count('A')) for row in lines]))
# ------------------------------------------
# 33196
# lines = list(open('33196.txt'))[0]
# alphabet = {'A' + chr(a): 0 for a in range(65, 91)}
# for comb in alphabet:
#     alphabet[comb] = lines.count(comb)
# res = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)
# print(res)
# ------------------------------------------
# 35482
# with open('35482.txt') as file:
#     lines = file.readlines()
#     lines = [line.strip() for line in lines]
#
# dict = {}
# for i in range(len(lines)):
#     dict[i] = lines[i].count('G')
# # print(dict)
# res = sorted(dict.items(), key=lambda x: x[1])
# print(res)
# rowIndex = res[0][0]
# print(rowIndex)
# alphabet = {chr(i): 0 for i in range(65, 91)}
# for el in alphabet:
#     alphabet[el] = lines[rowIndex].count(el)
# res = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)
# print(res)
# -------------------------------------------
# 35998
# with open('35998.txt') as file:
#     lines = file.readlines()
#     lines = [line.strip() for line in lines]
#
# alphabet = {chr(i): 0 for i in range(65, 91)}
# max_dist = 0
# for row in lines:
#     cur_max = 0
#     if row.count('A') < 25:
#         for letter in alphabet:
#             cur_max = max(row.rfind(letter) - row.find(letter), cur_max)
#     max_dist = max(max_dist, cur_max)
# print(max_dist)
# --------------------------------------------
# 36037
# lines = list(open('36037.txt'))[0]
# res = lines.split('XZZY')
# print(len(max(res, key=len)) + 6)
# -------------------------------------------
# 37131
# lines = list(open('37131.txt'))[0]
# res = lines.split(' L')
# max_dist = 0
# for row in res:
#     max_dist = max(len(max(row.split('LK'), key=len))+2, max_dist)
# print(max_dist)
# -------------------------------------------
# print(len(max(res, key=len)) + 2)
# res = lines.split('LK')
# print(len(max(res, key=len)) + 2)
# max_chain = 0
# cur_max = 1
# for i in range(len(lines)):
#     if lines[i] == 'K' and lines[i+1] == 'L' or lines[i] == 'L' and lines[i+1] == 'K':
#         max_chain = max(max_chain, cur_max)
#         cur_max = 1
#     else:
#         cur_max += 1
# print(max_chain)
# -------------------------------------------
# 37159
# lines = list(open('37159.txt'))[0]
# max_dist = 0
# cur_dist = 1
# for i in range(len(lines) - 1):
#     if lines[i] == 'a' and lines[i + 1] == 'd' or lines[i] == 'd' and lines[i + 1] == 'a':
#         max_dist = max(max_dist, cur_dist)
#         cur_dist = 1
#     else:
#         cur_dist += 1
# print(max_dist)
# max_all = 0
# res = lines.split('ad')
# for el in res:
#     cur_max = len(max(el.split('da'), key=len))
#     max_all = max(max_all, cur_max)
# print(max_all+2)

# 'gfadjuyeruytertad'

# lines = 'vcbadyggtda'
# res = ['vcb','yggtda']
# cur_max = len('vcb')
# max_all = 3
# ['yggt',''] -> 4
# --------------------------------------------
# 38602
# lines = list(open('38602.txt'))[0]
# # этот подход не учитывает пустые ячейки в результате
# print(max(lines.split('PP'), key=len))
# res = len(max(lines.split('PP'), key=len)) + 2  # две по краям
# if
# print(res)
# 'PPPPhgdfshgdsfPdsgfcPPPshdfgdsfPPP'
# res = ['','', 'hgdfshgdsfPdsgfc', 'Pshdfgdsf']
# ---------------------------------------------
# max_count = 0
# cur_count = 1
# start = 0
# for i in range(len(lines) - 1):
#     if lines[i] == lines[i + 1] == 'P':
#         max_count = max(max_count, cur_count)
#         # if cur_count > max_count:
#         #     max_count = cur_count
#         #     coord = (start, i - 1)
#         # start = i + 1
#         cur_count = 1
#     else:
#         cur_count += 1
# print(max_count)
# print(coord)
# print(lines[coord[0]: coord[1]])
# ----------------------------------------------
# 3786
import string

# input = open("3786.txt").read().splitlines()
# # alphabet = string.ascii_uppercase
# # dict = dict(zip(alphabet, [0] * len(alphabet)))
# alphabet = {chr(i): 0 for i in range(65, 91)}
# max_all = 0
# freq = []
# for i in range(len(input)):
#     str_res = ''
#     cur_max = 0
#     for letter in alphabet:
#         str_res += letter
#         while str_res in input[i]:
#             str_res += letter
#         str_res = str_res[:-1]
#         if len(str_res) > cur_max:
#             cur_max = len(str_res)
#             let = list(set(str_res))[0]
#         str_res = ''
#     freq.append([let, cur_max, i])
# print(freq)
# freq = sorted(freq, key=lambda x: (x[1], x[2]), reverse=True)
# print(freq)
# row_index = 161
# for letter in alphabet:
#     alphabet[letter] = input[row_index].count(letter)
# print(alphabet)
# print(sorted(alphabet.items(), key=lambda x: x[1], reverse=True))
# print( ''.join(input).count('K'))
