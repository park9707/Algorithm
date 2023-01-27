def solution(cards):
    boxes = {index + 1: card for index, card in enumerate(cards)}  # 카드의 순서 : 카드의 값으로 딕셔너리 생성
    groups = []
    while boxes:
        visited = set()  # 방문 초기화
        pos = list(boxes.keys())[0]  # 박스의 첫번째 키를 담음
        while pos not in visited:  # 방문하지 않았다면
            visited.add(pos)  # 방문 처리
            temp = boxes[pos]  # 임시 변수에 다음 인덱스 담기
            del boxes[pos]  # 박스에서 인덱스 pos 제거
            pos = temp  # pos에 다음 인덱스 값 담기
        groups.append(len(visited))  # 그룹의 길이 담기
    groups.sort(reverse = True)  # 길이를 담은 groups를 내림차순으로 정렬
    return groups[0] * groups[1] if len(groups) > 1 else 0  # 그룹이 2개 이상 나온다면 곱해서 리턴, 아니라면 0을 리턴

print(solution([8,6,3,7,2,5,1,4]))