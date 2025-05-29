# ✅ This is your FINALIZED app.py with proper imports and DSA integration

from flask import Flask, request
from bert_classifier import predict
from url_parser import extract_text_from_url
from parser import parse_article_to_tree
from flags import extract_red_flags, word_frequency
import re

app = Flask(__name__)

def get_full_sentence_snippet(text, limit=400):
    text = text.strip().replace('\n', ' ')
    sentences = re.split(r'(?<=[.!?]) +', text)
    result = ""
    for sentence in sentences:
        if len(result) + len(sentence) > limit:
            break
        result += sentence + " "
    return result.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        raw_text = request.form.get('article')

        if url:
            raw_text = extract_text_from_url(url)

        if not raw_text or raw_text.startswith("[ERROR"):
            return f"<h3>Error extracting or missing text.</h3><pre>{raw_text}</pre>"

        # ✅ Run BERT prediction
        label, score = predict(raw_text)

        # ✅ Use DSA: Tree ADT to structure article
        tree = parse_article_to_tree(raw_text)
        sections_html = "<ul class='list-group'>"
        for child in tree.children:
            snippet = get_full_sentence_snippet(child.text)
            sections_html += f"<li class='list-group-item'><b>{child.section}</b>: {snippet}</li>"
        sections_html += "</ul>"

        # ✅ Use DSA: Red flag priority queue
        flags = extract_red_flags(raw_text)
        flag_list = "<ul class='list-group'>" + "".join([f"<li class='list-group-item text-danger'>{f.message} (Severity {f.severity})</li>" for f in flags]) + "</ul>"

        # ✅ Explanation Material
        explanation = ""
        if label == "FAKE":
            explanation = "<div class='alert alert-danger'><b>Reasoning:</b> The article contains high emotional tone, lacks credible sources, or includes potential clickbait signals.</div>"
        else:
            explanation = "<div class='alert alert-success'><b>Reasoning:</b> The language and structure of the article align with patterns found in verified, factual news reports.</div>"

        return f"""
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <title>IsThisReal - Result</title>
            <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>
            <style>
                body {{ 
                    background-color: #f8f9fa;
                    background-image: url('/static/question-bg.png');
                    background-size: 150px;
                    background-repeat: repeat;
                    background-attachment: fixed;
                    backdrop-filter: blur(2px);
                    opacity: 0.95;
                }}
                .section-block {{ background: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }}
                pre {{ background: #f1f1f1; padding: 15px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <div class='container mt-5'>
                <h1 class='mb-4 text-center'>IsThisReal - Fake News Detector</h1>
                <div class='section-block'>
                    <h2>{label} ({round(score * 100, 2)}%)</h2>
                    {explanation}
                </div>
                <div class='section-block'>
                    <h4> Red Flags (Priority Queue)</h4>
                    {flag_list}
                </div>
                <div class='section-block'>
                    <h4>DSA: Article Structure (Tree ADT)</h4>
                    {sections_html}
                </div>
                <div class='section-block'>
                    <h4>Full Article Text</h4>
                    <pre>{raw_text}</pre>
                </div>
                <div class='text-center'>
                    <a href='/' class='btn btn-secondary mt-3'>🔁 Analyze Another Article</a>
                </div>
            </div>
        </body>
        </html>
        """

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>IsThisReal - Fake News Detector</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
                background-image: url('/static/question-bg.png');
                background-size: 150px;
                background-repeat: repeat;
                background-attachment: fixed;
                backdrop-filter: blur(2px);
                opacity: 0.95;
            }
            .container { max-width: 800px; }
            textarea { resize: vertical; }
        </style>
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4 text-center">IsThisReal - Fake News Detector</h1>
            <form method="post" class="card p-4 shadow-sm">
                <div class="mb-3">
                    <label class="form-label"><b>Paste a News Article URL</b></label>
                    <input type="text" class="form-control" name="url" placeholder="https://news.example.com/some-article">
                </div>
                <div class="text-center mb-2">— OR —</div>
                <div class="mb-3">
                    <label class="form-label"><b>Paste Raw Article Text</b></label>
                    <textarea name="article" class="form-control" rows="8" placeholder="Paste article text here..."></textarea>
                </div>
                <button type="submit" class="btn btn-primary w-100">🔍 Check News</button>
            </form>
            
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
