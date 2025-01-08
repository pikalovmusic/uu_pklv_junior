def all_variants(text: str):
    for j in range(1, len(text)+1):
        for i in range(len(text)):
            if j+i > len(text):
                break
            yield text[i:j+i]


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
