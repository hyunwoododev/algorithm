// https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=javascript

function solution(nums) {
  let getNum = nums.length / 2;
  let result = [...new Set(nums)]; // 중복을 제거하여 폰켓몬의 종류만 남깁니다.
  let answer = result.length > getNum ? getNum : result.length;
  return answer;
}
