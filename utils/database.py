from pymongo import MongoClient

db = MongoClient(
    "mongodb+srv://techzbots:4tQYI1SD64nr8jz5@rankingsbot.h5std55.mongodb.net/?retryWrites=true&w=majority"
).TechZDeployer.users


def inc_user(user, name, link):
    db.update_one(
        {"user": user},
        {"$inc": {"count": 1}, "$push": {"repos": [name, link]}},
        upsert=True,
    )


def repo_count(user):
    user = db.find_one({"user": user})
    if not user:
        return 0
    return user.get("repos", 0)
