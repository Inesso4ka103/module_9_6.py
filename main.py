def all_variants(text):
    for i in range(len(text)):
        for a in range(i, len(text)):
            yield text[i:a+1]



a = all_variants("abc")
for i in a:
    print(i)
