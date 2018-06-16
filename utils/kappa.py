#!/usr/bin/env python
import sys

similarity = "40"
weichen = "weichen/" + similarity + "_SourcererCC_Results.save"
zeng = "zeng/Zeng_" + similarity + "_SourcererCC_Results.save"

def kappa(anno1, anno2):
	num_cols = 4 # F, T1, T2, T3, Sum
	mat = []
	for i in range(num_cols):
		row = []
		for j in range(num_cols):
			row.append(0)
		mat.append(row)

	for i in range(len(anno1)):
		mat[anno1[i]][anno2[i]] += 1
		mat[num_cols - 1][anno2[i]] += 1
		mat[anno1[i]][num_cols - 1] += 1
		mat[num_cols - 1][num_cols - 1] += 1

	print('---------------------')
	for i in range(num_cols):
		line_output = ''
		for j in range(num_cols):
			line_output += str(mat[i][j]).rjust(5)
		print(line_output)

	print('---------------------')
	po = 0
	for i in range(num_cols - 1):
		po += mat[i][i]
	po = (float) (po) / mat[num_cols - 1][num_cols - 1]
	print('Po = ' + str(po))

	print('---------------------')
	pe = 0
	for i in range(num_cols - 1):
		pe += mat[i][num_cols - 1] * mat[num_cols - 1][i]
	pe = (float) (pe) / (mat[num_cols - 1][num_cols - 1] ** 2)
	print('Pe = ' + str(pe))

	print('---------------------')

	score = (po - pe) / (1 - pe)
	print('Kappa Score = ' + str(score))

	print('---------------------')	

if __name__ == '__main__':

	file1=None
	file2=None

	with open(weichen, "r") as text_file:
	    file1=text_file.readlines()

	with open(zeng, "r") as text_file2:
		file2=text_file2.readlines()

	anno_weichen = []
	for i in range(1, len(file1)):
		num = int(file1[i].split(' : ')[-1])
		if num == 3: num = 2
		anno_weichen.append(num)

	anno_zeng = []
	for i in range(1, len(file2)):
		num = int(file2[i].split(' : ')[-1])
		if num == 3: num = 2
		anno_zeng.append(num)

	kappa(anno_weichen, anno_zeng)
