with open("text_2.txt", "r", encoding='utf-8') as f_obj:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов' for line, count in enumerate(f_obj, 1)]
    print(*usefulness, f"Всего строк - {len(usefulness)}.", sep="\n")