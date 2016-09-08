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
'''


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

Build using bowtie2 with command: bowtie2-build -f /path/to/hg19.fa hg19

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


