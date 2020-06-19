import json
import os
import re
from include_markdown import get_all_md_files

SIGNAL = '<!-- REFERENCE -->'
TEMPLATE = """
<details>
<summary>[{}] {}</summary>
<br>
<!-- ({}) -->

{}

[{}](../papers/{})

</details>
"""


def get_reference_numbers(content):
    return [ref[1:-1] for ref in re.findall(r'\[[0-9]*\]', ' '.join(content))]


def fill(reference, reference_number, content):
    return TEMPLATE.format(reference_number,
                           reference[reference_number]['name'],
                           reference[reference_number]['markdown'],
                           ''.join(content),
                           reference[reference_number]['name'],
                           reference[reference_number]['markdown'],
                           )


def find_signal_index(content):
    for i, line in enumerate(content):
        if SIGNAL in line:
            return i

    return len(content)


def process(file):
    with open('reference.json', 'r') as f:
        reference = json.load(f)

    paper_folder = os.path.abspath('./docs/papers')

    with open(file, 'r') as f:
        content = f.readlines()

    start = find_signal_index(content)
    if start == len(content):
        reference_content = content + ['\n', SIGNAL + '\n']
    else:
        reference_content = content[:start + 1]
    reference_numbers = set(get_reference_numbers(reference_content))

    for reference_number in reference_numbers:
        with open(os.path.join(paper_folder, reference[reference_number]['markdown']), 'r') as f:
            file_content = f.readlines()

        new_content = fill(reference, reference_number, file_content)
        new_content = [line + '\n' for line in new_content.split('\n')]
        reference_content += ['\n'] + new_content

    with open(file, 'w') as f:
        for line in reference_content:
            f.write(line)


def main():
    md_files = get_all_md_files()
    for file in md_files:
        print("processing", file)
        process(file)

main()
