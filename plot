f = open("data.asc")
# with open(filename) as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

X_array = []

B = []

for line in f:
     if (len(line)) == 36:
        # line = line.replace("\n","")
        # line = line.replace("\t","")
        # B.append(line.split("   "))
        B.append(line)

# for line in B:
#     print(B)     

X_array.append(B[2])
# print(X_array)

# Y_array

# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_title('Eye Tracker Data')

# ax.plot(f)
