#!/usr/bin/env python 

def getBlocks(big_block):
	j = 0
	counter = 0
	block_1 = []
	block_2 = []
	while j < len(big_block):
		if big_block[j] == dash:
			counter += 1
		if counter == 1:
			block_1.append(big_block[j])
		if counter == 2:
			block_2.append(big_block[j])
		if counter == 3:
			break
		j += 1
	return (''.join(block_1), ''.join(block_2))

if __name__ == '__main__':
	file1=None
	file2=None

	block_list1=[]
	block_list2=[]

	mapping = {}
	dash = "-------------------------------------------\n"

	with open("wen.txt", "r") as text_file:
	    file1=text_file.readlines()

	with open("chen.txt", "r") as text_file2:
		file2=text_file2.readlines()

	start = 0
	end = 0 
	for i in range(1,1931):
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

	for i in range(len(block_list1)):
		xia_block = block_list1[i]
		for j in range(len(block_list2)):
			wen_block = block_list2[j]
			if (xia_block[0] == wen_block[0] and xia_block[1] == wen_block[1]) or (xia_block[0] == wen_block[1] and xia_block[1] == wen_block[0]):
				mapping[str(i)] = str(j)
				break
	print(mapping)