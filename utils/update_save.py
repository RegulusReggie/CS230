#!/usr/bin/env python

old_save = "weichen/40_SourcererCC_Results.save"
diff = "diff_SourcererCC_Results.save"

if __name__ == '__main__':

	file1=None
	file2=None

	with open(old_save, "r") as text_file:
	    file1=text_file.read().split('\n')

	with open(diff, "r") as text_file2:
		file2=text_file2.read().split('\n')

	anno_old = []
	for i in range(1, len(file1)):
		anno_old.append(file1[i].split(' : '))

	for i in range(len(file2)):
		update_pair = file2[i].split(' : ')
		for j in range(len(anno_old)):
			if anno_old[j][0] == update_pair[0] and anno_old[j][1] == update_pair[1]:
				anno_old[j][2] = update_pair[2]

	score_map = {
		'0' : 0,
		'1' : 0,
		'2' : 0,
		'3' : 0
	}
	for i in range(len(anno_old)):
		score_map[anno_old[i][2]] += 1
	print('#F:' + str(score_map['0']) + ', #T1:' + str(score_map['1']) + ', #T2:' + str(score_map['2']) + ', #T3:' + str(score_map['3']))
	for i in range(len(anno_old)):
		print(anno_old[i][0] + ' : ' + anno_old[i][1] + ' : ' + anno_old[i][2])