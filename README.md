# Song-Randomizer
## Base Idea
A website where users can add a song to a site-wide communal playlist, which will then deliver a song at random to a user on request.

## Structure
Front End: HTML/CSS, JavaScript<br>
Back End: Python/Flask, mySQL<br>
APIs Needed: Spotify Web API

The site will consist of a single page. There will be two main points of interaction. First, there will be a button for a user to search for and add a song of their choosing to the site's communal playlist, which will be handled by calls to the Spotify Web API. Second, there will be a button for a user to recieve a snippet of a random song from the playlist, also handled by calls to the Spotify Web API. 

To keep track of and manage the playlist, a simple database will be created to store the information pulled from the Spotify Web API calls. The stored information will include song name, artist name, album name, and year. The database will also store the full url pointing to the song.

The primary functionality of the website will be achieved through the Search functions provided by the Spotify Web API. This will allow songs to be chosen and found by both the user and the database to be processed.

## To Do
Front End
- [ ] Create basic outline for page using HTML/CSS. Add dynamic content through JavaScript/Flask.

Back End
- [ ] Link database to website, allow addition and selection operations.
- [ ] Decide on using PHP for direct database access, or running through Flask library.
- [ ] Create overall app structure through Flask following good practice.

Database
- [ ] Design and create databse to store selected songs.
- [ ] Decide on attributes and data types for each.
- [ ] Prevent malformed or malicious inputs from user.
