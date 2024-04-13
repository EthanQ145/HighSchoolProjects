def check_relate(child, parent, family, current_relation=0.5):
    try:
        if parent in family[child]:
            return current_relation
        else:
            total_relation = 0
            for prnt in family[child]:
                relation = check_relate(prnt, parent, family, current_relation * 0.5)
                if relation:
                    total_relation += relation

            if total_relation == 0:
                return None
            else:
                return total_relation
    except:
        return None



total_relations = []
while True:
    family_dict = {}
    current_relations = []
    finished = False
    while not finished:
        try:
            people = input()
            person, parent_1, parent_2 = people.split()
            family_dict[person] = [parent_1, parent_2]
        except:
            if people == "#":
                if family_dict == {}:
                    for rel in range(len(total_relations)):
                        for line in total_relations[rel]:
                            print(line)
                        if rel != len(total_relations) - 1:
                            print()
                    quit()
                queries = {}
                query_num = 0
                qry = True
                while qry:
                    try:
                        person_1, person_2 = input().split()
                        queries[query_num] = [person_1, person_2]
                        query_num += 1
                    except:
                        qry = False

                for query in queries.values():
                    person_1, person_2 = query
                    relation = check_relate(person_1, person_2, family_dict)
                    if relation is None:
                        relation = check_relate(person_2, person_1, family_dict)
                        if relation is None:
                            current_relations.append(f"{person_1} and {person_2} are not related.")
                        else:
                            relation = relation.as_integer_ratio()
                            current_relations.append(f"{person_2} is {relation[0]}/{relation[1]} {person_1}.")
                    else:
                        relation = relation.as_integer_ratio()
                        current_relations.append(f"{person_1} is {relation[0]}/{relation[1]} {person_2}.")
                total_relations.append(current_relations)
                finished = True