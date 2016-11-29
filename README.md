# ahcg_pipeline
Forked by ntopaz
Variant calling pipeline for genomic data analysis

## Requirements

1. [Python3 - version 3.4.1](https://www.python.org/download/releases/3.4.1/)
2. [Trimmomatic - version 0.36](http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip)
3. [Bowtie2 - version 2.2.9](https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.9/)
4. [Picard tools - version 2.6.0](https://github.com/broadinstitute/picard/releases/download/2.6.0/picard.jar)
5. [GATK - version 3.4](https://software.broadinstitute.org/gatk/download/)

## Reference genome

Reference genomes can be downloaded from [Illumina iGenomes](http://support.illumina.com/sequencing/sequencing_software/igenome.html)

## Test data

Use the following protocol to download and prepare test dataset from NIST sample NA12878

```{sh}
wget ftp://ftp-trace.ncbi.nih.gov/giab/ftp/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome/NIST7035_TAAGGCGA_L001_R1_001.fastq.gz
wget ftp://ftp-trace.ncbi.nih.gov/giab/ftp/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome/NIST7035_TAAGGCGA_L001_R2_001.fastq.gz
gunzip NIST7035_TAAGGCGA_L001_R1_001.fastq.gz
gunzip NIST7035_TAAGGCGA_L001_R2_001.fastq.gz
head -100000 NIST7035_TAAGGCGA_L001_R1_001.fastq > test_r1.fastq
head -100000 NIST7035_TAAGGCGA_L001_R2_001.fastq > test_r2.fastq
```


## Setup Github
```{sh}
git remote setup-url origin https.github.com/(USERNAME)/(PROJECT).git
Edited .gitignore file to avoid adding unnecessary files to repository
Edited readme (this)
git push -u origin master 
```


## Help

To access help use the following command:

```{sh}
python3 ahcg_pipeline.py -h
```


## Pipeline Dependencies and Command
```{sh}
Python3 - version 3.4.1
Trimmomatic - version 0.36
Bowtie2 - version 2.2.9
Picard - version 2.6.0
GATK - version 3.4

#Reference Genome:
 
wget www.prism.gatech.edu/~sravishankar9/resources.tar.gz

#Bowtie Index: 

bowtie2-build -f /path/to/hg19.fa hg19

#Samtools Index:

samtools faidx /path/to/hg19.fa

#Test Data Set Files:

wget ftp://ftp-trace.ncbi.nih.gov/giab/ftp/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome/NIST7035_TAAGGCGA_L001_R1_001.fastq.gz
wget ftp://ftp-trace.ncbi.nih.gov/giab/ftp/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome/NIST7035_TAAGGCGA_L001_R2_001.fastq.gz

Get first 100000 lines using head of each

```

### Pipeline Run Command

```{sh}
python3 ahcg_pipeline.py -t lib/Trimmomatic-0.36/trimmomatic-0.36.jar -b lib/bowtie2-2.2.9/bowtie2 -p lib/picard.jar -g lib/GenomeAnalysisTK.jar -i data/test_r1.fastq data/test_r2.fastq -w data/resources/genome/hg19 -d data/resources/dbsnp/dbsnp_138.hg19.vcf.gz -r data/resources/genome/hg19.fa -a lib/Trimmomatic-0.36/adapters/NexteraPE-PE.fa -o .
```

### 9/8/2016 - Working on BRCA1 Gene  ###
```{sh}
#Get annotation file for hg19
wget http://vannberg.biology.gatech.edu/data/ahcg2016/reference_genome/hg19_refGene.txt

#Grab gene of interest (BRCA1):
grep BRCA1 hg19_refGene.txt

#Use create_bed.py script to create bed from specified gene

python create_bed.py hg19_refGene.txt > output.bed

#Use bedtools getfasta to convert bed to fasta

bedtools getfasta -s -fi ./resources/genome/hg19.fa -bed output.bed -fo output.fna

```


### Extracting reads mapping to BRCA1 from NA12878 HiSeq Exome dataset:
```{sh}

#Download the NA12878 Exome dataset:
Found at: https://github.com/genome-in-a-bottle/giab_data_indexes/blob/master/NA12878/alignment.index.NA12878_HiSeq_Exome_Garvan_GRCh37_09252015

### Merge Bam files ###
samtools merge merged.bam in1.bam in2.bam .....	

#Use samtools to grab regions corresponding to bed BRCA1 bed:
samtools view -L <bed file> -b -o < outout bam file > < input bam file >

#Use bedtools to convert bam to fastq:
bedtools bamtofastq -i <bam file> -fq < fastq r1> -fq2 < fastq r2>

```


### Running pipeline on BRCA1 reference - 9/13/2016
```{sh}

#Obtained the new reference:

wget http://vannberg.biology.gatech.edu/data/brca.fa

#Created new bowtie2 and samtools index with same command above

#Ran pipeline command as shown below:

python3 ahcg_pipeline.py -t lib/Trimmomatic-0.36/trimmomatic-0.36.jar -b lib/bowtie2-2.2.9/bowtie2 -p lib/picard.jar -g lib/GenomeAnalysisTK.jar -i data/brca_r1.fastq data/brca_r2.fastq -w data/resources/genome/brca -d data/resources/dbsnp/dbsnp_138.hg19.vcf.gz -r data/resources/genome/brca.fa -a lib/Trimmomatic-0.36/adapters/NexteraPE-PE.fa -o .
 
#Obtained "gold standard" vcf for NA12878 from here:

wget ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/data/NA12878/analysis/Illumina_PlatinumGenomes_NA12877_NA12878_09162015/hg19/8.0.1/NA12878/NA12878.vcf.gz

#Both vcfs were bgzipped:

bgzip NA12878.vcf
bgzip brca_variants.vcf

#Both vcfs were tabix indexed:

tabix -p vcf NA12878.vcf.gz
tabix -p vcf brca_variants.vcf.gz
```


### Obtaining known gene list for diseases - 9/20/2016
```{sh}

#Gene list for color genomics available on: 
https://getcolor.com/learn/the-science

#Comparable gene list for breast/ovarian cancer available on:
http://www.otogenetics.com/forms/Breast_Cancer_gene_list.pdf

Gene list for ovarian and breast cancer:
BRIP1	NM_032043
BRCA1	NM_007294
BRCA2	NM_000059
DIRAS3	NM_004675
ERBB2	NM_001005862
CASP8	NM_001080124
TGFB1	NM_000660
MLH1	NM_000249
MSH2	NM_000251
MSH6	NM_000179
PMS2	NM_000535
EPCAM	NM_002354
TP53	NM_000546
PTEN	NM_000314
STK11	NM_000455
CDH1	NM_004360
PALB2	NM_024675
CHEK2	NM_001005735
AR 	NM_000044
ATM	NM_000051
NBN	NM_002485
BARD1	NM_000465
BRIP1	NM_032043
RAD50	NM_005732
RAD51A	NM_001164269
RAD51C	NM_058216
RAD51D	NM_002878


#Used create_bed.py to create exome-specific bed:

python create_bed.py > gene_list.bed

*Python script replaces start and end of gene with start and end of CDS
*Python script adds buffer of 500 (default) to start and end of CDS

#Samtools and Bedtools to obtain depth of coverage per base from bed file

samtools view -L data/gene_list.bed BAMFILE -b > new.bam

bedtools genomecov -ibam (bam) -bga > coverage_output.bed

bedtools intersect -loj -split -a brca1.bed -b coverage_output.bed > brca1_coverage.bed

awk '{printf("%s\t%s\t\%s\t%s\t%s\n", $1,$2,$3,$4,$10,$6)}' brca1_coverage.bed > final_brca1.coverage.bed

```

### Recalibrating VCF file obtained from NA12878 10/13/16
```{sh}

#Used vcftools to filter NA12878_variants.vcf file with the exons.bed file

vcftools --vcf NA12878_variants.vcf --bed exons.bed --recode --out 10_13_16_filtered.vcf

#Run GATK recalibration tool on vcf using command:


```
### Comparing recalibrated VCF with BRCA1 bed 
```{sh}
#Used bedtools intersect to compare vcf and brca1 bed to detect variants
bedtools intersect -a 10_13_16_filtered.vcf -b brca1_bed.bed 
# Generates VCF, compare with csv of known BRCA1/2 variants
Using script from Wilson Martin (https://github.com/redspot/ahcg_pipeline) 
compare_clin_with_vcf.py
```


