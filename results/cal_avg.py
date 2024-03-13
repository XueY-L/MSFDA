path = '/home/yxue/MSFDA/results/ImageNetC_ggsj_target-brightness_bs8_iter10.txt'

f = open(path, 'r')

lines = f.readlines()

sum_ = 0
for l in lines:
    sum_ += float(l)
print(sum_ / len(lines))