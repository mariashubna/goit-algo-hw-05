import timeit

file_path = 'art1.txt'
file_path2 = 'art2.txt'

with open(file_path, 'r', encoding='cp1251') as f1:
    content1 = f1.read()

with open(file_path2, 'r', encoding='cp1251') as f2:
    content2 = f2.read()


#Алгоритм Боєра-Мура

def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0 

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  

        if j < 0:
            return i  
        
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
        
    return None

    

# Алгоритм Кнута-Морріса-Пратта
def compute_lps(pattern):
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

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j
    
    return None

# Алгоритм Рабіна-Карпа


def polynomial_hash(s, base=256, modulus=101):
    
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string,  substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    base = 256 
    modulus = 101  
    
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    h_multiplier = pow(base, substring_length - 1) % modulus    
    
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    
    return None

pattern1 = ["Інтерполяційний пошук використовується для пошуку елементів у відсортованому масиві.", "Райгородский А.М. Математичні моделі Інтернета."]
pattern2 = [ "Розмір блоку розгорнутого списку впливає на швидкість роботи і на об’єм використаної пам’яті", "Райгородский А.М. Математичні моделі Інтернета."]

for sentence in pattern1:
    position1 = boyer_moore_search(content1, sentence)
    position2 = kmp_search(content1, sentence)
    position3 = rabin_karp_search(content1, sentence)
    boyer_moore_search_time = timeit.timeit(stmt='position1', globals=globals(), number=100)
    kmp_search_time = timeit.timeit(stmt='position2', globals=globals(), number=100)
    rabin_karp_search_time = timeit.timeit(stmt='position3', globals=globals(), number=100)
    if position1 is not None:
        print(f"Час пошуку за алгоритмом Боєра-Мура конструкції в тексті №1: {boyer_moore_search_time}")
    else:
        print(f"Час пошуку за алгоритмом Боєра-Мура неіснуючої конструкції в тексті №1: {boyer_moore_search_time}")
    if position2 is not None:
        print(f"Час пошуку за алгоритмом Кнута-Морріса-Пратта конструкції в тексті №1: {kmp_search_time}")
    else:
        print(f"Час пошуку за алгоритмом Кнута-Морріса-Пратта неіснуючої конструкції в тексті №1: {kmp_search_time}")
    if position3 is not None:
        print(f"Час пошуку за алгоритмом Рабіна-Карпа конструкції в тексті №1: {rabin_karp_search_time}")
    else:
        print(f"Час пошуку за алгоритмом Рабіна-Карпа неіснуючої конструкції в тексті №1: {rabin_karp_search_time}")
    print('----------------------------------------------------------------')

for sentence in pattern2:
    position1 = boyer_moore_search(content2, sentence)
    position2 = kmp_search(content2, sentence)
    position3 = rabin_karp_search(content2, sentence)
    boyer_moore_search_time = timeit.timeit(stmt='position1', globals=globals(), number=100)
    kmp_search_time = timeit.timeit(stmt='position2', globals=globals(), number=100)
    rabin_karp_search_time = timeit.timeit(stmt='position3', globals=globals(), number=100)
    if position1 is not None:
        print(f"Час пошуку за алгоритмом Боєра-Мура конструкції в тексті №2: {boyer_moore_search_time}")
    else:
        print(f"Час пошуку за алгоритмом Боєра-Мура неіснуючої конструкції в тексті №2: {boyer_moore_search_time}")
    if position2 is not None:
        print(f"Час пошуку за алгоритмом Кнута-Морріса-Пратта конструкції в тексті №2: {kmp_search_time}")
    else:
        print(f"Час пошуку за алгоритмом Кнута-Морріса-Пратта неіснуючої конструкції в тексті №2: {kmp_search_time}")
    if position3 is not None:
        print(f"Час пошуку за алгоритмом Рабіна-Карпа конструкції в тексті №2: {rabin_karp_search_time}")
    else:
        print(f"Час пошуку за алгоритмом Рабіна-Карпа неіснуючої конструкції в тексті №2: {rabin_karp_search_time}")
    print('----------------------------------------------------------------')

