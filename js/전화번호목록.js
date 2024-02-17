function solution(phoneBook) {
  // 전화번호 목록을 사전 순으로 정렬합니다.
  phoneBook.sort();

  // 전화번호 목록을 순회하면서, 각 번호가 다음 번호의 접두사인지 확인합니다.
  for (let i = 0; i < phoneBook.length - 1; i++) {
    if (phoneBook[i + 1].startsWith(phoneBook[i])) {
      return false; // 현재 번호가 다음 번호의 접두사라면, 요구사항을 위반하므로 false를 반환합니다.
    }
  }

  // 모든 검사를 통과했다면, 어떤 번호도 다른 번호의 접두사가 아니므로 true를 반환합니다.
  return true;
}
