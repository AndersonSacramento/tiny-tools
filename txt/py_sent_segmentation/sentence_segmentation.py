import argparse
import spacy


def read_text_chunks(in_path):
    text_chunks = []
    with open(in_path) as in_file:
        for line in in_file:
            line = line.strip()
            if not line:
                yield ' '.join(text_chunks)
                text_chunks = []
            else:
                text_chunks.append(line)

def segment_text_chunks(text_chuncks):
    for text in text_chuncks:
        for sent in nlp(text).sents:
            yield sent
        
        
def write_sentences(sentences, out_path):
    with open(out_path, "w", encoding="utf-8") as out_file:
        for sentence in sentences:
            out_file.write(sentence.text.strip())
            out_file.write("\n")
            
    
if __name__ == '__main__':
    global nlp
    
    parser = argparse.ArgumentParser(description="Sentence input document into one sentence per line output document")
    parser.add_argument("-in_path", type=str,
                        help="Input file path to txt document")
    parser.add_argument("-out_path", type=str,
                        help="Output file path to txt document with segmentated sentences")


    args = parser.parse_args()

    nlp = spacy.load("en_core_web_sm")
    write_sentences(segment_text_chunks(read_text_chunks(args.in_path)),
                     args.out_path)
    
