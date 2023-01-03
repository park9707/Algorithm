import re
def solution(files):
    arr = [re.split(r'(\d{1,5})', i) for i in files]
    arr = sorted(arr, key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(i) for i in arr]