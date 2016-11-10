import sys

#input refgene file
my_file = sys.argv[1]
output_text = sys.argv[2]
#list of targets
#target_list=['NM_000059']

#target_list=['NM_032043','NM_007294','NM_000059','NM_004675','NM_001005862','NM_001080124','NM_000660','NM_000249','NM_000251','NM_000179','NM_000535','NM_002354','NM_000546','NM_000314','NM_000455','NM_004360',
#'NM_024675',
#'NM_001005735',
#'NM_000044',
#'NM_000051',
#'NM_002485',
#'NM_000465',
#'NM_005732',
#'NM_001164269',
#'NM_058216',
#'NM_002878']

#target_dict = {"BRCA1":"NM_007294","BRCA2":"NM_00059","AR":"NM_000044","ATM":"NM_000051","BARD1":"NM_000465","BRIP1":"NM_032043","CASP":"NM_001080224","CDH1":"NM_004360",
#		"CHEK2":"NM_001005735","DIRAS3":"NM_004675","MSH6":"NM_000179.2","ERBB2":"NM_001005862","NBN":"NM_002485","PALB2":"NM_0024675","PTEN":"NM_000314","RAD50":"NM_005732","RAD51":"NM_001104269",
#		"STK11":"NM_000455","TGFB1":"NM_0006606","TP53":"NM_0005465","MLH1":"NM_000249","MSH2":"NM_000251","PMS2":"NM_000535","EPCAM":"NM_002354","RAD51C":"NM_002876","RAD51D":"NM_002878"}

target_dict = {"TNNT2":"NM_001001430","SCNSA":"NM_198056","MYH7":"NM_000257","MYBPC3":"NM_000256","MYH6":"NM_002471","LMNA":"NM_170707"}
#buffer to add/subtract to end/start of cds
start_buffer = 200
exon_buffer = 20
text = ""
revised_text = ""
with open(output_text,"w") as f:
	for target in target_dict.keys():
		f.write(target + "\t" + target_dict[target] + "\n")

firstline = True
with open(my_file) as f:
	the_text = f.readlines()
q=0
#iterate through target list
for target in target_dict.keys():
	init_start = 0
	current_start = 0
	current_end = 0
	i = 1
	for line in the_text:
		if target_dict[target] in line:
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
			text += chrom + "\t" + str(int(current_start)-exon_buffer) + "\t" + str(int(current_end)+exon_buffer) + "\t" + target +"\n"
			continue
	
	#grab cds start and stop and replace start and end of gene coordinates with respective
#	for line in text.split("\n"):
#		if line.strip() != "":
#			start = str(int(line.split("\t")[1])-start_buffer)
#			stop = str(int(line.split("\t")[2])+start_buffer)
#			chr = line.split("\t")[0]
#			if cds_s > int(start) and cds_s < int(stop):
#				revised_text += str(q)+"\t"+chr + "\t" + str(cds_s) + "\t" + stop + "\n"
#				continue
#			if cds_e > int(start) and cds_e < int(stop):
#				revised_text += str(q)+"\t"+chr + "\t" + start + "\t" + str(cds_e) + "\n"
#				break
#			else:
#				revised_text += str(q)+"\t"+ chr + "\t" + start + "\t" + stop + "\n"

print text
