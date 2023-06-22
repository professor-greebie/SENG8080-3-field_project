# GTF & GFF File store GENOMIC FEATURES INFORMATION.
- Gtf and Gff3 format files are used for annotating genomic intervals (an interval begin/end position on a contig/chromosome)
- These files have 9 fields that describe the gene/transcript related to the features and are tab separated.
- Features in these files are hierarchical. 
- GFF and GTF are TSV-based formats and, in general, have the same structure but with different numbers of features supported.

# STURCTURE OF EUKARYOTIC GENE & ITS FEATURES:
 - EXONS - they are Protein Coding Sequences
 - INTRONS - non Coding Protein Sequences. Exons are intruppted by Introns.
 - Untranslated Regions (UTR) - They are at either end of the Protein Sequences. 5' UTR (5 prime UTR) at the 5' end. 3' UTR at the 3' end. 
 - Promotor region - Upstream region with various protein binds like RNA and transcription factors to initiate transcription. (i.e. to convert this gene into mRNA (a message) )  

 - These features have a Hierarchical Relationship. That means they have a parent-child relationship. 
 - They have information about genes, followed by transcripts that belong to that gene.
 - Each Transcript has features like Exons, Coding Sequences (CDS), 5' UTR, 3' UTR etc.
 
# A sample gff3 file is gff_example1.gff3 
- FIRST FEW LINES OF [gff_exxample1.gff3](./gff_example1.gff3) ARE : 

chr1	ensGene	gene	4763287	4775820	.	-	.	Name=ENSMUSG00000033845;ID=ENSMUSG00000033845;Alias=ENSMUSG00000033845;gid=ENSMUSG00000033845
chr1	ensGene	mRNA	4764517	4775779	.	-	.	Name=ENSMUST00000045689;Parent=ENSMUSG00000033845;ID=ENSMUST00000045689;Alias=ENSMUSG00000033845;gid=ENSMUSG00000033845
chr1	ensGene	CDS	4775654	4775758	.	-	0	Name=ENSMUST00000045689.cds0;Parent=ENSMUST00000045689;ID=ENSMUST00000045689.cds0;gid=ENSMUSG00000033845

# FEILDS OF GFF3 FILES :

1. Sequences id : Its the name of the Reference Sequence. This example gene belongs to Chromosome 1; it is denoted as "chr1". 
2. Source of feature : It denotes the Algorithm or Operating Procedure used to obtain the feature. It may be the software name or the database name where the feature is sourced from.
3. Feature type : it denotes the type of feature such as gene, transcript, exon, CDS, 5' UTR, 3' UTR. Gtf file has few feature types than Gff file.
4. Start Coordinates of feature
5. End Coordinates of feature
6. Score of the feature : A floating point number that represents the score of the number. If no score has been assigned, then it is represented by the dot character.
7. Strand of feature : It denotes whether the feature has a forward strand (+) of the reverse strand (-)
8. Phase of CDS feature :  it is an integer value where a complete codon begins or the number of nucleotides one has to move to get a complete codon.
9. Attributes : Information about the annotation of the features. It is stored as Tag-Value pair separated by a semi-colon. It includes information such as the feature's Id, the parent to which the feature belongs, gene type, transcript type, transcript name and any additional information.  

RESOURCES : 
https://en.wikipedia.org/wiki/Gene_structure
https://youtu.be/2Y7zxh1BiFs
