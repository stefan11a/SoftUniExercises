damage_info = {}
health_info = {}
armor_info = {}

dragon_stats = [damage_info, health_info, armor_info]

N = int(input())

for i in range(N):

    dragon_type, name, damage, health, armor = input().split(' ')

    if dragon_type not in damage_info.keys():
        damage_info[dragon_type] = {}
    if dragon_type not in health_info.keys():
        health_info[dragon_type] = {}
    if dragon_type not in armor_info.keys():
        armor_info[dragon_type] = {}

    if name not in damage_info[dragon_type]:
        damage_info[dragon_type][name] = 0
    damage_info[dragon_type][name] = damage
    if name not in health_info[dragon_type]:
        health_info[dragon_type][name] = 0
    health_info[dragon_type][name] = health
    if name not in armor_info[dragon_type]:
        armor_info[dragon_type][name] = 0
    armor_info[dragon_type][name] = armor

