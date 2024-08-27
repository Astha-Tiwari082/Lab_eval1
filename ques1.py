def reverse_word(given):
    words = given.split()
    reverse = words[::-1]
    capital_words = [word.capitalize() for word in reverse]
    final = ' '.join(capital_words)
    return final

given = "The Ganges is the longest river in India while The Nile in World"
output_string = reverse_word(given)
print(output_string)
