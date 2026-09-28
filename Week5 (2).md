# Python 5주차 프로젝트 과제

이번 주 목표는 **파생변수를 만들고 그룹별 분석으로 핵심 요약표를 만드는 것**입니다.  
분석 질문에 답하기 위해 필요한 계산 기준을 직접 설계해보세요.

**필수:** 본인의 노트북에서 진행한 내용과 실행 결과를 스크린샷으로 첨부해주세요.  
👀 수행 인증샷은 필수입니다.

노트북은 반드시 위에서 아래로 순서대로 실행해주세요. 중간 셀만 실행하면 이전에 만든 변수가 없어 오류가 날 수 있습니다.

---

## 참고 교재

- 『파이썬 라이브러리를 활용한 데이터 분석』
  - 6장 데이터 로딩과 저장, 파일 형식: p.247~309
  - 7장 데이터 정제 및 준비: p.310~379
  - 10장 데이터 집계와 그룹 연산: p.381~465

---

## 이번 주 과제 목차

| 구분 | 내용 |
| --- | --- |
| 필수 1 | 파생변수 만들기 |
| 필수 2 | 그룹별 요약표 만들기 |
| 필수 3 | 피벗 테이블 만들기 |
| 필수 4 | 핵심 결과 정리 |
| 선택 | 비율 지표 만들기 |

---

<br>

<!-- 여기까진 그대로 둬 주세요-->

---

# 1️⃣ 필수 과제

먼저 지난주까지 사용한 정제 데이터를 불러오세요. 파일명은 본인의 저장 방식에 맞게 바꿔주세요.

```python
import pandas as pd

df_clean = pd.read_csv("cleaned_data.csv")
```

## 1. 파생변수 만들기

기존 컬럼을 활용해 새 컬럼을 2개 이상 만드세요. 예를 들어 매출, 비율, 구간, 연도/월 같은 변수를 만들 수 있습니다.

```python
df_clean["IncomePerYear"] = df_clean["MonthlyIncome"] * 12
df_clean["TenureRatio"] = df_clean["YearsAtCompany"] / df_clean["TotalWorkingYears"]
```

```md
파생변수 1: IncomePerYear 
의미: 월 소득을 연 소득으로 만들었다

파생변수 2: TenureRatio 
의미: 전체 경력 중 현재 회사에서 보낸 기간의 비율을 계산했다
```

## 2. 그룹별 요약표 만들기

분석 질문과 관련 있는 기준으로 데이터를 그룹화하세요. `sum()`, `mean()`, `count()` 중 데이터 성격에 맞는 함수를 사용하면 됩니다.

```python
summary = df_clean.groupby("Department")["MonthlyIncome"].mean().sort_values(ascending=False)
print(summary)
```

```md
Sales 부서가 평균 소득이 가장 높고, Research과 Development가 가장 낮음. 다만 세 부서 간 차이가 크지는 않다
```

## 3. 피벗 테이블 만들기

두 개의 기준을 동시에 비교하고 싶다면 `pivot_table()`을 사용하세요.

```python
pivot = pd.pivot_table(
    df_clean,
    values="MonthlyIncome",
    index="Department",
    columns="Attrition",
    aggfunc="mean"
)
print(pivot)
```
 


## 4. 핵심 결과 정리

이번 주 요약표가 분석 질문에 어떤 답을 주는지 정리하세요.

```md
가장 중요한 요약표: Department x Attrition 피벗 테이블

-> 부서와 무관하게 이직자의 평균 소득이 재직자보다 낮고, Human Resources에서 그 격차가 가장 크게 나타났다

-> 소득 수준이 낮을수록 이직 가능성이 높다는 경향이 부서 전반에서 확인된다
```

---

# 2️⃣ 선택 과제

단순 합계나 평균이 아니라 비율 지표를 만들어보세요. 예를 들어 전체 대비 비중, 전환율, 단가, 평균 금액 등이 될 수 있습니다.

```python
ratio = df_clean["MonthlyIncome"] / df_clean["MonthlyIncome"].sum()
print(ratio.head())
```

```md
전체 소득 총합 대비 각 직원 소득이 차지하는 비중을 계산했다. 특정 직원의 소득이 극단적으로 큰지 확인할 수 있다
```

---

# 3️⃣ 제출 체크리스트

- [v] 파생변수 2개 이상을 만들었다.
- [v] `groupby` 요약표를 1개 이상 만들었다.
- [v] `pivot_table`을 1개 이상 만들었다.
- [v] 요약표를 바탕으로 핵심 결과를 작성했다.

🎉 수고하셨습니다.  
다음 주에는 분석 결과를 그래프로 표현하고, 인사이트를 더 명확하게 정리합니다.
