import test_login_many_users

results = []
results.append(test_login_many_users.test_many_users_login())

with open("result.txt", "w", encoding="utf-8") as file:
    for r in results:
        print(r)
        file.write(r + "\n")
