from instapy import InstaPy

# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username, password=insta_password)
session.login()
print("logged")

get_nonfollowers = session.pick_nonfollowers(username="pasan.creation", live_match=True, store_locally=False)


print(get_nonfollowers)
non = get_nonfollowers

print("\n".join(non))
f = open("get_nonfollowers.txt", 'w')
f.write("\n".join(non))

print("saved as get_nonfollowers.txt")
