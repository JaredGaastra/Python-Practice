def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    # lett_count=0
    # letter_count=[let_count + 1 for let_count in word if let_count == letter]

    # loop through word
    for let in word:
        count = 0
        if let.lower() == letter.lower():# check if letter is equal to anything within the word
            print(count + 1)# if true set count + 1

    # count = word.upper().count(letter.upper())
    # print(count)