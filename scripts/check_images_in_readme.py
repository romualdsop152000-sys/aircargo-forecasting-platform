import os
import re

README_PATH = os.path.join(os.path.dirname(__file__), '..', 'README.md')
IMAGES_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs', 'images')

with open(README_PATH, encoding='utf-8') as f:
    readme = f.read()

# Regex to find all image links in markdown
image_links = re.findall(r'!\[[^\]]*\]\((docs/images/[^)]+)\)', readme)

missing = []
for rel_path in image_links:
    abs_path = os.path.normpath(os.path.join(os.path.dirname(README_PATH), rel_path))
    if not os.path.isfile(abs_path):
        missing.append(rel_path)

if not image_links:
    print('Aucune image référencée dans le README.')
elif not missing:
    print('✅ Toutes les images référencées dans le README existent dans docs/images.')
else:
    print('❌ Images manquantes ou mal nommées:')
    for m in missing:
        print('-', m)
