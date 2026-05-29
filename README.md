# BookBot 📚

A command-line tool that analyzes any `.txt` file and generates 
a detailed report with word count, top 10 most used words, 
and character frequency.

## 🛠️ Technologies
- Python
- Rich (terminal formatting)

## 🚀 How to Run
1. Clone the repo
2. Run: `uv init --no-readme`
3. Install dependencies: `uv add rich`
4. Run: `uv run main.py <path_to_book>`

## Example
uv run main.py books/frankenstein.txt

## 📊 Output
- Total word count
- Top 10 most used words
- Character frequency sorted from most to least common