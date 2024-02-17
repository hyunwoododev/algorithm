// https://school.programmers.co.kr/learn/courses/30/lessons/84021

// 주어진 블록의 위치를 (0,0) 기준으로 이동시키고 정렬하는 함수
function moveBlock(block) {
  // 블록의 최소 x, y 값을 찾아
  let minX = Math.min(...block.map((v) => v[0]));
  let minY = Math.min(...block.map((v) => v[1]));
  // 블록을 (0,0)을 기준으로 이동시키고 정렬
  return block.map((v) => [v[0] - minX, v[1] - minY]).sort();
}

// 블록을 시계 방향으로 90도 회전시키는 함수
function rotate(block) {
  // 블록의 최대 x, y 중 큰 값을 찾아
  let max = Math.max(...block.map((v) => Math.max(v[0], v[1])));
  // 블록을 회전시킨 후, (0,0) 기준으로 이동시키고 정렬
  let rotateBlock = block.map((v) => [max - v[1], v[0]]);
  return moveBlock(rotateBlock);
}

// BFS를 이용하여 연결된 블록(또는 빈 칸)을 찾는 함수
function bfs(start, table, k) {
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];
  let needVisit = start;
  let block = [];
  while (needVisit.length > 0) {
    let [cx, cy] = needVisit.shift();
    block.push([cx, cy]);
    for (let i = 0; i < 4; i++) {
      let nx = cx + dx[i];
      let ny = cy + dy[i];
      if (nx < 0 || ny < 0 || nx >= table.length || ny >= table.length)
        continue;
      else if (table[nx][ny] === k) continue;
      else {
        needVisit.push([nx, ny]);
        table[nx][ny] = k;
      }
    }
  }
  return moveBlock(block);
}

// 메인 솔루션 함수
function solution(game_board, table) {
  let blanks = [];
  let blocks = [];
  // 게임 보드에서 빈 칸 찾기
  for (let i = 0; i < game_board.length; i++) {
    for (let j = 0; j < game_board.length; j++) {
      if (game_board[i][j] === 0) {
        game_board[i][j] = 1;
        blanks.push(bfs([[i, j]], game_board, 1));
      }
    }
  }
  // 테이블에서 블록 찾기
  for (let i = 0; i < table.length; i++) {
    for (let j = 0; j < table.length; j++) {
      if (table[i][j] === 1) {
        table[i][j] = 0;
        blocks.push(bfs([[i, j]], table, 0));
      }
    }
  }
  // 매칭되는 블록 찾기
  let answer = 0;
  blocks.forEach((val) => {
    for (let i = 0; i < blanks.length; i++) {
      let match = false;
      for (let j = 0; j < 4; j++) {
        val = rotate(val);
        if (JSON.stringify(val) === JSON.stringify(blanks[i])) {
          blanks.splice(i, 1);
          answer += val.length;
          match = true;
          break;
        }
      }
      if (match) break;
    }
  });
  return answer;
}
