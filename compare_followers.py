from bs4 import BeautifulSoup
from typing import List


def get_user_profiles(file_path:str) -> List[str]:
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
    def __init__(self) -> None:
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
    followers = get_user_profiles('data/followers.html')
    following = get_user_profiles('data/following.html')
    print(f"You have {len(followers)} followers and {len(following)} following.")

    follower_tracker = FollowerTracker()
    follower_tracker.FOLLOWERS = followers
    follower_tracker.FOLLOWING = following

    friends = follower_tracker.get_friends()
    print(f"You have {len(friends)} friends.")


if __name__ == '__main__':
    main()
