#!/usr/bin/env python3
"""Generate all valid English words from head/vowel/tail combinations."""

# Data from index.html
head = {
    '140': {
        'Sub-1': ['b', 'p', 'm', 'n'],
        'Sub-2': ['d', 't', 'n', 'l'],
        'Sub-3': ['g', 'k', 'h'],
        'Sub-4': ['s', 'th', 'r']
    },
    '280': {
        'Sub-1': ['dr', 'tr', 'br', 'pr'],
        'Sub-2': ['bl', 'pl', 'kl', 'sl'],
        'Sub-3': ['sm', 'sn', 'sp', 'st', 'sg', 'str']
    }
}

vowel = {
    'Basic': {
        'Sub-1': ['e', 'ai', 'a', 'ou'],
        'Sub-2': ['i', 'oo', 'oa'],
        'Sub-3': ['o', 'er', 'ar']
    },
    '8800': {
        'Sub-1': ['a', 'e', 'i', 'o', 'u'],
        'Sub-2': ['a_e', 'e_e', 'i_e', 'o_e', 'u_e'],
        'Sub-3': ['ar', 'er', 'ir', 'or', 'ur'],
        'Sub-4': ['ee', 'oo', 'ou', 'oi', 'air']
    }
}

tail = {
    'Single': ['s', 'ss', 'b', 'p', 'd', 't', 'g', 'ck', 'st', 'sp'],
    'Nose': ['m', 'mb', 'mp', 'n', 'nd', 'nt'],
    'Extra': ['ph', 'ch', 'sh', 'th']
}

def flatten(data):
    """Flatten nested dict structure to list of values."""
    result = []
    for key, value in data.items():
        if isinstance(value, dict):
            result.extend(flatten(value))
        elif isinstance(value, list):
            result.extend(value)
    return list(set(result))  # Remove duplicates

def generate_word(h, v, t):
    """Generate word from head, vowel, tail."""
    if '_' in v:
        parts = v.split('_')
        return h + parts[0] + t + parts[1]
    else:
        return h + v + t

# Load system dictionary
def load_dictionary():
    """Load words from system dictionary."""
    words = set()
    dict_paths = [
        '/usr/share/dict/words',
        '/usr/share/dict/american-english',
        '/usr/share/dict/british-english',
    ]
    for path in dict_paths:
        try:
            with open(path, 'r') as f:
                for line in f:
                    word = line.strip().lower()
                    # Only include words without apostrophes
                    if "'" not in word:
                        words.add(word)
        except FileNotFoundError:
            continue
    return words

def main():
    heads = flatten(head)
    vowels = flatten(vowel)
    tails = flatten(tail)

    print(f"Heads ({len(heads)}): {sorted(heads)}")
    print(f"Vowels ({len(vowels)}): {sorted(vowels)}")
    print(f"Tails ({len(tails)}): {sorted(tails)}")
    print()

    # Generate all combinations
    all_combinations = []
    for h in heads:
        for v in vowels:
            for t in tails:
                word = generate_word(h, v, t)
                all_combinations.append(word)

    print(f"Total combinations: {len(all_combinations)}")

    # Load dictionary
    dictionary = load_dictionary()
    print(f"Dictionary size: {len(dictionary)}")

    # Find real words
    real_words = sorted(set(w for w in all_combinations if w.lower() in dictionary))
    print(f"Real words found: {len(real_words)}")
    print()

    # Group by length for readability
    by_length = {}
    for w in real_words:
        length = len(w)
        if length not in by_length:
            by_length[length] = []
        by_length[length].append(w)

    # Output JavaScript Set format
    print("// Real English words for detection")
    print("const realWords = new Set([")
    for length in sorted(by_length.keys()):
        words = by_length[length]
        # Split into lines of ~10 words each
        for i in range(0, len(words), 10):
            chunk = words[i:i+10]
            line = ", ".join(f"'{w}'" for w in chunk)
            print(f"    {line},")
    print("]);")

if __name__ == '__main__':
    main()
