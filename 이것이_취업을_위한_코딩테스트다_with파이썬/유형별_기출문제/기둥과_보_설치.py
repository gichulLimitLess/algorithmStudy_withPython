# 기둥과 보 설치
# ---> 어떻게 하면 쉽게 풀 수 있을까..에 대해서 고민이 많이 필요함
# "오답노트" -> 이걸 무식하게 보드 2개 만들어서 풀려 했던 내 잘못이 많이 큼..

# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
  for x, y, stuff in answer:
    if stuff == 0: # 설치된 것이 '기둥'인 경우
      # '바닥 위' 혹은 '보의 한 쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
      if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
        continue
      return False # 아니면 거짓 반환
    elif stuff == 1: # 설치된 것이 '보'인 경우
      # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
      if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
        continue
      return False # 아니라면 거짓 반환
    return True

def solution(n, build_frame):
  answer = []
  for frame in build_frame: # 작업의 갯수는 최대 1000개
    x, y, stuff, operate = frame
    if operate == 0: # 삭제하는 경우
      answer.remove([x, y, stuff]) # 일단 삭제를 해봐
      if not possible(answer): # 가능하지 않으면
        answer.append([x, y, stuff]) # 다시 빠꾸
    if operate == 1:
      answer.append([x, y, stuff]) # 일단 설치를 해봐
      if not possible(answer): # 가능하지 않으면
        answer.remove([x, y, stuff]) # 다시 빠꾸
  
  return sorted(answer) # 오름차순 정렬 이렇게 해도 된다