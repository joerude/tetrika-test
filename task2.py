from wikipediaapi import Wikipedia

rus_alphabet_str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()
animal_names_counter = {}
for char in rus_alphabet_str:
    animal_names_counter.setdefault(char, 0)


def number_of_animals_for_each_letter(categorymembers):
    for c in categorymembers.values():
        if (
            c.title[0].upper() in rus_alphabet_str
            and not c.title.endswith("(род)")
            and not c.title.startswith("Категория:")
        ):
            animal_names_counter[c.title[0].upper()] += 1


wiki_wiki = Wikipedia("ru")
rus_category_animals = wiki_wiki.page("Категория:Животные по алфавиту")
number_of_animals_for_each_letter(rus_category_animals.categorymembers)

if __name__ == "__main__":
    for key, value in animal_names_counter.items():
        print(f"{key}: {value}")
