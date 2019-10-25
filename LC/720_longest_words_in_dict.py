class Solution:
    def longestWord(self, words) -> str:
        
        # Create a dictionary of words
        # words_dict[str] == True only when 'str' can be build by other words
        words_dict = {}
        for word in words:
            words_dict[word] = False
        
        res = ''
        for word in words_dict:
            
            # Check from the largest substring to smallest
            for idx in range(len(word),0,-1):
                
                # only continue checking if substring is in the dict
                if word[0:idx] in words_dict:
                    
                    # If the current substring can be built from other words or the current substring is smallest, then the word can be built from other words
                    if words_dict[word[0:idx]] == True or idx == 1:
                        words_dict[word] = True
                        
                        # Condition to replace the current result, first compare the length
                        # then compare lexicographly
                        if len(word) > len(res):
                            res = word
                        elif len(word) == len(res) and word < res:
                            res = word
                            
                        break
                else:
                    break
                    
        return res
                
                
                    
                    
        
        