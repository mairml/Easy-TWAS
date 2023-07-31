
import glob
import subprocess

path = r'./supercent/WEIGHTS/*.pos'
files = glob.glob(path)

tissues=[]
for f in files:
	file=f.split(".")
	tissues.append(file[3])
print(tissues)

for CHR_NUM in range(23,24):
	CHR_NUM=str(CHR_NUM)
	for TISSUE in tissues:
		print("Running chr"+CHR_NUM+" for "+TISSUE)
		cmd1="Rscript FUSION.assoc_test.R  --sumstats ./supercent/aging_GWAS_allData.tsv "
		cmd3="--weights ./supercent/WEIGHTS/GTExv8.EUR."+TISSUE+".pos  "
		cmd4="--weights_dir ./supercent/WEIGHTS/  "
		cmd5="--ref_ld_chr ./LDREF/1000G.EUR.  "
		cmd6="--chr "+CHR_NUM+" "
		cmd7="--out ./cent_TWAS_output/cent"+TISSUE+CHR_NUM+".dat"
		cmd_str=cmd1+cmd3+cmd4+cmd5+cmd6+cmd7
		subprocess.run(cmd_str, shell=True)

#Rscript FUSION.assoc_test.R --sumstats ./supercent/PGC2.SCZ.sumstats --weights ./supercent/WEIGHTS/GTExv8.EUR.Whole_Blood.pos --weights_dir ./supercent/WEIGHTS/ --ref_ld_chr ./LDREF/1000G.EUR. --chr 22 --out PGC2.SCZ.22.dat



