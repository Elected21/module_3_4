def single_root_words(root_word, *other_words):
    same_words = []

    for i in range(len(other_words)):

        if root_word.lower() in str(other_words[i]).lower() or str(other_words[i]).lower() in root_word.lower():
            same_words.append(other_words[i])

    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
