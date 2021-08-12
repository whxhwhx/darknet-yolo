import random

out = open("shuffle_main\\test.txt", 'w')
lines=[]
with open("test.txt", 'r') as infile:
    for line in infile:
        lines.append(line)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
    for line in lines:
        out.write(line)

out = open("shuffle_main\\train.txt", 'w')
lines = []
with open("train.txt", 'r') as infile:
    for line in infile:
        lines.append(line)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
    for line in lines:
        out.write(line)

out = open("shuffle_main\\trainval.txt", 'w')
lines = []
with open("trainval.txt", 'r') as infile:
    for line in infile:
        lines.append(line)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
    for line in lines:
        out.write(line)

out = open("shuffle_main\\val.txt", 'w')
lines = []
with open("val.txt", 'r') as infile:
    for line in infile:
        lines.append(line)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
        random.shuffle(lines)
    for line in lines:
        out.write(line)