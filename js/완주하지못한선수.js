// https://school.programmers.co.kr/learn/courses/30/lessons/42576
function solution(participant, completion) {
  const counts = {}; // 선수의 이름을 키로, 등장 횟수를 값으로 저장할 객체

  // 참가자의 이름을 키로 하여 counts 객체에 등장 횟수를 저장
  participant.forEach((name) => {
    if (counts[name]) {
      counts[name] += 1;
    } else {
      counts[name] = 1;
    }
  });

  // 완주자의 이름을 키로 하여 counts 객체에서 등장 횟수를 감소
  completion.forEach((name) => {
    counts[name] -= 1;
  });

  // counts 객체를 순회하며 등장 횟수가 0이 아닌(즉, 완주하지 못한) 선수의 이름을 찾아 반환
  for (let name in counts) {
    if (counts[name] > 0) {
      return name;
    }
  }
}
