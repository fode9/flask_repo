from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/article/<int:id>')
def article(id):
    # Fetch article by ID (placeholder example)
    article = {
        'id': id,
        'title': 'Sample Article',
        'content': 'This is a sample article.',
        'author': 'Author Name',
        'date': '2024-07-26'
    }
    return render_template('article.html', article=article)

@app.route('/category/<string:category>')
def category(category):
    # Fetch articles by category (placeholder example)
    articles = [
        {'id': 1, 'title': 'Sample Article 1'},
        {'id': 2, 'title': 'Sample Article 2'}
    ]
    return render_template('category.html', category=category, articles=articles)

@app.route('/search')
def search():
    query = request.args.get('q')
    # Perform search (placeholder example)
    results = [
        {'id': 1, 'title': 'Search Result 1'},
        {'id': 2, 'title': 'Search Result 2'}
    ]
    return render_template('search.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)

