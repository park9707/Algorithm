class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter,digit=[],[]
        for i in logs:
            if i.split()[1].isdigit():
                digit.append(i)
            else:
                letter.append(i)
        
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letter+digit
