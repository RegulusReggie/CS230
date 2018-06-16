#!/usr/bin/env python
import sys

similarity = "40"
rand_file = similarity + "_cc_random_100_index.txt"
sourcerCC_file = similarity + "_sourcererCC_clone_content.txt"
similar_file = "wen.txt"
similar_rand_idx = [5, 11, 42, 104, 123, 136, 148, 157, 160, 163, 173, 186, 188, 202, 218, 219, 225, 231, 260, 293, 308, 315, 346, 350, 356, 361, 371, 397, 422, 437, 440, 448, 472, 550, 565, 593, 609, 629, 675, 679, 679, 717, 728, 756, 822, 831, 872, 873, 880, 888, 894, 904, 919, 929, 932, 959, 970, 988, 1002, 1003, 1005, 1024, 1047, 1053, 1070, 1220, 1254, 1282, 1308, 1322, 1324, 1334, 1342, 1378, 1404, 1423, 1425, 1459, 1470, 1487, 1490, 1500, 1524, 1524, 1531, 1544, 1568, 1570, 1589, 1599, 1638, 1642, 1696, 1699, 1734, 1735, 1819, 1849, 1859, 1889]

def getBlocks(big_block):
	j = 0
	counter = 0
	block_1 = []
	block_2 = []
	block_3 = []
	block_4 = []
	while j < len(big_block):
		if big_block[j] == dash:
			counter += 1
			j += 1
			continue
		if counter == 1:
			block_1.append(''.join(big_block[j].split()))
			block_3.append(big_block[j][:-1])
		if counter == 2:
			block_2.append(''.join(big_block[j].split()))
			block_4.append(big_block[j][:-1])
		if counter == 3:
			break
		j += 1
	return (''.join(block_1), ''.join(block_2), block_3, block_4)

def printList(l):
	for i in range(len(l)):
		print(l[i])

def match(block1, block2):
	longer = block1 if len(block1) > len(block2) else block2
	shorter = block2 if len(block1) > len(block2) else block1
	return longer.find(shorter) != -1

if __name__ == '__main__':
	reverse = False
	if (len(sys.argv)) > 1:
		if sys.argv[1] == "-r":
			reverse = True
		else:
			exit()
	num_clones = 0
	with open(rand_file, "r") as f:
		lines = f.readlines()
		f.close()
		num_clones = int(lines[0])
		rand_idx = [int(num) for num in lines[1].split(' ')]
	rand_idx.sort()

	if reverse:
		rand_idx = similar_rand_idx

	file1=None
	file2=None

	block_list1=[]
	block_list2=[]

	mapping = {}

	dash = "-------------------------------------------\n"


	with open(sourcerCC_file, "r") as text_file:
	    file1=text_file.readlines()

	with open(similar_file, "r") as text_file2:
		file2=text_file2.readlines()

	start = 0
	end = 0 
	for i in range(1,num_clones + 1):
		sep = str(i)+dash

		while start < len(file1) and file1[start] != sep :
			start += 1

		end = start
		sep_next = str(i+1)+dash
	    
		while end < len(file1) and file1[end] != sep_next:
			end += 1

		block_list1.append(getBlocks(file1[start:end]))
		start = end

	start = 0
	end = 0 
	for i in range(1,1931):
		sep = str(i)+dash

		while start < len(file2) and file2[start] != sep :
			start += 1

		end = start
		sep_next = str(i+1)+dash
	    
		while end < len(file2) and file2[end] != sep_next:
			end += 1

		block_list2.append(getBlocks(file2[start:end]))
		start = end

	if not reverse:
		for i in range(len(block_list1)):
			sourcerCC_block = block_list1[i - 1]
			for j in range(len(block_list2)):
				similar_block = block_list2[j]
				if (match(sourcerCC_block[0], similar_block[0]) and match(sourcerCC_block[1], similar_block[1])) or (match(sourcerCC_block[1], similar_block[0]) and match(sourcerCC_block[0], similar_block[1])):
					mapping[str(i)] = str(j + 1)
					print('CC_' + str(i) + ' : SimilaR_' + str(j + 1))
					print('------CC1------')
					printList(sourcerCC_block[2])
					print('------CC2------')
					printList(sourcerCC_block[3])
					print('------SR1------')
					printList(similar_block[2])
					print('------SR2------')
					printList(similar_block[3])
					break
		#print(mapping)
	else:
		for i in range(len(block_list2)):
			similar_block = block_list2[i - 1]
			for j in range(len(block_list1)):
				sourcerCC_block = block_list1[j]
				if (match(sourcerCC_block[0], similar_block[0]) and match(sourcerCC_block[1], similar_block[1])) or (match(sourcerCC_block[1], similar_block[0]) and match(sourcerCC_block[0], similar_block[1])):
					mapping[str(i)] = str(j + 1)
					break
		print(mapping)