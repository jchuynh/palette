
<h1 align="center">
  <a href="https://github.com/jchuynh/color-palette-demo">
    <img alt="Palette" src="https://github.com/jchuynh/palette/blob/master/static/app_images/palette-dashed-circle.png" width="50%">
  </a>
  <br>[Palette](http://palette.jessicahuynh.com/index)<br>
</h1>


Palette is an application that provides users with color inspiration with famous works of art. You are able to create your own color palette based on one of Vincent van Gogh's paintings. If you have been fully inspired and would like to use a photo or image you have, feel free to upload it and receive the color palette.

## About Me
Before beginning her new career as a software engineer at Hackbright Academy, Jessica was in the biotechnology field as an engineering process technician. She started out working in the lab to complete daily experiments and following up with detailed reports on her findings. Her responsibilities shifted and she began overlooking other technicians by training them, coordinating experiments and projects, analyzing their reports and providing milestones.

## Contents
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Future State](#future)
* [Installation](#installation)

## <a name="tech-stack"></a>Technologies
* Python
* Flask
* Jinja2
* PostgresQL
* SQLAlchemy ORM
* HTML
* CSS
* Bootstrap
* jQuery
* Python Imaging Library
* Haishoku Tool
* Select2
* Werkzeug-Utlities

## <a name="features"></a>Features

### Welcome to The Gallery 
Visitors are able to see the full set of artworks available in a gallery view. When one artwork catches their eye, they can click on the image to receive more detailed information. 

### It's all in the details
The visitors are directed to artwork's details. The left contains text information on the art piece, set to the right. 

#### Tags
Tags are located under the artist's name. When selecting the tags, the visitor will be redirected to another 'mini' gallery with all the artworks that have the same tag. This allows the visitor to view similar artworks based on a tag description.

![Exploring with Tags](/static/gifs/tags.gif)

#### Color Palette
There are five visible color swatches of the color palette. The visitor can also select the "More Colors" button, to view the 3 more swatches. By keeping some the colors hidden, the visitor will have time to view the dominant colors and see where in the artwork is that color. 

#### Recently Viewed
With all the available artworks that the visitor viewed, the "Recently Viewed" button allows the visitor to backtrack and choose an artwork to see again. 

### Search Page
Visitors can search the gallery by artist, a tag description, and the title of an artwork. The information will be populated based on the visitor's search term. 

![Searching for artwork](/static/gifs/search.gif)

### Upload Page: Be your own inspiration
When a visitor is feeling inspired, they can upload their own image. The uploaded image will be processed in the same way as the artworks and will provide the full eight color swatches.

![Uploading Images](/static/gifs/upload.gif)


## <a name="future"></a>Future Features
Palette has some features that would continue to help provide the information:
* Increase the artwork database to include more museums.
* Creating a user login to save color swatches and/or palettes of your choice.
* Increase search box queries to include year and type of artwork.
* Making the web app a responsive site.
* Further deconstructing painting to show only outlines of brushstrokes.
* Save users' uploads to a cloud service
* Deploy website 

