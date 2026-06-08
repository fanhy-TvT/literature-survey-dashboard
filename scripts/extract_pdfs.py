import os
import argparse
try:
    import PyPDF2
except ImportError:
    os.system('pip install PyPDF2')
    import PyPDF2

def extract_text_from_pdfs(pdf_dir, output_file, pages_to_read=2, char_limit=3000):
    with open(output_file, 'w', encoding='utf-8') as out:
        for filename in os.listdir(pdf_dir):
            if filename.endswith('.pdf'):
                path = os.path.join(pdf_dir, filename)
                try:
                    with open(path, 'rb') as f:
                        reader = PyPDF2.PdfReader(f)
                        text = ''
                        # Read the first few pages (usually enough for abstract & intro)
                        for i in range(min(pages_to_read, len(reader.pages))):
                            text += reader.pages[i].extract_text() + '\n'
                        
                        out.write(f'--- {filename} ---\n')
                        out.write(text[:char_limit] + '\n\n')
                except Exception as e:
                    out.write(f'--- {filename} ---\nError extracting text: {e}\n\n')
    print(f"Extraction complete. Raw text saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract text from PDF papers')
    parser.add_argument('--input_dir', required=True, help='Directory containing PDF papers')
    parser.add_argument('--output_file', required=True, help='Output text file path')
    parser.add_argument('--pages', type=int, default=2, help='Number of pages to read per PDF')
    parser.add_argument('--chars', type=int, default=3000, help='Character limit per PDF')
    args = parser.parse_args()
    
    extract_text_from_pdfs(args.input_dir, args.output_file, args.pages, args.chars)
