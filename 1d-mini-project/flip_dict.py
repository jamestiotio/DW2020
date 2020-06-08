# Flip dictionary utility
# Created by James Raphael Tiovalen (2020)

flipped_data = []

with open("filename.py", "r+") as f:
     data = f.readlines()
     for line in data:
         new_data = line.split(": ")
         new_data[1] = new_data[1].split("\n")[0]
         flipped_data.append("    " + new_data[1] + ": " + new_data[0] + ",\n")
     f.writelines(flipped_data)

