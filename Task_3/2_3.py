import os


def write_line_count(dict_txt):
    sorted_dict_txt_values = sorted(dict_txt.values())
    new_sorted_dict_text = {}
    for value in sorted_dict_txt_values:
        for key in dict_txt.keys():
            if dict_txt[key] == value:
                new_sorted_dict_text[key] = dict_txt[key]
    with open('sorted_text.txt', 'w') as document:
        for doc, value in new_sorted_dict_text.items():
            document.write(os.path.basename(doc) + '\n')
            document.write(str(value))
            document.write('\n')
            with open(doc) as f:
                for line in f:
                    document.write(line)
                document.write('\n')


class RecordingSortedFiles:
    dict_text = {}

    def __init__(self, file):
        self.file = file

    def line_count(self, file):
        counter = 0
        with open(file) as document:
            for line in document:
                counter += 1
            self.dict_text[file] = counter
        return self.dict_text


txt1 = RecordingSortedFiles('1.txt')
txt2 = RecordingSortedFiles('2.txt')
txt3 = RecordingSortedFiles('3.txt')

txt1.line_count(txt1.file)
txt2.line_count(txt2.file)
txt3.line_count(txt3.file)
write_line_count(RecordingSortedFiles.dict_text)
