class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        nbr = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nbr[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nbrWord in nbr[pattern]:
                        if nbrWord not in visited:
                            visited.add(nbrWord)
                            q.append(nbrWord)
            res += 1

        return 0


        