import tweepy
import config
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Połączenie z Twitter API
client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# Baza danych SQLite
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS blocked_users (user_id TEXT)")
conn.commit()

class BlockUserRequest(BaseModel):
    user_id: str

@app.get("/comments")
async def get_comments(username: str):
    try:
        user = client.get_user(username=username)
        tweets = client.get_users_tweets(id=user.data.id, max_results=5, tweet_fields=["conversation_id"])
        
        all_comments = []
        for tweet in tweets.data:
            replies = client.search_recent_tweets(query=f"conversation_id:{tweet.conversation_id}", tweet_fields=["in_reply_to_user_id"])
            for reply in replies.data:
                all_comments.append({"text": reply.text, "user_id": reply.in_reply_to_user_id})
        
        return all_comments
    except tweepy.errors.TweepyException as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/block-user")
async def block_user(request: BlockUserRequest):
    cursor.execute("INSERT INTO blocked_users (user_id) VALUES (?)", (request.user_id,))
    conn.commit()
    return {"message": "User blocked"}
