def aditis_info():
    name = "Aditi Akella"
    grade = "11th grade"
    about = "Hello! I am Aditi and I am a Junior at Del Norte. I love animals, travel, and science. This is my first year in Mr. M's class and I am learning so much about Python and html files! I look forward to learning more about computers and programming."
    contributions = "Contributions: I created the about us page and the Jinja templates, and I also added most of the app routes on views.py and passed data through the back end. I also created the simple database and incorporated the joke API."
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions}
    return info

def sophies_info():
    greeting = "Hi!"
    name = "Sophie Bulkin"
    grade = "11th grade"
    about = "Hello! I am Sophie and I am an eleventh grader at Del Norte. I took a  Computer Science class last year with Mr.M and it has been a very fun experience. I have learned different types of coding from basic Python fundamentals to .html. I hope to further improve from here."
    contributions = "Contributions: about us page, prototypes,sophie.html, feedback"
    info = {"greeting": greeting, "name": name, "grade": grade, "about": about, "contributions": contributions}
    return info

def graces_info():
    greeting = "Hi!"
    name = "Grace Le"
    grade = "11th grade"
    about = "Hi my name is Grace and I am a junior at Del Norte High School. I am taking Computer Science for the first time this year and I am very excited to see people enjoying what I code. I have learned different types of coding languages and hopefully learning more and improving."
    contributions = "Contributions: Fill in"
    info = {"greeting": greeting, "name": name, "grade": grade, "about": about, "contributions": contributions}
    return info

def lukes_info():
    greeting = "Hi!"
    name = "Luke Manning"
    grade = "th grade"
    about = "About: Fill in"
    contributions = "Contributions: Fill in"
    info = {"greeting": greeting, "name": name, "grade": grade, "about": about, "contributions": contributions}
    return info

def lukes_info():
    greeting= "Hello!"
    name = "Luke Manning"
    grade = "12th grade"
    about = "Hi my name is Luke Manning and I am a senior at Del Norte"
    contributions = "Contributions: "
    info = {"greeting": greeting, "name": name, "grade": grade, "about": about, "contributions": contributions}
    return info

def alldata():
    return [aditis_info(), sophies_info(), graces_info(), lukes_info()]