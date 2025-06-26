# Import needed libraries
from instagrapi import Client
import random as r
import time
import schedule

# Credentials
USERNAME = "nethulann"
PASSWORD = "nethula@2009"

# Posts to search for
tags = ["pixelart", "gamedev", "indiegame", "pythoncoding"]

# Comments
comments = ["Great work!", "Keep it up", "Nice", ":)"]

# Function to search for posts with certain tags, leave a nice comment, and
# then follow the creator
def search_tags():
    # Creating the client object
    client = Client()

    # Log in using credentials
    client.login(USERNAME, PASSWORD)

    num_interaction_posts = r.randint(1, 5)

    # Sleep, and then search for posts
    time.sleep(r.randint(2000, 7000)/1000)
    tag_choice = r.choice(tags)
    hashtag_posts = client.hashtag_medias_recent(tag_choice)

    print(f"--- Searched TAG ({tag_choice}) ---")
    print(f"--- Proceeding to interact with {num_interaction_posts} posts ---")

    chosen_post_ids = []

    # Insert indices of which posts to like
    for i in range(num_interaction_posts):
        insertion_index = r.randint(0, len(hashtag_posts) - 1)

        while insertion_index in chosen_post_ids:
            insertion_index = r.randint(0, len(hashtag_posts) - 1)

        chosen_post_ids.append(insertion_index)

    # Go through each post, and decide to like, comment, and/or follow
    for i in chosen_post_ids:
        print(f"--- Interacting with POST caption - '{hashtag_posts[i].caption_text}' ---")

        # Chance to like (50% chance to like)
        like = True
        if r.randint(0, 100) <= 50:
            like = False
        
        # Chance to follow (75% chance to follow)
        follow = True
        if r.randint(0, 100) < 25:
            follow = False

        # Chance to comment (10% to comment)
        comment = True
        if r.randint(0, 100) < 90:
            comment = False

        # Get the media and user IDs
        media_id = hashtag_posts[i].pk
        user_id = hashtag_posts[i].user.pk

        time.sleep(r.randint(4000, 8000)/1000)

        # Try poitential LIKE
        if (like):
            time.sleep(r.randint(2000, 7000)/1000)
            try:
                client.media_like(media_id)
            except Exception as error:
                print("Too many like requests. Slow down commenting")

            print("--- Post LIKED ---")
        
        # Try potential FOLLOW
        if (follow):
            time.sleep(r.randint(3000, 9000)/1000)

            try:
                client.user_follow(user_id)
            except Exception as error:
                print("Too many follow requests. Slow down commenting")

            print("--- User FOLLOWED ---")

        # Try potential COMMENT
        if (comment):
            time.sleep(r.randint(7000, 12000)/1000)

            try:
                client.media_comment(media_id, r.choice(comments))
            except Exception as error:
                print("Too many comment requests. Slow down commenting")

            print("--- Post COMMENTED ---")

search_tags()

# # Scheduling
# time_1 = str(r.randint(8, 11)) + ":" + str(r.randint(0, 59))
# time_2 = str(r.randint(13, 15)) + ":" + str(r.randint(0, 59))

# schedule.every().day.at(time_1).do(search_tags)  # Example: 9:00 AM
# schedule.every().day.at(time_2).do(search_tags)  # Example: 3:30 PM

# print("Scheduled times for\n" + time_1 + "\n" + time_2)

# # Keep the script running indefinitely
# while True:
#     schedule.run_pending()  # Check for pending jobs
#     time.sleep(1)  # Wait 1 second before checking again