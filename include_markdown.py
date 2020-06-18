import os
import networkx as nx

# <!-- () -->
SIGNAL = '<!--'  # because it is comment. i.e <!-- (This may be the b hhk  most platform independent comment) -->


def get_all_md_files(dir='./', ext='.md'):
    md_files = []
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                md_files.append(os.path.join(root, file))

    return md_files


def is_valid(files):
    """
    Check if conflicting exists, by checking the cycle in graph
    :param files: list of input files
    :return: true/false whether it is conflicted
    """
    edges = []
    for file in files:
        _, sub_files, _, _ = find_included_files(file)
        for sub_file in sub_files:
            edges.append((os.path.abspath(file), os.path.abspath(sub_file)))

    G = nx.DiGraph(edges)

    found_cycle = False
    for cycle in nx.simple_cycles(G):
        print("Found cycle:", cycle)
        found_cycle = True

    return not found_cycle


def find_included_files(file):
    """

    :param file: current file
    :return: content, sub_files, starts, ends
    """
    with open(file, 'r') as f:
        content = f.readlines()

    starts = []
    ends = []
    sub_files = []
    # find all the sub-files contained in that file and correspond starts and ends

    dir_name = os.path.dirname(file)

    i = 0
    while i < len(content):
        if SIGNAL in content[i]:
            # find the included file
            file_path = content[i][content[i].find('(') + 1: content[i].find(')')]
            sub_files.append(os.path.join(dir_name, file_path))

            found_start_div = False
            while i < len(content) and not found_start_div:
                if '<div>' in content[i]:
                    starts.append(i + 1)
                    found_start_div = True
                i += 1

            found_end_div = False
            while i < len(content) and not found_end_div:
                if '</div>' in content[i]:
                    ends.append(i)
                    found_end_div = True
                i += 1

        i += 1

    return content, sub_files, starts, ends


def process(file):
    root_content, sub_files, starts, ends = find_included_files(file)

    sub_contents = []
    for sub_file in sub_files:
        with open(sub_file, 'r') as f:
            sub_contents.append(f.readlines())

    # add to root_content, then write root content to file
    previous_end = 0
    new_content = []
    for content, start, end in zip(sub_contents, starts, ends):
        new_content += root_content[previous_end: start] + ['\n'] + content
        previous_end = end

    new_content += root_content[previous_end:]

    with open(file, 'w') as f:
        for line in new_content:
            if line[-1] != "\n":
                line += "\n"

            f.write(line)

    print("handle", file, "successfully")


def main():
    md_files = get_all_md_files(dir='./', ext='.md')
    if is_valid(md_files):
        for file in md_files:
            print("processing file", file)
            process(file)
    else:
        print("FAILED, FOUND CYCLE")


# main()
