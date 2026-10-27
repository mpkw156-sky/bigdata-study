"""
1주차 자동 채점기

실행: python week01/check.py
이 파일은 수정하지 마세요.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import practice as p  # noqa: E402


def same(a, b):
    if isinstance(a, float) or isinstance(b, float):
        try:
            return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
        except TypeError:
            return False
    return a == b


# (문제 번호, 이름, 함수 이름, [(입력값들, 기대값), ...])
CASES = [
    (1, "합계", "total", [
        (([3, 5, 2],), 10),
        (([-4, 10, 0],), 6),
        (([7],), 7),
    ]),
    (2, "평균", "mean", [
        (([2, 4, 6],), 4.0),
        (([1, 2],), 1.5),
        (([-3, 3, 9],), 3.0),
    ]),
    (3, "최댓값", "maximum", [
        (([3, 9, 2],), 9),
        (([-5, -2, -8],), -2),
        (([4],), 4),
    ]),
    (4, "짝수 골라내기", "evens", [
        (([1, 2, 3, 4],), [2, 4]),
        (([1, 3, 5],), []),
        (([0, -2, 7, 8],), [0, -2, 8]),
    ]),
    (5, "점수 -> 등급", "grade", [
        ((95,), "A"), ((90,), "A"), ((89,), "B"),
        ((80,), "B"), ((70,), "C"), ((69,), "F"), ((0,), "F"),
    ]),
    (6, "단어 빈도", "word_count", [
        ((["a", "b", "a"],), {"a": 2, "b": 1}),
        ((["사과", "배", "사과", "사과"],), {"사과": 3, "배": 1}),
        (([],), {}),
    ]),
    (7, "값이 가장 큰 key", "top_key", [
        (({"kim": 70, "lee": 95},), "lee"),
        (({"a": -3, "b": -1, "c": -7},), "b"),
        (({"only": 1},), "only"),
    ]),
    (8, "중앙값", "median", [
        (([3, 1, 2],), 2),
        (([4, 1, 3, 2],), 2.5),
        (([10],), 10),
        (([5, 5, 1, 9, 7],), 5),
    ]),
    (9, "분산", "variance", [
        (([2, 4, 4, 4, 5, 5, 7, 9],), 4.0),
        (([1, 1, 1],), 0.0),
        (([1, 3],), 1.0),
    ]),
    (10, "결측치 빼고 평균", "mean_skip_none", [
        (([10, None, 20],), 15.0),
        (([None, None, 6],), 6.0),
        (([1, 2, 3],), 2.0),
    ]),
]


def run():
    passed = 0
    print("=" * 44)
    print(" 1주차 채점 결과")
    print("=" * 44)
    for num, name, fname, tests in CASES:
        func = getattr(p, fname)
        status = "정답"
        detail = ""
        for args, expected in tests:
            # 입력이 함수 안에서 바뀌어도 다음 테스트에 영향이 없도록 복사
            safe_args = tuple(a.copy() if hasattr(a, "copy") else a for a in args)
            try:
                got = func(*safe_args)
            except Exception as e:  # noqa: BLE001
                status = "에러"
                detail = f"입력 {args} 에서 {type(e).__name__}: {e}"
                break
            if got is None and expected is not None:
                status = "미완성"
                detail = "None이 반환됨 (return을 썼는지 확인)"
                break
            if not same(got, expected):
                status = "오답"
                detail = f"입력 {args} -> 내 답: {got!r}"
                break
        if status == "정답":
            passed += 1
        mark = {"정답": "O", "오답": "X", "에러": "!", "미완성": "-"}[status]
        print(f" [{mark}] 문제 {num:>2}. {name:<12} {status}")
        if detail:
            print(f"       {detail}")
    print("-" * 44)
    print(f" 점수: {passed} / {len(CASES)}")
    if passed == len(CASES):
        print(" 1주차 완료! 'git push'로 올리고 오답 분석을 요청하세요.")
    print("=" * 44)


if __name__ == "__main__":
    run()
