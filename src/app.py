from const import cyrillic


def main(text: str):
    result = ""
    for i in text:
        result += f"&#{1040 + cyrillic.index(i)};" if i in cyrillic else str(i)
    with open("TextToUnicode1.txt", "a+") as file:
        file.write(f"{result}\n")
    with open("TextToUnicode2.txt", "w") as file:
        file.write(f"{result}\n")
    return result


print(
    "TextToUnicode v1.0\n"
    "Данная программа создана, чтобы конвертировать Кириллицу в Unicode\n\n"
    "Основное предназначение:\nГенерировать Unicode, отправлять пользователю ВКонтакте файл и просить его, чтобы он "
    "отправил содержимое файла в чат. ВКонтакте автоматически конвертирует Unicode в текст и отправляется изначальная "
    "фраза.\n"
    "Пример:\n"
    "Вы сгенерировали фразу \"Передать 1 10000\", скинули файл с юникодом пользователю и попросили его написать "
    "этот текст какому-нибудь игровому боту. После чего этот человек передает вам 10000 игровой валюты.\n"
)

print(
    f"Ваша фраза в Unicode: {main(input('Введите текст: '))}\n"
    f"Ваша фраза была:\n"
    f"1) Дописана в файл TextToUnicode1.txt\n"
    f"2) Записана в файл TextToUnicode2.txt"
)
