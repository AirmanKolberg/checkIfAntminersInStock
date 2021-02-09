from selenium import webdriver

firefox = webdriver.Firefox()
bitmain_url = 'https://shop.bitmain.com/product/detail?pid=00020201222165500548JAa69Gvu067A'
gmail_url = 'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
subject_line = 'ANTMINER IN STOCK!'

# You could and should, of course, change the name
# to whom this robot is addressing.
message_body = f"""T.J.,

The Antminer S19 Pro is in stock!
Here's a link:  {bitmain_url}

Respectfully,
Your robot
:)"""
