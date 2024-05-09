import os
import sqlite3
from bs4 import BeautifulSoup


def create_sqlite_db(db_name):
    if not os.path.exists(db_name):
        try:
            with sqlite3.connect(db_name) as conn:
                cursor = conn.cursor()
                create_tables(cursor)
                conn.commit()
            print(f"Database '{db_name}' created successfully.")
        
        except sqlite3.Error as e:
            print(e) 
    else:
        print(f"Database '{db_name}' already exists.\nRunning updates...")

def create_tables(cursor):
    sql_statements = [
        '''CREATE TABLE followers
            (username TEXT, date_added DATE)''',
        '''CREATE TABLE following
            (username TEXT, date_added DATE)''',
        '''CREATE INDEX idx_followers_username ON followers (username)''',
        '''CREATE INDEX idx_following_username ON following (username)''',
    ]
    for statement in sql_statements:
        cursor.execute(statement)


def get_user_profiles(file_path):
    try:
        with open(file_path, "r") as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, "html.parser")
            # get <a> tags
            anchors = soup.find_all("a")
            # get profile links
            links = [link.get("href") for link in anchors if link.get("href")]
            return links

    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


class FollowerTracker():
    def __init__(self):
        self.FOLLOWERS = []
        self.FOLLOWING = []

    def get_friends(self):
        followers = set(self.FOLLOWERS)
        friends = []
        for following in self.FOLLOWING:
            if following in followers:
                friends.append(following)
        return friends

    def user_does_not_follow_back(self):
        pass

    def does_not_follow_back_user(self):
        pass

    def unfollowers(self):
        pass


def main():
    create_sqlite_db('ig_tracker.db')

    # followers = get_user_profiles('data/followers.html')
    # following = get_user_profiles('data/following.html')
    # print(f"You have {len(followers)} followers and {len(following)} following.")

    # follower_tracker = FollowerTracker()
    # follower_tracker.FOLLOWERS = followers
    # follower_tracker.FOLLOWING = following

    # friends = follower_tracker.get_friends()
    # print(f"You have {len(friends)} friends.")


if __name__ == '__main__':
    main()
