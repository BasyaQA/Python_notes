# кортежи, в отличие от списков, НЕ ИЗМЕНЯЮТСЯ

user_roles = ("admin", "editor", "viewer")
print(user_roles)

for role in user_roles:
    print(role)

print("admin" in user_roles)

# у кортежей есть индексы
print(user_roles[2])

# распаковка кортежа
role_1, role_2, role_3 = user_roles
print(user_roles)
print(role_2)

# tuple чаще всего используется в функциях
