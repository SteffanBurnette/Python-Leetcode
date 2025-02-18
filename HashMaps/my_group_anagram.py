class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use a hashmap to store the key which is the sorted string and the append index location (the value)
        #Will need to account for the string not existing

      my_dict = {}  # Will hold the location for each key
      dub_ary = []  # Will hold the groups
     
      for i in strs:
        key = ''.join(sorted(i))
        if key in my_dict:
            dub_ary[my_dict[key]].append(i)
        else:
             # The new index for the new key is the current length of dub_ary
            my_dict[key] = len(dub_ary)
            dub_ary.append([i])
                
      return dub_ary


