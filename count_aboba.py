with open('coolstory.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    count_aboba = data.count('aboba')
    print(f"Количество абоба: {count_aboba}")