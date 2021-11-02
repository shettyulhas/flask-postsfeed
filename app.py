import uuid
import os
import json
from flask import Flask, request, jsonify, render_template
from models import get_session, User, Profile, Post, create_all, db_query


app = Flask(__name__)

# rows_per_page = 5

@app.route('/user/create', methods=['POST'])
def create_user_endpoint():
    r = request.json
    username = r.get('username')
    first_name = r.get('first_name')
    last_name = r.get('last_name')
    session = get_session()
    user = User()
    profile = Profile()
    user.user_uuid = str(uuid.uuid4())
    user.username = username
    profile.user_uuid = user.user_uuid
    profile.first_name = first_name
    profile.last_name = last_name
    user.profile = profile
    u = session.merge(user)
    session.commit()
    session.close()
    return jsonify({'return': 'success'}), 200


## Seeding DB table u_post with posts data using POST method
@app.route('/seed-db', methods=['GET', 'POST'])
def seed_db():

    ## Check and laod data if feed data file exists; else, return message that feed file is unavailable 
    if os.path.exists('./data/feed.json'):
        ## Open session to get session info
        session = get_session()

        ## Read data from feed file
        with open('./data/feed.json') as feedfile:
            feed_data = json.load(feedfile)

        for feed in feed_data:
            # print(feed)

            ## Create Post() DB object
            post = Post()
            
            ## Read column values from each feed object and load it to Post() object to load into DB table
            post.caption = feed['caption']
            post.followers = feed['followers']
            post.image_url = feed['image_url']
            post.likes = feed['likes']
            post.profile_image_url = feed['profile_image_url']
            post.title = feed['title']
            post.username = feed['username']
            
            ## Commit data to DB table
            session.add(post)
            session.commit()

        ## Close session
        session.close()
    
        return 'DB loaded'

    else:
        return 'Feed File Unavailable'


## Getting posts data from DB table u_post using GET method
@app.route('/get-data', methods=['GET'])
def get_data():

    db_query()

    # Set pagination configuration
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.paginate(page=page, per_page=rows_per_page)

    ## Get all datarows from DB table and pass it to index.html file for rendering
    posts = Post.query.order_by(Post.username).all()
    return render_template('index.html', posts=posts)
    

if __name__ == '__main__':
    if not os.path.exists('app.db'):
        create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)