import pandas as pd
import fetch_comment
from id_exists import exists


print("Video ID of this URL (https://www.youtube.com/watch?v=3rmeiTJX3mw) is '3rmeiTJX3mw'")
print("Enter Video ID: ",end = " ")

while(True):
    ID = input()
    # Check if it is valid ID
    if(exists(ID)):
        break
    print("Invalid ID. Try Again")
    print("Enter Video ID: ",end = " ")

try:
    # Check if this video already exists or not
    comments_id_ = pd.read_csv(f"./videos_id/{ID}.csv")
except:
    # Create new folder for this video ID
    pd.DataFrame({}).to_csv(f"./videos_id/{ID}.csv")
    comments_id_ = pd.read_csv("f./videos_id/{ID}.csv")

# change comments_id dataframe to list here
comments_id_done = list(comments_id_["0"])  # Check here is 0 is correct or not

comments, comments_id = fetch_comment.fetch(ID,comments_id_done)
# Check Repitition here
flags = fetch_comment.check_repitition(comments, comments_id_done)

# Save here to let sentiment access comments.csv file
fetch_comment.save_for_sentiment(comments_id,comments,flags)

# ====================================================================================

# Here comes the part where we go to sentimental analysis file to bring sentiments of a comments.
# Calculate sentiments of those which have flags value == True

# =====================================================================================


# =====================================================================================

# Here comes the part where we give authority to reply_on_comment.py for next operations.

# =====================================================================================