# ---------- Keyword Arguments ----------

def employee(**info):
    print(info)


employee(name="Tom", last_name="Johnson", age=34,
         skill_set="Developer")
# Non-keyword Arguments == Tuples (*var_name)
# Keyword Arguments == Dictionaries(**var_name)

print("------------")


def to_do(**to_do_status):
    return to_do_status


to_do_status_result = to_do(get_coffee="Done", exercise="Pending",
                            watch_tv="In Progress")

print(to_do_status_result)
