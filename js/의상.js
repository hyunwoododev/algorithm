function solution(clothes) {
  const closet = {}; // 의상 종류별로 의상의 수를 저장할 객체

  // 의상을 순회하며 종류별로 의상의 수를 계산
  clothes.forEach(([item, type]) => {
    if (!closet[type]) {
      closet[type] = 1; // 해당 종류의 첫 의상이라면 1로 초기화
    } else {
      closet[type]++; // 이미 해당 종류의 의상이 있다면 1 증가
    }
  });

  // 각 종류별로 선택할 수 있는 방법의 수를 모두 곱함 (아무것도 선택하지 않는 경우 포함)
  let answer = 1;
  for (let type in closet) {
    answer *= closet[type] + 1; // 의상을 선택하는 경우 + 선택하지 않는 경우
  }

  // 아무것도 선택하지 않는 경우를 제외하기 위해 1을 뺌
  return answer - 1;
}
