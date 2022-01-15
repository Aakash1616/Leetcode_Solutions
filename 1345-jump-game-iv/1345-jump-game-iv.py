class Solution:
    def minJumps(self, A):
        indices = collections.defaultdict(list)
        for i, a in enumerate(A):
            indices[a].append(i)
        done, now = {-1}, {0}
        for steps in itertools.count():
            done |= now
            if len(A) - 1 in done:
                return steps
            now = {j for i in now for j in [i-1, i+1] + indices.pop(A[i], [])} - done
        