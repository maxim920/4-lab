text = "слава украине героям слава"

list_no = ['.',',',':',';','!','"','-','?']
list = []

for word in text.lower().split():
    if not word in list_no:
        _word = word 
        if word[-1] in list_no:
            _word = _word[:-1]
        if word[0] in list_no:
            _word = _word[1:]
        list.append(_word)

_dict = dict()
for word in list:
    _dict[word] = _dict.get(word, 0) + 1

_list = []
for key, value in _dict.items():
    _list.append((value, key))
    _list.sort(reverse = True)

print(f'самое частое слово в тексте {_list[0][1]} использовалось {_list[0][0]} раз')
