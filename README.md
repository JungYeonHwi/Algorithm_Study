# 그리디/탐욕 알고리즘 (Greedy Algorithm)

## 이론

- 선택의 순간인 각 단계에서 찾을 수 있는 가장 최적의 방법 선택
- 지금의 선택이 앞으로 남은 선택들에 어떠한 영향을 끼치는지 고려하지 않음
- 알고리즘의 결과가 최적임을 알리는 것을 정당성 증명
- 선택마다의 값은 그 순간에서 최적(지역적 최적)일수 있지만, 그 선택들을 반복하여 수집하였다고 해도 최종적인 정답(전역적인 정답)을 만들었다는 보장 없음
- 그러나 그리디 알고리즘을 적용할 수 있는 문제들은 최적이면서 전역적으로 최적인 문제들

## 알고리즘 적용 조건

1. 탐욕적 선택 속성(Greedy Choice Property) : 앞의 선택이 이후의 선택에 영향을 주지 않음
2. 최적 부분 구조(Optimal Substructure) : 문제에 대한 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성

## 해결 방법

1. 선택 절차(Selection Procedure) : 현재 상태에서의 최적의 해답을 선택
2. 적절성 검사(Feasibility Check) : 선택된 해가 문제의 조건을 만족하는지 검사
3. 해답 검사(Solution Check): 원래의 문제가 해결되었는지 검사하고, 해결되지 않았다면 선택 절차로 돌아가 위의 과정을 반복

## 문제

<BOJ 2839> 설탕 배달

**해결 방법 적용**

- 선택 절차 : 설탕 봉지 개수를 줄이기 위해 현재 가장 담을 무게가 높은 5kg 봉지 우선적 선택
- 적절성 검사
  - 1번 과정을 통해 선택된 봉지들의 무게 합이 총 무게를 초과하는지 검사
  - 초과하면 가장 마지막에 선택한 봉지를 삭제하고, 1번으로 돌아가 한 단계 작은 봉지인 3kg를 선택
- 해답 검사
  - 선택된 봉지들의 무게 합이 총 무게와 일치하는지 검사
  - 총 무게보다 작다면 1번 과정부터 다시 반복

**예제 입력**
18 -> (5kg) -> 13kg -> (5kg) -> 8kg -> (5kg) -> 3kg -> (3kg) -> 0kg

**예제 출력**
5kg 봉지 3개, 3kg 봉지 1개 => 4개

---

<BOJ 5585> 거스름돈

**해결 방법 적용**

- 선택 절차 : 거스름돈의 동전 개수를 줄이기 위해 현재 가장 가치가 높은 동전 우선적 선택
- 적절성 검사
  - 1번 과정을 통해 선택된 동전들의 합이 거슬러 줄 금액을 초과하는지 검사
  - 초과하면 가장 마지막에 선택한 동전을 삭제하고, 1번으로 돌아가 한 단계 작은 동전을 선택
- 해답 검사
  - 선택된 동전들의 합이 거슬러 줄 금액과 일치하는지 검사
  - 액수가 부족하면 1번 과정부터 다시 반복

**예제 입력**
380엔 => 거스름 돈 : 620엔
620엔 -> (500엔) -> 120엔 -> (100엔) -> 20엔 -> (10엔) -> 10엔 -> (10엔) -> 0엔

**예제 출력**
500엔, 100엔, 10엔, 10엔 => 4개

---
