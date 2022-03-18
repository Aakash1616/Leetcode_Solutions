class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c : i for i, c in enumerate(s)}
        st = ["!"]
        visited = set() 
        
        for i, ch in enumerate(s):
            if ch in visited: continue 
            
            while(ch < st[-1] and last_occ[st[-1]]>i):
                visited.remove(st.pop()) 
                
            visited.add(ch)  
            st.append(ch) 
        return "".join(st[1:])