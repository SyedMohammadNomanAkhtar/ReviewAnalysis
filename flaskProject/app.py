from flask import Flask, jsonify
from textblob import TextBlob
import pyodbc
from sqlalchemy import create_engine, MetaData, Table, select, update
from sqlalchemy.orm import scoped_session, sessionmaker

from conn import conn_str

app = Flask(__name__)

@app.route('/analyze-sentiments', methods=['POST'])
def analyze_sentiments():
    # Establish a connection to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Fetch reviews where the Outcome is NULL
    cursor.execute("SELECT ReviewId, ReviewText FROM Reviews WHERE Outcome IS NULL")
    reviews = cursor.fetchall()

    # Iterate over the fetched reviews
    for review in reviews:
        review_id, review_text = review

        # Perform sentiment analysis on the review text
        blob = TextBlob(review_text)
        sentiment = 'Positive' if blob.sentiment.polarity > 0 else 'Negative'

        # Update the Outcome column based on the sentiment analysis
        cursor.execute("UPDATE Reviews SET Outcome = ? WHERE ReviewId = ?", (sentiment, review_id))
        conn.commit()  # Commit the transaction

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return jsonify({"message": "Sentiment analysis completed and outcomes updated."})

if __name__ == '__main__':
    app.run(debug=True)
