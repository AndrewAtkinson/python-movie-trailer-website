import time
import webbrowser

class Movie:

    
    """Movie class that stores information about a movie

    Attributes:
        title: A String containing the title of the movie.
        description: A String containing the description of the movie.
        poster_image_url: A String containing a link to the image of movies poster.
        trailer_youtube_url: A string containing the URL for the movies trailer
    """

    
    def __init__(self, title, description, image_name, youtube_id, release_date=""):
        """Intiallises a new movie object and assigns the data to the movie object"""
        self.title = title
        self.description = description
        self.poster_image_url = image_name
        self.trailer_youtube_url = self.get_movie_url(youtube_id)
        self.trailer_youtube_url = self.get_movie_url(youtube_id)
        self.release_date = self.format_date(release_date)


    def play_trailer(self):

        
        """Opens a web browser to the movies trailer url"""
        webbrowser.open(self.trailer_youtube_url)


    def get_movie_url(self, youtube_id):

        
        """Generates a full YouTube URL from the video id
        Args:
            youtube_id: The id of the youtube video to build the URL for.
            
        Return:
               A full YouTube URL
        """

        
        return 'http://www.youtube.com/watch?v=' + youtube_id


    def format_date(self, date):


        """Formats a date into the format we want
            Args:
                date: date string "%d/%m/%Y".
            
        Return:
               A date string with format %A %d %B %Y
        """
         
 
        date_formatted = "To Be Announced"

        if date != "":
            date_formatted = time.strptime(date, "%d/%m/%Y")
            date_formatted = time.strftime("%A %d %B %Y", date_formatted)            

        return date_formatted

    
