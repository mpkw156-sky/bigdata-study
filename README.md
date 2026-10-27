# bigdata-study

Python 데이터 분석 실력을 쌓으면서 빅데이터분석기사(빅분기) 필기·실기 범위를 함께 공부하는 개인 실습 저장소입니다.

## 폴더 구조

```
bigdata-study/
├── CLAUDE.md        # Claude Code가 지킬 규칙 (정답 대신 써주지 않기 등)
├── 오답노트.md       # 틀린 문제와 원인 분석 누적 기록
├── requirements.txt # 필요한 Python 패키지
└── weekNN/          # 주차별 실습
    ├── README.md    # 이번 주 개념 정리 + 문제 설명
    ├── practice.py  # 내가 직접 코드를 채우는 파일
    └── check.py     # 실행하면 자동 채점
```

## 공부하는 방법

1. **시작할 때**: Claude Code에서 "최신으로 받아줘" → `git pull`
2. **읽기**: `weekNN/README.md`로 개념 확인
3. **풀기**: `weekNN/practice.py`의 `pass` 자리를 **직접** 채우기
4. **채점**: `python weekNN/check.py` 실행 (Claude Code에 "채점 돌려줘"라고 해도 됨)
5. **끝낼 때**: Claude Code에서 "오늘 한 거 올려줘" → `git push`
6. **오답 분석**: claude.ai '공부' 프로젝트 대화창에서 "N주차 채점하고 오답 분석해줘"

## 처음 한 번만: PC 준비

Claude Code에 아래처럼 말하면 됩니다.

> 이 저장소에 필요한 Python 환경을 준비해줘. requirements.txt에 있는 패키지를 설치해줘.

## 로드맵

전체 학습 로드맵은 claude.ai의 '데이터 분석 × 빅데이터분석기사 학습 로드맵' 문서에 있습니다.
