import sys


my_file = sys.argv[1]
target = "NM_007294"
#my_dict = {}
coord_list = []
init_start = 0
current_start = 0
current_end = 0
text = ""
revised_text = ""
i = 1
q = 1
firstline = True
with open(my_file) as f:
	the_text = f.readlines()

for line in the_text:
	if target in line:
		props = line.split('\t')
		chrom = props[2]
		cds_start = props[6]
		cds_end = props[7]
		strand = props[3]
		coord_1 = props[9].strip()
		coord_2 = props[10].strip()
		all_coords = coord_1 + coord_2

cds_s = int(cds_start)
cds_e = int(cds_end)

for coord in sorted(all_coords.split(',')):
	if coord.strip() == '':
		continue
	if i == 1:
		current_start = coord
		i = 2
		continue
	if i == 2:	
		current_end = coord
		i = 1
		text += chrom + "\t" + current_start + "\t" + current_end + "\n"
		continue


for line in text.split("\n"):
	if line.strip() != "":
		start = line.split("\t")[1]
		stop = line.split("\t")[2]
		chr = line.split("\t")[0]
		if cds_s > int(start) and cds_s < int(stop):
			revised_text += chr + "\t" + str(cds_s) + "\t" + stop + "\n"
			continue
		if cds_e > int(start) and cds_e < int(stop):
			revised_text += chr + "\t" + start + "\t" + str(cds_e) + "\n"
			break
		else:
			revised_text += chr + "\t" + start + "\t" + stop + "\n"
	
print revised_text
