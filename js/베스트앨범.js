// https://school.programmers.co.kr/learn/courses/30/lessons/42579
function solution(genres, plays) {
  const genreMap = {};

  genres.forEach((genre, index) => {
    if (!genreMap[genre]) {
      genreMap[genre] = { totalPlay: 0, songs: [] };
    }
    genreMap[genre].totalPlay += plays[index];
    genreMap[genre].songs.push({ index, play: plays[index] });
  });

  const genreList = Object.entries(genreMap).sort(
    (a, b) => b[1].totalPlay - a[1].totalPlay
  );

  const bestAlbum = [];
  genreList.forEach(([genre, { songs }]) => {
    songs.sort((a, b) => b.play - a.play || a.index - b.index);
    songs.slice(0, 2).forEach((song) => bestAlbum.push(song.index));
  });

  return bestAlbum;
}
