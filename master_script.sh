#!/bin/bash
TRIM_PATH=
BOWTIE_PATH=
PICARD_PATH=
GATK_PATH=
FASTQ_1=
FASTQ_2=
REFERENCE=
BT2_INDICES=
DBSNP=
ADAPTER=
TRIM_SUFFIX=".trimmed"
UNUSED_SUFFIX=".unused"
VARIANTS=
RECAL_OUTPUT=
RECAL=
GENE_LIST=
BAM_FILE=
#parse args
while getopts "t:b:p:g:w:i:q:d:r:a:o:" opt; do
    case $opt in
        t) TRIM_PATH="$OPTARG" ;;
        b) BOWTIE_PATH="$OPTARG" ;;
        p) PICARD_PATH="$OPTARG" ;;
        g) GATK_PATH="$OPTARG" ;;
        w) BT2_INDICES="$OPTARG" ;;
        i) FASTQ_1="$OPTARG" ;;
        q) FASTQ_2="$OPTARG" ;;
        d) DBSNP="$OPTARG" ;;
        r) REFERENCE="$OPTARG" ;;
        a) ADAPTER="$OPTARG" ;;
        o) VARIANTS="$OPTARG" ;;
    esac
done

#Run variant caller pipeline
python3 ahcg_pipeline.py \
-t $TRIM_PATH \
-b $BOWTIE_PATH \
-p $PICARD_PATH \
-g $GATK_PATH \
-i $FASTQ_1 $FASTQ_2 \
-w $BT2_INDICES \
-d $DBSNP \
-r $REFERENCE \
-a $ADAPTER \
-o ./output.vcf


#Recalibration
java -jar $GATK_PATH \
    -T ApplyRecalibration \
    -R $REFERENCE \
    -input ./output.vcf \
    -mode SNP \
    --ts_filter_level 99.0 \
    -recalFile output.recal \
    --tranches_file output.tranches \
    -o output_recal.vcf

#Get Coverage
samtools view -L $GENE_LIST $BAMFILE -b > new.bam
bedtools genomecov -ibam new.bam -bga > coverage_output.bed
bedtools intersect -loj -split -a $GENE_LIST -b coverage_output.bed >  cov.bed
awk '{printf("%s\t%s\t\%s\t%s\t%s\n", $1,$2,$3,$4,$10,$6)}' cov.bed > prepped_cov.bed
