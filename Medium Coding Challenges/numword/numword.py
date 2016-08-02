"""Convert an integer number to the word representation.

We should handle zero:

    >>> num_word(0)
    'zero'

And numbers under a thousand:

    >>> num_word(2)
    'two'

    >>> num_word(-2)
    'negative two'

    >>> num_word(11)
    'eleven'

    >>> num_word(20)
    'twenty'

    >>> num_word(100)
    'one hundred'

    >>> num_word(121)
    'one hundred twenty one'

And numbers over a thousand:

    >>> num_word(1256)
    'one thousand two hundred fifty six'

    >>> num_word(100001)
    'one hundred thousand one'

    >>> num_word(1000000)
    'one million'

And all numbers ranging from -999,999,999,999 to 999,999,999,999 (you
can stop there):

    >>> num_word(-1234567890)  # doctest:+NORMALIZE_WHITESPACE
    'negative one billion two hundred thirty four million
    five hundred sixty seven thousand eight hundred ninety'

    >>> num_word(999999999999)  # doctest:+NORMALIZE_WHITESPACE
    'nine hundred ninety nine billion nine hundred ninety nine million
    nine hundred ninety nine thousand nine hundred ninety nine'

"""
ONES = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ",
        "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ",
        "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ",
        "nineteen "]
        
TENS = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ",
        "seventy ", "eighty ", "ninety "]

THOUSANDS = ["", "thousand ", "million ", "billion "]

def handle_cluster(num):
    out = ''
    if num >= 100: # handle hundreds
        out += ONES[num / 100] + 'hundred '
        num %= 100
    elif num >= 20: # handle tens
        out += TENS[num / 10]
        num %= 10
    else: # handle singles and teens
        out += ONES[num]
    return out

def num_word(num):
    """Convert word to number."""

    if num_word < 0:
        return "negative " + num_word(abs(num))

    out = ""
    cluster = 0

    while num > 0:
        cluster_val = num % 1000
        num = num / 1000

        if cluster_val > 0:
            out = handle_cluster(cluster_val) + THOUSANDS[cluster] + out

        cluster += 1

    return out.rstrip() or "zero"

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
