# 문제5
# 게임 캐릭터가 몬스터와 1:1 전투를 하려 합니다.
# 몬스터는 처음에 일정 수치의 체력(HP)을 가지고 있습니다.
# 캐릭터가 전투에서 이기려면 몬스터를 공격해 몬스터의 체력을 0이하로 만들어야합니다.
# 캐릭터는 공격 마법만 사용하며, 공격 마법은 항상 같은 데미지를 입힙니다.
# 몬스터는 힐링 마법만을 사용하며, 힐링 마법은 항상 같은 수치로 체력을 회복합니다.
# 둘은 항상 번갈아 가며 마법을 사용하고, 처음에는 항상 캐릭터가 먼저 공격을 시작합니다.
# * attack은 1 이상 100 이하의 자연수입니다.
# * recovery는 1 이상 100 이하의 자연수입니다.
# * 캐릭터의 공격력은 항상 몬스터의 회복력보다 큽니다(recovery < attack).
# * hp는 200 이상 1,000 이하의 자연수입니다.

# | attack | recovery | hp  | return |
# |--------|----------|-----|--------|
# | 30     | 10       | 60 | 3      |


def solution(attack, recovery, hp):
    turn = 0
    while hp > 0:
        turn += 1
        hp -= attack
        if hp <= 0:
            break
        hp += recovery
    print(turn)


attack = 30
recovery = 10
hp = 600
solution(attack, recovery, hp)
