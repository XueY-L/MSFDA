path = '/home/yxue/MSFDA/results/imagenetc-bs8/ImageNetC_ggsj_target-defocus_blur_bs8_iter10.txt'

f = open(path, 'r')

lines = f.readlines()

sum_ = 0
for l in lines:
    sum_ += float(l)
print(sum_ / len(lines))