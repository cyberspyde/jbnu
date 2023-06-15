
def clean_data(id):
    try:
        with open(f"data/output{id}.txt", "r", encoding='utf-8') as f:
            text = f.read()

        start_index = text.find("제목")
        end_index = text.find("목록")

        text = text[start_index:end_index-1]

        with open(f'clean_data/output{id}.txt', 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        print(e)

for i in range(300, 320):
    clean_data(i)
# with open('output-clean.txt', 'w', encoding='utf-8') as f:
#     f.write(text)