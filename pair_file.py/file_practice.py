def load_dictionary(filename):
    """fileaas ug bolon utgaiig unshaad sudlah"""
    word_dict={}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts=line.split(maxsplit=1)
            if len(parts)<2:
                continue
            rest=parts[1]

            token = rest.split(maxsplit=1)
            if len(token)<2:
                continue
            word=token[0].strip()
            meaning=token[1].strip().strip('"')
            word_dict[word]=meaning
    return word_dict

def main():
    dictionary=load_dictionary('pair_file.py/vocablary.txt')

    print("===영어 단어 사전===")
    print(f"총{len(dictionary)} 개의 단어가 등록되어 있습니다.")
    print("종료하려면'quit'를 입력하세요.\n")

    while True:
        word=input("단어를 입력하세요:").strip()
        if word.lower() == 'quit':
            print("프로그램을 종료합니다.")
            break
        if word in dictionary:
            print(f"{word}:{dictionary[word]}\n")
        else:
            print(f" '{word}'은(는) 사전에 없는 단어입니다.\n")

if __name__== '__main__':
    main()