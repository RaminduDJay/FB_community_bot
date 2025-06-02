import facebook
import requests

def post_to_facebook(content, image_path):
    graph = facebook.GraphAPI(access_token="YOUR_FACEBOOK_TOKEN")
    
    # Upload image
    with open(image_path, "rb") as img:
        graph.put_photo(image=img, message=f"{content['headline']}\n\n{content['body']}\n\n{content['link']}")
    
    print("Post published!")

def get_comments(post_id):
    graph = facebook.GraphAPI(access_token="YOUR_FACEBOOK_TOKEN")
    comments = graph.get_connections(id=post_id, connection_name="comments")
    return [{"id": c["id"], "text": c["message"]} for c in comments["data"]]

def reply_to_comment(comment_id, reply_text):
    graph = facebook.GraphAPI(access_token="YOUR_FACEBOOK_TOKEN")
    graph.put_object(parent_object=comment_id, connection_name="comments", message=reply_text)