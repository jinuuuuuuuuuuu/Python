# Python 2주차 프로젝트 과제

이번 주 목표는 **데이터를 자세히 살펴보고 데이터 명세서를 작성하는 것**입니다.  
단순히 함수를 실행하는 데서 끝내지 말고, 각 컬럼이 분석에서 어떤 의미를 갖는지 정리하세요.

**필수:** 본인의 노트북에서 진행한 내용과 실행 결과를 스크린샷으로 첨부해주세요.  
👀 수행 인증샷은 필수입니다.

노트북은 반드시 위에서 아래로 순서대로 실행해주세요. 중간 셀만 실행하면 이전에 만든 변수가 없어 오류가 날 수 있습니다.

---

## 참고 교재

- 『파이썬 라이브러리를 활용한 데이터 분석』
  - 5장 판다스 시작하기: p.181~246
  - 6장 데이터 로딩과 저장, 파일 형식: p.247~309

---

## 이번 주 과제 목차

| 구분 | 내용 |
| --- | --- |
| 필수 1 | 데이터 불러오기 |
| 필수 2 | 기본 구조 확인 |
| 필수 3 | 컬럼 명세서 작성 |
| 필수 4 | 분석 활용 컬럼 선정 |
| 필수 5 | 데이터 이해 메모 |
| 선택 | 데이터 품질 메모 추가 |

---

<br>

<!-- 여기까진 그대로 둬 주세요-->

---

# 1️⃣ 필수 과제

## 1. 데이터 불러오기

1주차에 선택한 데이터셋을 불러오세요. 파일 경로는 본인 폴더 구조에 맞게 조정하면 됩니다.

```python
import pandas as pd

df = pd.read_csv("파일경로.csv")
```

## 2. 기본 구조 확인

아래 코드를 실행해 데이터의 크기, 앞부분, 컬럼명, 데이터 타입을 확인하세요.

```python
print(df.head()): 처음 5개 행
print(df.shape): 전체 행과 열
print(df.info()): 각 컬럼의 데이터 타입과 결측치 여부
print(df.describe()):수치형컬럼에 대한 통계 요약(최대값, 최소값, 평균 등)
print(df.columns): 모든 컬럼 목록
```

## 3. 컬럼 명세서 작성

주요 컬럼 8개 이상을 골라 명세서를 작성하세요. 모든 컬럼을 설명할 수 있다면 더 좋습니다.

```md
| 컬럼명 | 데이터 타입 | 의미 | 예시 값 | 분석에서 사용할 가능성 |
| --- | --- | --- | --- | --- |
| MonthlyIncome | int64 | 월 소득 | 5993 | 높음 |
| DistanceFromHome | int64 | 집-회사 간 거리 | 1 | 높음 |
| EnvironmentSatisfaction | int64 | 근무 환경 만족도 (1~4) | 2 | 높음 |
| JobInvolvement | int64 | 업무 몰입도 (1~4) | 3 | 높음 |
| JobSatisfaction | int64 | 직무 만족도 (1~4) | 4 | 높음 |
| WorkLifeBalance | int64 | 워라밸 만족도 (1~4) | 1 | 높음 |
| TotalWorkingYears | int64 | 총 경력 연수 | 8 | 높음 |
| YearsAtCompany | int64 | 현 회사 근속 연수 | 6 | 높음 |
| JobLevel | int64 | 직급 (1~5) | 2 | 중간 |
| MaritalStatus | object | 결혼 여부 (Single/Married/Divorced) | Single | 중간 |
| OverTime | object | 초과 근무 여부 (Yes/No) | Yes | 중간 |
| RelationshipSatisfaction | int64 | 대인관계 만족도 (1~4) | 1 | 중간 |
```

데이터 타입은 `int64`, `float64`, `object`, `bool`처럼 `info()` 결과에 나온 값을 적으면 됩니다.

## 4. 분석 활용 컬럼 선정

1주차 분석 질문에 답하기 위해 꼭 필요해 보이는 컬럼을 정리하세요.

```md
핵심 컬럼: Attrition, MonthlyIncome, OverTime, JobSatisfaction, WorkLifeBalance, TotalWorkingYears, YearsAtCompany
보조 컬럼: DistanceFromHome, EnvironmentSatisfaction, JobInvolvement, JobLevel, MaritalStatus, RelationshipSatisfaction
사용하지 않을 것 같은 컬럼: EmployeeCount, Over18, StandardHours, EmployeeNumber
제외 이유: EmployeeCount, Over18, StandardHours는 전체 행에서 값이 1종류뿐이라 정보량이 없고, EmployeeNumber는 직원 고유 ID로 통계적 의미가 없어 분석 변수로 사용하지 않음
```

## 5. 데이터 이해 메모

데이터를 처음 살펴보고 알게 된 점을 정리하세요. 아직 분석 결과가 아니어도 괜찮습니다.

```md
관찰한 점 1: 전체 1470명, 35개 컬럼으로 구성된 IBM HR Attrition 데이터셋이며 결측치는 하나도 없음
관찰한 점 2: EmployeeCount, Over18, StandardHours는 모든 행의 값이 동일해 분석에 쓸 수 없고, EmployeeNumber는 값이 1470종류로 단순 식별자에 해당함
분석 전에 더 확인해야 할 점: 만족도·몰입도 관련 컬럼(EnvironmentSatisfaction, JobSatisfaction 등)이 1~4 척도의 순서형 데이터인지, 수치형처럼 다뤄도 되는지 확인 필요
```

---

# 2️⃣ 선택 과제

데이터 품질을 미리 점검해보세요. 결측치나 이상해 보이는 값이 있는지 간단히 메모하면 3주차 전처리 계획을 세우기 쉬워집니다.

```python
print(df.isna().sum())
print(df.nunique())
```

```md
결측치가 있어 보이는 컬럼: 없음 
값의 종류가 너무 많거나 적은 컬럼: EmployeeCount, Over18, StandardHours- 값 1종류 / EmployeeNumber- 값 1470종류
품질 확인이 더 필요한 컬럼: 별도로 없다
```

---

# 3️⃣ 제출 체크리스트

- [ v] 데이터를 불러왔다.
- [ v] `head()`, `shape`, `info()`, `describe()` 결과를 첨부했다.
- [ v] 주요 컬럼 8개 이상에 대한 명세서를 작성했다.
- [ v] 분석에 사용할 핵심 컬럼을 선정했다.
- [ v] 데이터 이해 메모를 작성했다.

🎉 수고하셨습니다.  
다음 주에는 데이터의 결측치, 중복, 이상치를 점검하고 전처리 기준을 세웁니다.
