"""Read and merge 2 CSV files and write them in a single file. For example, the first CSV can have 
employee details, and the second one can have their number of experiences (one-to-one 
relationship)."""

import pandas

csvfile1 = input("enter the csv file name")
csvfile2 = input("enter the csv file name")


#option = input("enter the ypur option 1->left ,2->rigth, 3->inner")

file1 = pandas.read_csv(csvfile1)
file2 = pandas.read_csv(csvfile2)

#if option.lower() is 'left':
mergefile = pandas.merge(left = file1,right = file2, on = 'ROLLno', how = 'inner')
mergefile.to_csv("final.csv")
