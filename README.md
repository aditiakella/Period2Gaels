# Period 2: Gaels

## Links
* [Study Journal](https://docs.google.com/document/d/1NFgEh_1AZGfm3fGWLUgGT7Xm9tNoPROnnH0_pO72MzM/edit?usp=sharing)
* [Collaboration video](https://youtu.be/rLajlcMSnqM)
* [Scrum Board](https://github.com/aditiakella/Period2Gaels/projects/1)
* [Project Plan](https://docs.google.com/document/d/1wBFv8xEiTdBYL12SreRxs_ixNCXaxFt93r1jJ1S14m4/edit?usp=sharing)
* [Website on Rasberry Pi Web Server](http://tweeter.gq/)

# Scrum Team Cards
### Scrum Master Grading: 19/20 (For all team members)
* Deployment - Grace
    * Running Instructions: to run our website on the Raspberry Pi Web Server, click this [link](Tweeter.gq)
    * created a raspberry pi web server using these [instructions](http://nighthawkcoders.cf/lesson/pi-webserver/)
    * did port forwarding with our project using these [instructions](http://nighthawkcoders.cf/lesson/pi-portforward/)
    * created a domain called Tweeter.gq running our main [website](Tweeter.gq) on it
    * [Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-52163809)
* Web API - Aditi 
    * Running Instructions: In order to run the joke API, click the link to our [website](Tweeter.gq). Then, click on word “Birds” in the navbar. This is the joke API page and every time you click on “New Joke”, a new joke will be generated. 
    * I added th joke API to the project so I could get familiar with using APIs before moving on to incproprating my own API.
    * First I added an [app route on the views.py page](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L42-L50) so that the joke API could have it's own page
    * Then I created a file called [joke.html](https://github.com/aditiakella/Period2Gaels/blob/main/templates/joke.html), which was the code for the joke page. 
    * Then we had to install a package called [requests](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L3) in views.py so that the joke page could work. 
    * [Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-52589451)
* Feedback Page Set Up - Sophie
    * Running Instructions: In order to run the Feedback page, click the link to our [website](Tweeter.gq). Then, click “Feedback” in the NavBar of the homepage, and it should take you to a link where you answer a couple of questions. Once you are done, it will prompt you to hit “submit” and will take you to our Thank You page.
    * I added the [Responses page app route](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L52-L54) so that the feedback page wouldn't lead to an error once you hit submit
    * I added the colors and questions to the [Feedback page](https://github.com/aditiakella/Period2Gaels/blob/main/templates/Feedback.html)
    * I made an [app route for the Feedback page](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L12-L14)
    * [Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-52906850)
 

## Scrum Team Members
* Aditi Akella
* Sophie Bulkin
* Grace Le
* Luke Manning (joined week 6)

## Project Overview
A bird website called "Tweeter" that has a data base for the different types of birds. We will use web scraping to find the different types of birds that will be divided based on their specie, or order, with sub menus allowing you to pick the specific bird that you want to explore. We will use the bird api as a resource and use more advanced techniques that will be evident at N@M and fufill all of the College Board requirments. We will use Python, HTML, CSS, and Flask to develop our project and deploy our website on a rasberry pi. 

## Project Components 
* home page 
* Drop down of order of birds and sub drop down with each type of bird
* Added HTML files to each dropdown menu
* About us page
    * Introduce team membbers
    * Describes the project in more detail
* categories on the orders of birds 
* nav bar

## 5 Hour Challenge
* finshed homepage and organization
* added about us page
* added phylogenetic page and images
* worked on organization and formatting
