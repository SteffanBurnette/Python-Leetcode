class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        my_hash = {} #My hash map
       
        
        for i in range(len(strs)):
            temp_ana = []
            print("".join(sorted(strs[i])))
            for j in range(len(strs)):
                if sorted(strs[i]) == sorted(strs[j]) and "".join(sorted(strs[i])) not in my_hash:
                    temp_ana.append(strs[j])
            if len(temp_ana) >= 1:
                anagrams.append(temp_ana)
            my_hash["".join(sorted(strs[i]))] = True
           


        return anagrams
