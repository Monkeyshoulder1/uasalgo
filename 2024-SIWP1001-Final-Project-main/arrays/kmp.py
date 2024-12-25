def kmp_algorithm(pattern, text):
    """
    Find all occurrences of pattern in text using KMP algorithm
    
    Args:
        pattern (str): Pattern to search
        text (str): Text to search in
    
    Returns:
        List[int]: Indices of pattern occurrences
    """
    # Compute longest prefix-suffix array
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Find pattern matches
    matches = []
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print("Pattern Occurrences:", kmp_algorithm(pattern, text))