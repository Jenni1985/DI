# Write a Python class to get all possible unique subsets from a set of distinct integers.

# import itertools
#
# stuff = [5, 6, 7, 8]
#
# for L in range(0, len(stuff) + 1):
#     for subset in itertools.permutations(stuff, L):
#         print(subset)

# Write a Python class to find the three elements that sum to zero from a set of n real numbers.

class Subsets:
    def __init__(self,list):
        self.list = list

    def triplets(self):
        for i in range(len(self.list) - 2):
            for j in range(1,len(self.list) - 1):
                for k in range(2,len(self.list)):

                    if (self.list[i] + self.list[j] + self.list[k]) == 0:
                        print(self.list[i], self.list[j], self.list[k])



# ---------------------------------------------------- main
mylist = [-25, -10, -7, -3, 2, 4, 8, 10]

s = Subsets(mylist)
s.triplets()