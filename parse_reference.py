import json
import os

with open('references.txt', 'r') as f:
    content = f.readlines()

content = [line[:-1] for line in content]

results = []
i = 0
new_line = ''
while i < len(content):
    if '[' in content[i] and i != 0:
        if new_line:
            results.append(new_line)
            new_line = content[i]
    else:
        new_line += ' ' + content[i]
    i += 1

results.append(new_line)

special_characters = '´":.¨!@#$%^&*()+:..,- '
names = []
paper_names = []
for r in results:
    paper_name = r[r.find('“') + 1: r.find('”') - 1]
    paper_names.append(paper_name)
    md_name = paper_name.lower()
    for c in special_characters:
        md_name = md_name.replace(c, '_')
    for _ in range(len(special_characters)):
        md_name = md_name.replace('__', '_')
    md_name += '.md'
    names.append(md_name)

correct_names = []
incorrect_names = []

correct_indexes = []
incorrect_indexes = []

for i, name in enumerate(names):
    correct = True
    for c in '0123456789':
        if c in name:
            correct = False
            break

    if correct:
        correct_names.append(name)
        correct_indexes.append(i)
    else:
        incorrect_names.append(name)
        incorrect_indexes.append(i)

os.mkdir('papers')
for name in correct_names:
    with open(os.path.join('papers', name), 'w') as f:
        f.write('# ' + name)

# TODO: change the wrong names here
corrected_names = [
    'ai_benchmark_all_about_deep_learning_on_smartphones_in_2019.md',
    'deep_learning.md',
    'rl2__fast_reinforcement_learning_via_slow_reinforcement_learning.md',
    'meta_learning_in_computational_intelligence.md',
    'the_theory_of_market_economy.md',
    'learning_a_synaptic_learning_rule.md',
    'domain_adaptation_in_computer_vision_applications.md',
    'humanlevel_performance_in_3d_multiplayer_games_with_populationbased_reinforcement_learning.md',
    'few_shot_human_motion_prediction_via_meta_learning.md',
    'searching_for_mobilenetv3.md',
    'nas_bench_101_towards_reproducible_neural_architecture_search.md',
    'nas_bench_201_extending_the_scope_of_reproducible_neural_architecture_search.md',
    'trends_in_the_us_and_canadian_pathologist_workforces_from_2007_to_2017.md'
]

for name in corrected_names:
    with open(os.path.join('papers', name), 'w') as f:
        f.write('# ' + name)

markdown_names = [''] * len(paper_names)

for i, name in zip(correct_indexes, correct_names):
    markdown_names[i] = name

for i, name in zip(incorrect_indexes, corrected_names):
    markdown_names[i] = name

data = {}
for i in range(len(markdown_names)):
    data[str(i + 1)] = {}
    data[str(i + 1)]['name'] = paper_names[i]
    data[str(i + 1)]['markdown'] = markdown_names[i]

with open('reference.json', 'w') as f:
    json.dump(data, f)
