import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# first get all sequence contain "GT" and "AG"
result = re.findall(r'GT\S+AG', seq)

# find the longest sequence in the list
large=result[0]
for i in result:
    if len(i)>len(large):
        large = i
print(large)
