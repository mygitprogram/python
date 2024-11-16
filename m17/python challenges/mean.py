# the mean of 40 numbers is 38 and i misread 56 as 36. find the correct mean

total_numbers = 40
mean = 38

total = total_numbers* mean

cor_num = 56
num_ent = 36
diff = cor_num-num_ent

cor_tot = total + diff
cor_mean = cor_tot/total_numbers
print("the correct Mean is",cor_mean)