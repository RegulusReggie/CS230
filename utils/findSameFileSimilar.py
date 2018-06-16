#!/usr/bin/env python 

def findSameFile(big_block):
	file1 = big_block[6].split(' : ')[0]
	file2 = big_block[7].split(' : ')[0]
	if file1 == file2:
		return file1
	return None

if __name__ == '__main__':
	file1=None

	block_list1=[]

	dash = "-------------------------------------------\n"

	with open("wen.txt", "r") as text_file:
	    file1=text_file.readlines()

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

		sameFile = findSameFile(file1[start:end])
		if sameFile:
			block_list1.append(sameFile)
		start = end
	print(block_list1)