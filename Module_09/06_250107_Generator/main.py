def all_variants(text: str):
    length = len(text)+1
    for j in range(1, length):
        i = 0
        while i+j < length:
            yield text[i:i+j]
            i += 1


# Проверка:
a = all_variants("abc")
b = all_variants("абв")
c = all_variants('123')
for i in a:
    print(i)

print()

for i in b:
    print(i)


print()

for i in c:
    print(i)
