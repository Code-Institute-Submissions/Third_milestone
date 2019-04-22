# Test vs PROD

<u>change the IP to local in MongoDB once live & Turn OFF DEBUG in production</u>

# Surfingeurope

The [surfingeurope](https://surfingeurope.herokuapp.com/) is a Data Centric Development Milestone Project build for [Code Institute's](https://www.codeinstitute.net/) Full Stack Web Developer Course.

The Surfingeurope website is a surfing locations guide that allows surfers to expolore various types of spots in Europe. The site has a social aspect by allowing users to add new locations, edit current spots and rate or comment on the existing ones based on their personal experience and knowledge.

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
- As a user R, I want to see some data showing the most popular facilities for all of the locations.
- As a user S, I want to see some data showing the most common hazards for all of the locations.

### Scope

The Surfingeurope website should focus on user engagement by allowing users to create new locations and to edit existing spots in order to correct incorrect data. The users should be able as well to rate and comment on the spots to help other fellow surfers in making their future surf travel choices. In order to help in making that decision, each of the surfing locations should have spot features including but not limited to break type, bottom type, wind direction, type of available facilities and occuring hazards. These features together with location description would allow surfers to find at least one spot that is matching their surfing style and abilities.

### Structure

Based on the strategy and scope, the website structure should have clearly organized content and should allow an intuitive interaction for the users. The website should lack any clutter and be informative as much as possible at the same time. There shouldn't be any distractions to the users and the focus should be placed on providing the surfing location features and to stimulate users to interact with the site. 

### Skeleton

The following wireframes were created to determine the visual form and arrangment of the application elements:

- <a href="mockups/Small_device.png" target="_blank">Small device.</a>
- <a href="mockups/Medium_device.png" target="_blank">Medium device.</a>
- <a href="mockups/Large_device.png" target="_blank">Large device.</a>

### Surface

Once the wireframes were in place, the following visuals were introduced:

- The base colors for the site are green and blue with its different shades and white as the main background color. These colors were selected to match with the surfing theme i.e. colors of the ocean.
- Typography is limited to three Google typefaces with "Roboto" being the default one. It's a clean and modern sans serif typeface makes the site readable on both small and large devices. The other two are "Kaushan Script" and "Oswald". The first one was used as a base for Surfingeurope logotype and occasionally on the website to give the content some vibrant feel. The later, being a reworking of the classic gothic typeface style is used to put an emphasis on text content due to its better fit to the pixel grid of a standard digital screens.
- The website logotype and its shorcut are custom made making the site more stylish and memorable.
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

The landing page consists of a large image with a button that leads users to page listning all of the locations and a welcome text. The remaining content consists of three top rated locations cards promoting the best spots in Europe and three randomly selected locations allowing users to explore some other spots.

### All Locations Page

There are two main elements of that page. The top element allow users to sort the list of locations by name being the default view, country and rating. There is a search button underneath the filters that allows quick transition to the search page for a more tailored results.

The bottom element display list of locations cards based on the selected filter. The amount of location cards is limited to 6 per page to avoid clutter and intensive scrolling. At the bottom of the list, there is a pagination range displed making navigation between spots quick and easy.

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

The user has freedom to specify only the options that he believe are necessery for his query. If there are no results matching either of the searches, the user will be redirected to error page and notified about lack of results.

### Add or Edit Location

The main concept of the application is to engage users to share their local knowledge by adding new spots to the site. In order to add a new location user needs to provide a unique spot name. Once the name is validated in order to ensure no duplications are created, the user is provided with a form containing all of the spot features. The user is again required to fill all the fields beside facilities and hazards, which can remain unchecked if none of the options match the spot characteristics. Once all data is provided user is able to add new location to the site.

Similar appraoch exists for the ability to edit existing location. The user is provided with all existing details of the spot but is given choice to change only the features he/she wants to overwrite, add or remove.

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

- Password imput requirements to be added.
- Pagination to have limit of displayed page numbers with hidden excess of pages beyond the limit.
- Add Google Map API to show locations on the map.
- Add a image gallery for each location.
- Prevent showing a spot in the random locations display if the spot is already display on the page.
- Provide users with list of similar locations that match their preference based on the user ratings of other spots.


## Technologies Used




# Credits

Photo by Thierry Meier on Unsplash (hero_main.jpg)
Photo by Cristian Palmer on Unsplash (footer.jpg)
[article on conditional aggregation](http://davenewson.com/posts/2013/conditional-aggregation-on-arrays-of-objects-in-mongodb.html)
Photo by Jeremy Bishop on Unsplash (background image for loc if no img provided)
(gradient)[http://www.colorzilla.com/gradient-editor/]
Photo by Jeremy Bishop on Unsplash (error)
Photo by Tyler Nix (campervan)