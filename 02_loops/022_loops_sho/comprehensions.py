# Only Theory - Since we don't have the whole Code

def main ():
    counts = {}
    words = get_words("address. txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]      # Modifying Multiple Values by using a for - loop

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    save_counts(counts)