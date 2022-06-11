import json
import re


def get_file_meta():
    # lines will contain all file lines
    lines = open('CACM/cacm.all', 'r').readlines()

    # file meta will contain index, title, summary, authors.
    file_meta = {}

    # Value to be retured
    files_meta = {}

    for i in range(0, len(lines)):

        # Detect index of a document
        match = re.match(r'\.I ([0-9]+)', lines[i])
        if match:
            if file_meta.__len__() != 0:
                files_meta[file_meta['index']] = file_meta
                file_meta = {}

            # Detect starting of a document
            file_meta['index'] = int(match.group(1))

        # Detect title of a document
        if re.match(r'\.T', lines[i]):
            i = i + 1
            if not re.match(r'\.W', lines[i]):
                file_meta['title'] = lines[i].replace('\n', '')

        # Detect document summary
        summary = ''
        if re.match(r'\.W', lines[i]):
            i = i + 1
            for j in range(i, len(lines)):
                if re.match(r'\.[A-Z]', lines[j]):
                    break
                summary = summary + ' ' + lines[j].replace('\n', '')
            file_meta['summary'] = summary

        # Detect authors
        authors = []
        if re.match(r'\.A', lines[i]):
            i = i + 1
            for j in range(i, len(lines)):
                if re.match(r'\.[A-Z]', lines[j]):
                    break
                authors.append(lines[j].replace('\n', ''))
            file_meta['authors'] = authors

        if i == len(lines) - 1:
            files_meta[file_meta['index']] = file_meta

    with open('meta.json', 'w', encoding='UTF-8') as file_writer:
        json.dump(files_meta, file_writer, ensure_ascii=False, sort_keys=False)

    return files_meta
