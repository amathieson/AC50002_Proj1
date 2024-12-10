def test(processor):
    print("Testing \x1b[1;33mScores\x1b[0m...")
    test_scores = [
        # WORD  ACRONYM SCORE
        ("Cold", "COL", 38),
        ("Cold", "COD", 26),
        ("Cold", "CLD", 22),
        ("Cool", "COO", 43),
        ("Cool", "COL", 26),
        ("C++ Code", "CCO", 21),
        ("C++ Code", "CCD", 11),
        ("C++ Code", "CCE", 20),
        ("C++ Code", "COD", 32),
        ("C++ Code", "COE", 41),
        ("C++ Code", "CDE", 31)
    ]
    fails = 0
    for case in test_scores:
        scr = processor.score(case[0].upper(), case[1])
        if scr != case[2]:
            fails += 1
            print(
                f"FAIL: Word: \x1b[1;33m{case[0]}\x1b[0m Acronym: \x1b[1;33m{case[1]}\x1b[0m Expected: \x1b[1;31m{case[2]}\x1b[0m Result: \x1b[1;31m{scr}\x1b[0m")
    print(
        f"Scores Test: \x1b[1;{'31' if fails > 0 else '32'}m{fails}\x1b[0m Failed / \x1b[1;33m{len(test_scores)}\x1b[0m Tests (\x1b[1;{'31' if fails > 0 else '32'}m{round((1 - fails / len(test_scores)) * 100)}%\x1b[0m Pass)")
    print("Testing \x1b[1;33mAcronyms\x1b[0m...")
    test_acronyms = [
        # WORD   ACRONYMS
        ("Cold", {"COL", "COD", "CLD"}),
        ("Cool", {"COO", "COL"}),
        ("C++ Code", {"CCO", "CCD", "CCE", "COD", "COE", "CDE"}),
    ]
    fails = 0
    for case in test_acronyms:
        acc = processor.generate_acronyms(case[0]).set
        if acc != case[1]:
            fails += 1
            print(
                f"FAIL: Word: \x1b[1;33m{case[0]}\x1b[0m Expected: \x1b[1;31m{case[1]}\x1b[0m Result: \x1b[1;31m{acc}\x1b[0m")
    print(
        f"Acronym Test: \x1b[1;{'31' if fails > 0 else '32'}m{fails}\x1b[0m Failed / \x1b[1;33m{len(test_acronyms)}\x1b[0m Tests (\x1b[1;{'31' if fails > 0 else '32'}m{round((1 - fails / len(test_acronyms)) * 100)}%\x1b[0m Pass)")
    print("Testing \x1b[1;33mSet\x1b[0m...")
    test_set = [
        # WORD  BEST ACRONYM
        ("Cold", ["CLD"]),
        ("Cool", ["COO"]),
        ("C++ Code", ["CCD"]),
    ]
    # Shorthand for selecting first item in tuple making a new list from it
    acronyms = processor.generate_set([i[0] for i in test_set])
    fails = 0
    for i, case in enumerate(test_set):
        if case[1] != acronyms[case[0]]:
            fails += 1
            print(
                f"FAIL: Word: \x1b[1;33m{case[0]}\x1b[0m Expected: \x1b[1;31m{case[1]}\x1b[0m Result: \x1b[1;31m{acronyms[case[0]]}\x1b[0m")
    print(
        f"Sets Test: \x1b[1;{'31' if fails > 0 else '32'}m{fails}\x1b[0m Failed / \x1b[1;33m{len(test_set)}\x1b[0m Tests (\x1b[1;{'31' if fails > 0 else '32'}m{round((1 - fails / len(test_set)) * 100)}%\x1b[0m Pass)")
