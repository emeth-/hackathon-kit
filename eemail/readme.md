Mailgun setup - Make a new route with these settings:
    catch_all()
    forward("http://yoursite.herokuapp.com/email/catch_all")
