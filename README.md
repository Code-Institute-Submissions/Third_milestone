# Surfingeurope

The [surfingeurope](https://surfingeurope.herokuapp.com/) is a Data Centric Development Milestone Project build for [Code Institute's](https://www.codeinstitute.net/) Full Stack Web Developer Course.

The Surfingeurope website is a surfing locations guide that allows surfers to explore various types of spots in Europe. The site has a social aspect by allowing users to add new locations, edit current spots and rate or comment on the existing ones based on their personal experience and knowledge.

## The Brief

The project brief required to build a data-driven web application using technologies learned throughout Data Centric Development module. The core technologies for this particular project include Python and Flask framework being the logic and Html, Css, Javascript and D3js library as a structure and visualization. The CRUD operations were carried out using NoSQL MongoDB database. 

## UX

The UX process played a major role in the design of the Surfingeurope application with all of its components playing equally important role.

### Strategy

The Surfingeurope website is created for surfers to allow them to explore spots all over Europe and to engage with fellow surfing enthusiast. The main aim of the application is to promote travel and to share otherwise unknown locations and local knowledge between users. 

Based on the above description and the research process the following user stories were identified:

- As a user A, I want to see the top rated locations.
- As a user B, I want to see list of all locations.
- As a user C, I want to filter the locations by spot name, country and rating.
- As a user D, I want to be able to search a location by name.
- As a user E, I want to be able to tailored search by selecting specific location characteristic like break type or wave direction.
- As a user F, I want to be able to search locations by a specific facility type.
- As a user G, I want to be able to exclude certain hazards from a location search.
- As a user H, I want to be able to explore location in detail.
- As a user I, I want to edit an existing location which I believe has a mistake.
- As a user J, I want to be able to create a new location.
- As a user K, I want to be able to delete a location which I believe was added by mistake.
- As a user L, I want to rate a location based on my preference.
- As a user M, I want to be able to comment on a location of my choice.
- As a user N, I want to see all my rates and comments under my personal page so I can easily access my spots.
- As a user O, I want to be able to track all the spots I created or edited under my personal page.
- As a user P, I want to see some data showing number of locations per break type and bottom type.
- As a user Q, I want to see some data showing the most popular facilities for all of the locations.
- As a user R, I want to see some data showing the most common hazards for all of the locations.

### Scope

The Surfingeurope website should focus on user engagement by allowing users to create new locations and to edit existing spots in order to amend incorrect data. The users should be able as well to rate and comment on the spots to help other fellow surfers in making their future surf travel choices. In order to help in making that decision, each of the surfing locations should have spot features including but not limited to break type, bottom type, wind direction, type of available facilities and occurring hazards. These features together with location description would allow surfers to find at least one spot that is matching their surfing style and abilities.

### Structure

Based on the strategy and scope, the website structure should have clearly organized content and should allow an intuitive interaction for the users. The website should lack any clutter and be informative as much as possible at the same time. There shouldn't be any distractions to the users and the focus should be placed on providing the surfing location features and to stimulate users to interact with the site. 

### Skeleton

The following wireframes were created to determine the visual form and arrangement of the application elements:

- <a href="mockups/Small_device.png" target="_blank">Small device.</a>
- <a href="mockups/Medium_device.png" target="_blank">Medium device.</a>
- <a href="mockups/Large_device.png" target="_blank">Large device.</a>

### Surface

Once the wireframes were in place, the following visuals were introduced:

- The base colors for the site are green and blue with its different shades and white as the main background color. These colors were selected to match with the surfing theme i.e. colors of the ocean.
- Typography is limited to three Google typefaces with "Roboto" being the default one. It's a clean and modern sans serif typeface makes the site readable on both small and large devices. The other two are "Kaushan Script" and "Oswald". The first one was used as a base for Surfingeurope logotype and occasionally on the website to give the content some vibrant feel. The later, being a reworking of the classic gothic typeface style is used to put an emphasis on text content due to its better fit to the pixel grid of a standard digital screens.
- The website logotype and its shortcut are custom made making the site more stylish and memorable.
- The website assets include photographs, either taken from stock photography or provided by users as a surfing location image. They photographs that are used to style the application were carefully selected and edited to create a consistent overall design.

## Features

The main idea behind the Surfingeurope application is to help users in finding location that suits their needs and providing them with smooth interaction with the site and engagement with other users. The following features play a major role in that process:

- Home page.
- Page with list of all locations.
- Detailed view of the selected spot.
- Locations search functionality.
- Ability to edit existing or add a new location.
- Data Charts.
- User personal space.

### Home Page

The landing page consists of a large image with a button that leads users to page listing all of the locations and a welcome text. The remaining content consists of three top rated locations cards promoting the best spots in Europe and three randomly selected locations allowing users to explore some other spots.

### All Locations Page

There are two main elements of that page. The top element allow users to sort the list of locations by name being the default view, country and rating. There is a search button underneath the filters that allows quick transition to the search page for a more tailored results.

The bottom element display list of locations cards based on the selected filter. The amount of location cards is limited to 6 per page to avoid clutter and intensive scrolling. At the bottom of the list, there is a pagination range display making navigation between spots quick and easy.

### Location Detailed View

The user can access details of any of the surfing locations at any time by selecting the card that represents particular spot. Once the card is trigged it will open a page with location details and available interaction. The details page consists of the following fields:

- location name
- country name
- region name
- spot features including:
    - break type
    - wave direction
    - wind direction
    - swell direction
    - bottom
    - surroundings
- facilities
- hazards
- description
- ratings
- comments
- author/editor

The user has an option to rate or comment on the location and edit it content. Furthermore, if the user is an author of that record, he/she can remove it from the application. All of these choices are clearly visible and assigned to buttons.

At the bottom of the page, the user has recommendation for three randomly selected locations awaiting for exploration.

### Search Functionality

The search page consists of two search options. The initial one, which is being displayed by default is the search by location name. This search has an autocomplete feature making it easier to find a spot in the database.

The second option is revealed once the user selects the "advanced search" text. Once engaged, the initial search will be replaced by a form giving user much wider selection of options to narrow the search. The user can go back to name search by selecting "search by name" text. The advanced search selection include:

- country name
- break type
- wave direction
- bottom
- facilities to include in the search
- hazards to exclude from the search

The user has freedom to specify only the options that he believe are necessary for his query. If there are no results matching either of the searches, the user will be redirected to error page and notified about lack of results.

### Add or Edit Location

The main concept of the application is to engage users to share their local knowledge by adding new spots to the site. In order to add a new location user needs to provide a unique spot name. Once the name is validated in order to ensure no duplications are created, the user is provided with a form containing all of the spot features. The user is again required to fill all the fields beside facilities and hazards, which can remain unchecked if none of the options match the spot characteristics. Once all data is provided user is able to add new location to the site.

Similar approach exists for the ability to edit existing location. The user is provided with all existing details of the spot but is given choice to change only the features he/she wants to overwrite, add or remove.

The name of the user whether creator or editor of the spot will be saved and displayed in the location detailed view.

### Data Charts

In order to give users and visitors some overview of the growing list of locations, a data charts are provided in the about page. The data is broken into two parts. Part one is showing two bar charts giving overview of number of locations per break type and bottom type. The second part display two pie chart showing the most common facilities and hazards for all locations.

### User Personal Space

The user personal space page contain all of the user interactions with the application. The personal space page can only be access by login into the site. The user will find all of the locations he/she created, edited, commented on and rated. All of the edits and comments will include the exact time and date of the input. The user will be able to view details of the spots he/she interacted with by selecting the name of the spot.

### Other Features

The other features of the Surfingeurope are as follows:

- Responsive layout that allows users to preview website on all devices.
- Simple and clean design with intuitive navigation and simplified data.
- Custom button styles which adds meaning and visual indication.
- Hover effect on clickable content to help users navigate and interact with the application.
- Notifications and personalised messages for visitors and logged users that either greets them, notify about user valid changes or display errors if needed, makes the connection more user friendly.

### Features Left to Implement

- Password input requirements to be added.
- Pagination to have limit of displayed page numbers with hidden excess of pages beyond the limit.
- Add Google Map API to show locations on the map.
- Add a image gallery for each location.
- Prevent showing a spot in the random locations display if the spot is already display on the page.
- Provide users with list of similar locations that match their preference based on the user ratings of other spots.

## Database Schema

The NoSQL MongoDB database was used to store the application data. Initially, the database contain 10 collections with "locations.json" being the main one as it contain all of the surfing spots details nested within. All of the other 9 collections were later on merged into one nested collection of documents called "categories.json" in order to reduce the number of collections and to efficiently use the MongoDB features.

These two main collections were updated multiple times during the development of the application. The main adjustments were the addition of rating, image url and author for each of the surfing location documents.

Each time the collections were updated and stored in JSON format, they were imported into MongoDB Shell via `mongoimport` tool.

These two collections are as follows:

- <a href="db_schema/locations.json" target="_blank">Locations collection.</a>
- <a href="db_schema/categories.json" target="_blank">Categories collection.</a>

The other collection called "users" were added to the database once the registration and rating were introduced. It stores users names for verification and personal page purposes.

## Technologies Used

The following languages, technologies and tools were used to construct this website:

- [Python](https://www.python.org/) - Used for application logic.
- [Flask](http://flask.pocoo.org/) - A microframework for Python.
- [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python.
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript) - Used to make the application interactive.
- [HTML5](https://www.w3.org/TR/html52/) - Core structure of the website.
- [CSS](https://www.w3.org/Style/CSS/) - Main style of the website.
- [Materialize](https://materializecss.com/) - Used to develop responsive website fast and efficiently.
- [3D.js](https://d3js.org/) - Used to produce bar and pie charts data visualizations inside the application.
- [Dc.js](https://dc-js.github.io/dc.js/) - A javascript charting library with native crossfilter support.
- [MongoDB](https://www.mongodb.com/) - A NoSQL database used to build the application.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - A automated cloud MongoDB service.
- [Jasmine](https://jasmine.github.io/) - A behaviour-driven development framework for testing JavaScript code.
- [Jasmine-jquery plugin](https://github.com/velesin/jasmine-jquery) - A extension for Jasmine Testing.
- [Balsamiq Mockups](https://balsamiq.com/) - Used to sketch quick wireframes for website's UX design.
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/) - Chrome browser tool used to iterate and debug the website.
- [HTML Checker](https://validator.w3.org/nu/) - Online HTML checker used to validate code semantics.
- [JSHint](https://jshint.com/) - Online Static Code Analysis Tool for JavaScript.
- [PEP8](http://pep8online.com/) - Online PEP8 checker.
- [Parallels](https://www.parallels.com/) - Software providing hardware virtualization used to test application on other platforms like Windows or Linux.  
- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) - Online Chrome tool used to audit the website's performance and accessibility.
- [Caniuse](https://caniuse.com/) - Online browser support tables for modern web technologies.
- [Github](https://github.com/) - Project's repository.
- [Visual Studio Code](https://code.visualstudio.com/) - Text editor used to write down all the code.
- [Google Fonts](https://fonts.google.com/) - Typefaces used to style the website.

## Testing

During the website development stage I have conducted two types of testing, manual and automated. The manual testing was ongoing throughout the whole development stage while the automated test was conducted using Python and Jasmine framework when the project was at its finish.

### Manual Testing

The manual testing consisted mainly of the following technologies/tools:

- Chrome DevTools

Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. This tools allows me to instantly preview and edit my website but I was mainly using it to diagnose problems and fix them on the go.

- Operating Systems:
    - MacOS
    - Microsoft Windows
    - Linux
    - Android
    - iOS

The Operating Systems test played an important part of the manual testing. Majority of the test was done using the Parallels software on MacOS which allows me to test my application on Linux and Windows virtual machines. The test consisted of running the application on the most popular browsers within these Operating Systems and validating the expected behaviour of the site.

- Web browsers:
    - Chrome
    - Firefox
    - Safari
    - Opera
    - Internet Explorer

In order to make sure that there are no errors with the application I was doing a cross browser testing from time to time. It basically consisted of running the site on these browsers, changing the size of the browser window and where possible using the native developer tools to check site responsiveness and functionality. These tests were run on desktop, tablet and smartphone devices.

- Devices:
    - desktop
    - tablet
    - smartphone

I run a manual testing on few types of devices whenever I had a chance but mainly I was testing the website using desktop, tablet and smartphone, so I could cover the most popular screen sizes.

- User Stories Testing

The following user stories from the UX section were tested to make sure everything works as intended:

1. User "A" wants to see the top rated locations. In order to satisfied that need, visitors are provided with a list of 3 top rated spots at the landing page. It is possible as well to filter all of the available location by rate by visiting the "All Locations" page.

2. User "B" wants to see list of all locations and user "C" wants the possibility to filter them by name, country and rating. The following steps needs to be conduct in that case:

    1. Navigate to the "All Locations" page where all of the spots are displayed showing 6 location cards by page. By default they are sorted alphabetically by location name.
    2. Select one of available buttons at the top of the page to sort locations by either country, rating or spot name.

3. Users "D", "E", "F" and "G" wants to search for location based on various search criteria’s. The following steps needs to be conduct in that case:

    1. Navigate to the "Search" page where users are provided with a basic search by location name and an option for advanced search if required.
    2. In order to search locations by name, user is required to type spot name in the provided input form. The form has a autocomplete functionality in order to help with that search and a "Search" button which once clicked will either display search result or a lack of results message.
    3. The visitors have option to tailor their search results by selecting the "Advanced search". Once that option is selected a new form will be displayed showing dropdown lists and checkboxes.
    4. Users can select any given value from the dropdown lists, e.g. "reef break" from break type, "right" from wave direction, etc.
    5. Users have option to include in the search any of the listed facility types by clicking on the checkbox beside facility type.
    6. Users have option to exclude in the search any of the listed hazard types by clicking on the checkbox beside hazard type.
    7. Once the selection is made, users should click the "Search" button which will either display search results or a lack of results message.

4. User "H" wants to explore a location of choice in detail. There are various ways to do so. User can access any location details by clicking on location card with the location image, name, country and region. The location cards can be found on the "Home", "All Locations" and "Search" pages. If the user is registered, the locations name that he/she either created, edited, rated or commented on, will be listed under his/hers name page with a direct link to detailed spot view.

5. Users "I", "K", "L" and "M" wants a possibility to either edit, delete, rate or comment on a location of their choice. All of these actions required user to be registered with an exception to removing a spot, where the user needs to be the author of that location as well. The following steps needs to be conduct in that case:

    1. Users should find a location of choice either by going through the list of available locations, searching location by name or by browsing through list of advanced search results. If the location of interest was created by the user, or previously edited, rated or commented, it can be found as well under user's personal page.
    2. Once the spot is located, users should select it in order to be redirected to detailed view.
    3. Once in detailed view, users can either "rate or comment", "edit location" or "remove" it by clicking on the related button that can be found underneath the comments section of the page.
    4. If the user selects "rate or comment", he/she will be redirected to a new page that has a collapsible "rate or comment" elements. User then needs to select the action he wish to undertake and submit it, whether it is rating the spot or adding a comment about it. 
    5. If the user selects "edit location", he/she will be redirected to a new page that contain an editable form for each of the spot details. User can edit one or all of the features and save changes.
    6. If the user selects "remove", he/she will be redirected to a page which acts as a safe guard in case user clicked on the button by mistake. The user will be asked to tick a checkbox in order to acknowledge the deletion request and only then he/she will be able to remove the spot from the site.

6. User "J" wants to add a new location. The following steps needs to be conduct in that case:

    1. Navigate to the "Add Spot" page where user is provided with a two step process of creating new location.
    2. First step require to input a location name in order to verify if it is not a duplication of already existing spot. 
    3. Step two contain a form with all of the location features that user can select from. All of the selection fields require user input beside facilities and hazards checkboxes.

7. Users "N" and "O" wants to track theirs interaction with the application by having their inputs stored on their personal page. Registered and logged users can access these pages by navigating to the nav bar at the top of the page on desktop and selecting their username that will be revealed once clicked on the "person" icon. Mobile version required users to click on the "hamburger" menu icon in order to access menu list where they will find their username. The personal page display all user interactions including list of created, edited, rated and commented locations.

8. Users "P" ,"Q" and "R" wants to see a data showing breakdown of locations per break type and bottom type, as well as the most popular facilities and most common hazards for all available locations. The data charts for each can be found by navigating to "about" page.

#### Manual Testing Bugs

I have not encountered any bugs with manual testing.

### Automated Testing

The automate testing was conduct using the following tools:

- Unit testing with Python

Unit test is a test which verify that a single component in the application operates in the right way. In order to verify test results, please run the following in your command line `python3 test_global.py`

- Jasmine framework with jasmine-jquery plugin

Jasmine is a behaviour-driven development framework for testing JavaScript code. There are 5 specs tested with no failures.

In order to run the Jasmine test please open the "specRunner.html" file in a browser. The test results will be displayed immediately. There is a known issue with new versions of Chrome which does not allow "file://URIs" to read other "file://URIs". This can be override by running Chrome with a switch "--allow-file-access-from-files". Works on other browsers without any problems.

- Chrome Lighthouse

The Lighthouse is an open-source automated tool that audits website for performance, accessibility, SEO and more. The website score was constantly satisfactory with recent results as follows:

```
- Performance at 78
- Progressive Web App at 50
- Accessibility at 91
- Best Practices at 80
- SEO at 89

highest score is 100
```

#### Automated Testing Bugs

I have not encountered any bugs with automated testing.

## Deployment

The application was deployed to [Heroku](https://www.heroku.com/home) with the following steps:

1. Installing Heroku CLI.
2. Creating a Heroku Account or Login into Heroku via command `heroku login`.
3. Initializing a git repository if not already created.
4. Create a heroku application with `heroku create your-first-heroku-app --buildpack heroku/python`.
5. Add the remote heroku git repository with `heroku git:remote -a your-first-heroku-app`.
6. Create requirements.txt file in your project root folder in order for heroku to detect it as a Python project with `sudo pip3 freeze --local > requirements.txt`.
7. Adding a Procfile with `echo web: python app.py > Procfile`.
8. Committing the files to Heroku’s repository master branch with `git add .` and `git commit -m "First commit for heroku"`. Push the changes from your local master branch to heroku’s master branch with `git push heroku master`.
9. Run the application with `heroku ps:scale web=1` (This is a command to the Heroku to tell it to get up and running).
10. The final step is to specify IP and PORT. Go to Heroku web app and from there go to `Settings > Config Variables` to specify our IP and PORT `IP = 0.0.0.0` and `PORT = 5000`.

## Credits

### Media

The photos used in the application were obtained from:

- [Unsplash](https://unsplash.com/) and the following authors - Thierry Meier, Jeremy Bishop, Tyler Nix and Jeremy Bishop.
- and [Magicseaweed](https://magicseaweed.com/).

### Content

The CSS Gradient was generated with [Colorzilla](http://www.colorzilla.com/gradient-editor/) online gradient editor.

### Acknowledgements

Dave Newson's [article](http://davenewson.com/posts/2013/conditional-aggregation-on-arrays-of-objects-in-mongodb.html) on conditional aggregation in MongoDB helped me understand it better.