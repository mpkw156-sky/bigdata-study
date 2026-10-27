# 1주차: Python 기초 다지기 (데이터 분석용)

> 단계: 0. 준비 · 빅분기 연결: 실기 공통 기초 (pandas를 쓰기 전 체력 만들기)

이번 주 목표는 **pandas 없이 순수 Python으로** 평균·최댓값·빈도 같은 기초 통계를 직접 계산해 보는 것입니다.
나중에 pandas가 `df.mean()` 한 줄로 해 주는 일이 안에서 어떻게 돌아가는지 이해하게 됩니다.

## 이번 주 순서 (약 5시간)

| 세션 | 할 일 |
| --- | --- |
| 평일 1 (1시간) | 아래 "개념 정리" 읽고 예제 직접 쳐 보기 |
| 평일 2 (1시간) | `practice.py` 문제 1~5 |
| 평일 3 (1시간) | `practice.py` 문제 6~10 |
| 주말 (2시간) | 틀린 문제 다시 풀기 + claude.ai에서 오답 분석 요청 |

## 개념 정리

### 1. 리스트: 여러 값을 순서대로 담기

```python
scores = [80, 92, 75, 64]
print(scores[0])     # 80  (첫 번째, 0부터 셈)
print(scores[-1])    # 64  (마지막)
print(len(scores))   # 4   (개수)
scores.append(100)   # 맨 뒤에 추가
```

### 2. 반복문: 하나씩 꺼내서 처리하기

```python
total = 0
for s in scores:
    total = total + s   # total += s 와 같음
print(total)
```

**누적 변수 패턴**: "0에서 시작해서 하나씩 더해 간다"는 이 모양은 이번 주 문제의 절반에 나옵니다.

### 3. 조건문: 경우에 따라 다르게

```python
x = 7
if x % 2 == 0:       # %는 나머지
    print("짝수")
elif x > 5:
    print("5보다 큰 홀수")
else:
    print("그 외")
```

### 4. 딕셔너리: 이름표(key)로 값 찾기

```python
count = {}
for fruit in ["사과", "배", "사과"]:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1
print(count)   # {'사과': 2, '배': 1}
```

빈도(개수) 세기는 빅분기 실기 1유형의 단골입니다. pandas에서는 `value_counts()`가 이 일을 합니다.

### 5. 함수: 자주 쓰는 계산에 이름 붙이기

```python
def double(x):
    return x * 2

print(double(5))   # 10
```

`return`이 없으면 함수는 `None`을 돌려줍니다. 채점에서 "미완성"이 뜨면 대부분 `return`을 빠뜨린 경우입니다.

### 6. None: "값이 없음"

```python
values = [10, None, 30]
for v in values:
    if v is None:      # None은 == 대신 is 로 비교
        continue       # 이번 것은 건너뛰기
    print(v)
```

데이터 분석에서는 이것을 **결측치**라고 부릅니다. 2주 뒤 pandas에서 `NaN`으로 다시 만납니다.

## 문제 목록 (`practice.py`)

| 번호 | 함수 | 하는 일 | 규칙 |
| --- | --- | --- | --- |
| 1 | `total(nums)` | 합계 | `sum()` 금지 |
| 2 | `mean(nums)` | 평균 | `sum()`, `statistics` 금지 |
| 3 | `maximum(nums)` | 최댓값 | `max()` 금지 |
| 4 | `evens(nums)` | 짝수만 골라 새 리스트 | |
| 5 | `grade(score)` | 점수 → 등급(A/B/C/F) | |
| 6 | `word_count(words)` | 단어별 개수 딕셔너리 | `Counter` 금지 |
| 7 | `top_key(d)` | 값이 가장 큰 key | `max()` 금지 |
| 8 | `median(nums)` | 중앙값 | `sorted()` 사용 가능 |
| 9 | `variance(nums)` | 분산(모분산) | 위에서 만든 `mean()` 사용 가능 |
| 10 | `mean_skip_none(values)` | None을 빼고 평균 | |

"금지" 규칙은 원리를 이해하기 위한 것입니다. 실제 분석과 시험에서는 `sum()`, `max()`를 마음껏 쓰면 됩니다.

## 채점

```bash
python week01/check.py
```

모든 문제가 `정답`이 나오면 이번 주 완료입니다.
