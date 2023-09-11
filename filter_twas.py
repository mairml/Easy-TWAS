#MAIR M L
#BOTAS LAB USE

#Script runs through TWAS output files and will filter by significant, count number of tissues variant is significant
#All tissues and brain tissues
#####EDIT HERE#########

pvalcutoff=0.00001 #pval cutoff
path = r'./cent_TWAS_output/*' #path to TWAS outputs
outfile=open("supercent_TWAS_summary.tsv",'w') #output
######################

import glob
import subprocess

#Function to remove duplicates
def unique(list1):
 
    unique_list = []
 
    #go through all elements
    for x in list1:
    #check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        return(x)
 

files = glob.glob(path)

fileList=[]
for f in files:
	fileList.append(f)

#File Format:
#GENE Tissue GWASrs TWASrs GWASz TWASz Pval 


tcount={}#tissue count
bcount={}#brain tissue count
store=[]#output storage
for f in files: #go through all TWAS files
	data_file=open(f,'r')
	next(data_file)
	for l in data_file:
		l = l.strip()
		line = l.split("\t")
		gene= line[2]
		tissue = line[0]
		chrom=line[3]
		pos0 = line[4]
		pos1 = line[5]
		SNP=chrom+"_"+pos0
		GWASrs= line[7]
		GWAS_z=line[8]
		eQTLrs=line[9]
		TWASz=line[18]
		TWASp=line[19]
		try:
			if float(TWASp)<pvalcutoff:
				output=SNP+"\t"+gene+"\t"+tissue+"\t"+chrom+"\t"+pos0+"\t"+pos1+"\t"+GWASrs+"\t"+eQTLrs+"\t"+TWASz+"\t"+TWASp
				store.append(output)
				#Count number of tissues hit appears in
				if GWASrs not in tcount:
					tcount[GWASrs]=[tissue]
				else:
					tcount[GWASrs].append(tissue)
				if "Brain" in f:
					if GWASrs not in bcount:
						bcount[GWASrs]=[tissue]
					else:
						bcount[GWASrs].append(tissue)
				else:
					pass #don't count as brain tissue 
		except:
			pass

outfile.write("SNP\tGene\tTissue\tChr\tP1\tP2\tGWASrs\teQTLrs\tTWASz\tTWASp\tTissueCount\tTissues\tBrainTissueCount\tBrainTissues\n")
print(bcount)
for i in store:
	g=i.split("\t") #line data
	geneid=g[6] #gene GWASrs
	tissueIDs=set(tcount[geneid]) #format to count tissues
	tissueNum=len(tissueIDs) #tissue count
	if geneid in bcount.keys():
		brainIDs=set(bcount[geneid]) #format to count brain tissues
		brainNum=len(brainIDs) #brain tissue count
	else:
		brainIDs="NA" #don't count brain tissues is no brain tissues present
		brainNum=0
	tissueID=""
	for t in tissueIDs:
		tissueID=tissueID+t+"/" #format to print
	brainID=""
	for b in brainIDs: #format to print
		brainID=brainID+b+"/"
	out=i+"\t"+str(tissueNum)+"\t"+tissueID+"\t"+str(brainNum)+"\t"+brainID+"\n"
	outfile.write(out)


data_file.close()
outfile.close()
