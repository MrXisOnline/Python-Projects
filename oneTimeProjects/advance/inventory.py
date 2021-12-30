def show_inventory(dic):
    count_item = 0
    print("Inventory : ")
    for key in dic.keys():
        count_item = count_item + dic[key]
        print(dic[key], key)
    print("Total number of items:", count_item)


def precise_list(li):
    pr_li = {}
    for i in li:
        no_item = li.count(i)
        if i not in pr_li.keys():
            pr_li[i] = no_item
    return pr_li


def add_to_inventory(dic, loot):
    loot_dic = precise_list(loot)
    for item in loot_dic.keys():
        if item in dic.keys():
            val = dic[item]
            dic[item] = val + loot_dic[item]
        else:
            dic[item] = 1
    show_inventory(dic)
    return dic


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
show_inventory(inventory)
add_to_inventory(inventory, dragonLoot)
