text = "X-DSPAM-Confidence:    0.8475"


def parse_confidence(string):
    strings = text.split(":")
    result = strings[1].strip()
    print(float(result))


parse_confidence(text)