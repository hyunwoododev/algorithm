# https://school.programmers.co.kr/learn/courses/30/lessons/42860

# 죽어도 이해안됨.
def solution(name):
    spell_move = 0
    cursor_move = len(name) - 1  
    for i, spell in enumerate(name):
        spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        cursor_move = min([ cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next) ])
        
        
    return spell_move + cursor_move