class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        dict = {}
        for word in words:
            dict[word] = dict.get(word , 0) + 1
        result = []
        for word , count in dict.items():
            result.append((-count , word))
        result.sort()
        answer = []
        for count , word in result[:k]:
            answer.append(word)
        return answer        
            
             