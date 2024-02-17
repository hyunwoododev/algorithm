// https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=javascript
function solution(numbers, target) {
  let answer = 0;

  function dfs(index, sum) {
    // 모든 숫자를 탐색했을 때
    if (index === numbers.length) {
      // 현재 합계가 타겟 넘버와 같다면, 경우의 수 1 증가
      if (sum === target) {
        answer++;
      }
      return;
    }

    // 현재 숫자를 더하는 경우
    dfs(index + 1, sum + numbers[index]);
    // 현재 숫자를 빼는 경우
    dfs(index + 1, sum - numbers[index]);
  }

  // DFS 탐색 시작
  dfs(0, 0);

  return answer;
}
