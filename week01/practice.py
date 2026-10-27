"""
1주차 실습: Python 기초 다지기

각 함수의 `pass`를 지우고 직접 코드를 작성하세요.
다 쓰면 터미널에서 `python week01/check.py`로 채점합니다.

규칙: 문제에 '금지'라고 적힌 내장 함수는 쓰지 마세요. (원리를 익히기 위한 연습입니다)
"""


# 문제 1. 합계
# nums: 숫자 리스트 (예: [3, 5, 2])
# 반환: 모든 수의 합 (예: 10)
# 금지: sum()
def total(nums):
    count = 0
    for n in nums:
        count = count + n

    return count


# 문제 2. 평균
# nums: 숫자 리스트 (비어 있지 않음)
# 반환: 산술평균 (예: [2, 4, 6] -> 4.0)
# 금지: sum(), statistics 모듈
def mean(nums):
    pass


# 문제 3. 최댓값
# nums: 숫자 리스트 (비어 있지 않음, 음수가 섞일 수 있음)
# 반환: 가장 큰 값
# 금지: max(), sorted(), .sort()
def maximum(nums):
    pass


# 문제 4. 짝수만 골라내기
# nums: 정수 리스트
# 반환: 짝수만 원래 순서대로 담은 새 리스트 (예: [1, 2, 3, 4] -> [2, 4])
def evens(nums):
    pass


# 문제 5. 점수 -> 등급
# score: 0~100 사이 정수
# 반환: 90 이상 'A', 80 이상 'B', 70 이상 'C', 그 외 'F'
def grade(score):
    pass


# 문제 6. 단어 빈도 세기
# words: 문자열 리스트 (예: ['a', 'b', 'a'])
# 반환: {단어: 개수} 딕셔너리 (예: {'a': 2, 'b': 1})
# 금지: collections.Counter, list.count()
def word_count(words):
    pass


# 문제 7. 값이 가장 큰 key 찾기
# d: {이름: 숫자} 딕셔너리 (비어 있지 않음, 최댓값은 하나뿐)
# 반환: 값이 가장 큰 항목의 key (예: {'kim': 70, 'lee': 95} -> 'lee')
# 금지: max()
def top_key(d):
    pass


# 문제 8. 중앙값
# nums: 숫자 리스트 (비어 있지 않음, 정렬 안 되어 있음)
# 반환: 중앙값
#   - 개수가 홀수면 가운데 값          (예: [3, 1, 2] -> 2)
#   - 개수가 짝수면 가운데 두 값의 평균 (예: [4, 1, 3, 2] -> 2.5)
# 허용: sorted()
def median(nums):
    pass


# 문제 9. 분산 (모분산)
# nums: 숫자 리스트 (비어 있지 않음)
# 반환: 각 값에서 평균을 뺀 것을 제곱해서 평균 낸 값
#   예: [2, 4, 4, 4, 5, 5, 7, 9] -> 평균 5, 분산 4.0
# 허용: 위에서 만든 mean() 함수
def variance(nums):
    pass


# 문제 10. 결측치(None)를 빼고 평균
# values: 숫자와 None이 섞인 리스트 (숫자가 최소 1개는 있음)
# 반환: None을 제외한 숫자들의 평균 (예: [10, None, 20] -> 15.0)
def mean_skip_none(values):
    pass


# 직접 결과를 확인해 보는 곳 (자유롭게 수정하세요)
if __name__ == "__main__":
    print(total([3, 5, 2]))
    print(mean([2, 4, 6]))
    print(word_count(["사과", "배", "사과"]))
