"""
The class is defined in purpose of the shopping cart system
"""

class Product:
    """"Defined as the base class for products in the store"""
    
    def __init__(self, productid, price):
        """
        Initiating product
        
        Args: 
            productid (str): unique identifier for the product
            price (float/double): price in euros
        """
        self.id=productid
        self.price=price
        
    def get_product_weight(self):
        """
        function: retrieve weight of the selected product
        
        return: product weight in kilogrms
        
        """
        
        raise NotImplementedError("require implementing subclass get_weight()")
    
    
class Book(Product):
    def __init__(self, productid,title, author, num_pages, price,weight):
        """
        Initialize book record
        
        Args: 
            product_id (str): Unique identifier
            title (str): Book title
            author (str): Author name
            num_pages (int): Number of pages
            price (float): Price in euros
            weight (float): Weight in kilograms
        """
        super().__init__(productid, price)
        self.title=title
        self.author = author
        self.num_pages = num_pages
        self.weight = weight

    def get_weight(self):
        """retrieve the weight of the book"""
        return self.weight
    
    def __str__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', price=€{self.price:.2f})"
    
    

class MusicAlbum(Product):
    """Inititalize a class for music album"""
    
    def __init__(self, productid,artist,title,num_tracks,price,weight):
        """
        Initialize a music album.
        
        Args:
            product_id (str): Unique identifier
            artist (str): Artist name
            title (str): Album title
            num_tracks (int): Number of tracks
            price (float): Price in euros
            weight (float): Weight in kilograms
        
        """
        super().__init__(productid, price)
        self.artist = artist
        self.title = title
        self.num_tracks = num_tracks
        self.weight = weight
        
    def get_weight(self):
        """retrieve the weight of the music album"""
        return self.weight
    
    def __str__(self):
        return f"MusicAlbum(id={self.id}, artist='{self.artist}', title='{self.title}', price=€{self.price:.2f})"
    
class SoftwareLicense(Product):
    """Class to initalize software license"""
    def __init__(self, productid, name,price):
        
        """
        Args:
            product_id (str): Unique identifier
            name (str): Name of the software
            price (float): Price in euros
        """
        super().__init__(productid, price)
        self.name = name
        
    def get_weight(self):
        """
        retrieve the weight of the softwarelicense
        Note: As software license does not have any weight we will return 0.0
        """
        return 0.0
    
    def __str__(self):
        return f"SoftwareLicense(id={self.id}, name='{self.name}', price=€{self.price:.2f})"