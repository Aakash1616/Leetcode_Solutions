class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c : i for i, c in enumerate(s)}
        st = ["!"]
        visited = [0]*26 
        
        for i, ch in enumerate(s):
            if visited[ord(ch)-97]: continue 
            
            while(ch < st[-1] and last_occ[st[-1]]>i):
                visited[ord(st.pop())-97] = 0 
                
            visited[ord(ch)-97] = 1 
            st.append(ch) 
        return "".join(st[1:])