def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"

    is_yell = any(c.isalpha() for c in hey_bob) and hey_bob.upper() == hey_bob
    is_question = hey_bob.endswith("?")

    if is_yell and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yell:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."

