#!/usr/bin/env python
rand_file = "80_cc_random_100_index.txt"
result_file = "data/SourcererCC_Results_Weichen.txt"

if __name__ == '__main__':
	with open(rand_file, "r") as f:
		rand_idx = [int(num) for num in f.read().split(' ')]
		f.close()

	rand_idx.sort()
	with open(result_file, "r") as f:
		lines = f.readlines()
		f.close()
		lines = lines[1:]
		lines = [str(i) + ' : ' + lines[i - 1] for i in rand_idx]
		num_map = {
			'0' : 0,
			'1' : 0,
			'2' : 0,
			'3' : 0
		}
		name_map = {
			'0' : 'F',
			'1' : 'T1',
			'2' : 'T2',
			'3' : 'T3'
		}
		for line in lines:
			tokens = line.split(' : ')
			num_map[tokens[3].strip()] += 1
		stats = ''
		stats += '#' + name_map['0'] + ':' + str(num_map['0']) + ', '
		stats += '#' + name_map['1'] + ':' + str(num_map['1']) + ', '
		stats += '#' + name_map['2'] + ':' + str(num_map['2']) + ', '
		stats += '#' + name_map['3'] + ':' + str(num_map['3'])
		print(stats)
		print(''.join(lines))
