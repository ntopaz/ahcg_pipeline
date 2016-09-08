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


## Pipeline Dependencies
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

#Use samtools to grab regions corresponding to bed BRCA1 bed:
samtools view -L <bed file> -b -o < outout bam file > < input bam file >

#Use bedtools to convert bam to fastq:
bedtools bamtofastq -i <bam file> -fq < fastq r1> -fq2 < fastq r2>

```

