# given two strings, write a methods to decide if one is a permutaion of the other

""" Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba"). """

""" Input:s1= "ab" s2 = "eidboaoo"
    Output: False """


class Permutation:
    def checkPermutation(self, s1: str, s2: str) -> bool:
        self.string1 = s1
        self.string2 = s2

        if self.string1[::-1] or self.string1 in self.string2:
            return True
        else:
            return False


if __name__ == '__main__':
    perm = Permutation()
    # print(perm.checkPermutation('ab', 'eidbaooo'))
    print(perm.checkPermutation('ab', 'eidboaoo'))
