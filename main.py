import os

base_dir = 'markdown/'
os.makedirs(base_dir, exist_ok=True)

def parse_bible_text(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    verses = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue 

        parts = line.split('\t', 1)
        if len(parts) != 2:
            continue  

        verse_ref, content = parts
        book, chapter_verse = verse_ref.rsplit(' ', 1)

        if book not in verses:
            verses[book] = []
        verses[book].append((chapter_verse, content))
    
    return verses

def write_verse_files(verses):
    for book, verse_list in verses.items():
        book_dir = os.path.join(base_dir, book)
        os.makedirs(book_dir, exist_ok=True)

        for chapter_verse, content in verse_list:
            file_name = f'{book} {chapter_verse}.md'
            file_path = os.path.join(book_dir, file_name)

            with open(file_path, 'w') as f:
                f.write(f'# {book} {chapter_verse}\n\n{content}')

if __name__ == '__main__':
    bible_file = './bible/kjv.txt'
    verses = parse_bible_text(bible_file)
    write_verse_files(verses)
    
    print("Makdown files generated successfully.")
