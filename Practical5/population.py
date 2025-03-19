import matplotlib.pyplot as plt

uk=[57.11,3.13,1.91,5.45]# sort uk countries
ukname=["England","Wales","Northern Ireland","Scotland"]
dictuk={ukname[i]:uk[i] for i in range(len(uk))}
sorteduk=sorted(dictuk.items(),key=lambda x:x[1])
print("origin data:",dictuk)
print("after sorted:",sorteduk)

cn=[65.77,41.88,45.28,61.27,85.15]# sort cn provinces
cnname=["Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"]
dictcn={cnname[i]:cn[i] for i in range(len(cn))}
sortedcn=sorted(dictcn.items(),key=lambda x:x[1])
print("origin data:",dictcn)
print("after sorted:",sortedcn)

plt.figure(1)#draw figure one
plt.subplot(1,2,1)
plt.pie(uk,labels=ukname,autopct="%0.2f%%")
plt.title("UK Countries Distribution")

plt.subplot(1,2,2)#draw figure two
plt.pie(cn,labels=cnname,autopct="%0.2f%%")
plt.title("CN Provinces Distribution")

plt.show()# show the figure