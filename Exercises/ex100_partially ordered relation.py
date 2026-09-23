# 100. Partially Ordered Relation (POSET)

def get_all_order_pairs(set_items):
    n = len(set_items)
    order_pairs = set()
    for i in range(n):
        for j in range(n):
            order_pairs.add((int(set_items[i]), int(set_items[j])))
    return order_pairs


def get_sub_order_pairs(number, set_items):
    # Get subsets of ordered pairs by the user
    # and create the relation
    order_pair_sets = get_all_order_pairs(set_items)
    sub_set = set()  # Initialize
    for i in range(number):
        while True:
            sub = input(f"Enter pair {i + 1}: ").split(",")
            sub_S = tuple(int(s) for s in sub)  # Convert to tuple
            if sub_S in order_pair_sets:
                sub_set.add(sub_S)  # Add the tuples to the set
                break
            else:
                print("The pair does not exist in the set")
    return sub_set  # Return the relation (set of tuples)


def check_reflexive(order_pairs, relation_set):  # Check for reflexive
    # The relation is reflexive when there exists all pairs (a, b)
    # With a = b {note that a, b must be in set X} => pair (a, a)
    for i in order_pairs:
        # If there is any missing value (a, a) in the relation
        if i[0] == i[1] and i not in relation_set:
            return False
    return True


def check_antisymmetric(relation_set):  # Check for antisymmetric
    # The relation is antisymmetric when there does not exist
    # any pair (a, b) and (b, a) with a ≠ b
    # {note that a, b must be in set X}
    for i in relation_set:
        # If the reverse of the tuple exists in the relation
        # And no pair (a, a) exists in the relation
        if i[::-1] in relation_set and i[0] != i[1]:
            return False
    return True


def check_transitive(relation_set):  # Check for transitive
    # The relation is transitive when: if there exists pair (a, b) and (b, c)
    # there exists a pair (a, c) {note that a, b must be in set X}
    for i in relation_set:
        for j in relation_set:
            # If there exists two pairs
            # that the index 0 of pair 1 == index 1 of pair 2
            # And there does not exist the transitive pair in the relation
            if i[1] == j[0] and (i[0], j[1]) not in relation_set:
                return False
    return True


def check_poset():
    set_input = input("Enter the elements of the set (comma-separated, e.g., 1,2,3): ").split(', ')
    set_items = [item.strip() for item in set_input]

    all_order_pairs = set()
    for x in set_items:
        for y in set_items:
            all_order_pairs.add((int(x), int(y)))

    num_pairs = int(input("Enter the number of ordered pairs in the relation: "))
    relation_set = get_sub_order_pairs(num_pairs, set_items)

    is_reflexive = check_reflexive(all_order_pairs, relation_set)
    is_antisymmetric = check_antisymmetric(relation_set)
    is_transitive = check_transitive(relation_set)

    print("\n--- POSET Properties Check ---")
    print(f"Reflexive: {is_reflexive}")
    print(f"Antisymmetric: {is_antisymmetric}")
    print(f"Transitive: {is_transitive}")

    if is_reflexive and is_antisymmetric and is_transitive:
        print("\nThe given relation is a Partially Ordered Set (POSET).")
    else:
        print("\nThe given relation is NOT a Partially Ordered Set (POSET).")


check_poset()
