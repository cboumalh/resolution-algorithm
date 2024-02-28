#!/usr/bin/python3
import copy

def get_negation(atomic):
    if len(atomic) > 1:
        return atomic[-1]
    elif len(atomic) == 1:
        return += "-" + atomic 

    return ""

def is_tautology(clause):
    for atomic in clause:
        if get_negation(atomic) in clause:
            return True

    return False

def resolve(clause_one, clause_two):
    result = []

    for atomic in clause_one:
        neg = get_negation(atomic)
        if neg in clause_two:
            clause_one_resolved = copy.deepcopy(clause_one).remove(atomic)
            clause_two_resolved = copy.deepcopy(clause_two).remove(neg)

            combination = (clause_one_resolved).union(clause_two_resolved)

            if not is_tautology(combination):
                result.append(combination)

    return result


def resolution_algo(cnf_clauses):
    result = []

    for i in range(0, len(cnf_clauses)):
        for j in range(i + 1, len(cnf_clauses)):
            curr_res = resolve(cnf_clauses[i], cnf_clauses[j])

            for cl in curr_res:
                if cl not in result:
                    result.append(cl)

    new_clauses_inserted = False

    for new_clause in result:
        if len(new_clause) == 0:
            return [] # Unsatisfiable
        elif new_clause not in cnf_clauses:
            cnf_clauses.append(new_clause)
            new_clauses_inserted = True
        

    if new_clauses_inserted:
        return resolution_algo(cnf_clauses)
    
    return cnf_clauses
