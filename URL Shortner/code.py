import hashlib
import base64

# Dictionary to store the mappings between short and original URLs
url_mapping = {}

def shorten_url(long_url):
    # Generate a unique hash for the long URL
    hash_object = hashlib.sha1(long_url.encode())
    hex_digest = hash_object.hexdigest()
    
    # Take the first 8 characters of the hash as the short URL
    short_url = hex_digest[:8]
    
    # Store the mapping between short and long URLs
    url_mapping[short_url] = long_url
    
    return short_url

def expand_url(short_url):
    # Retrieve the original long URL from the mapping
    return url_mapping.get(short_url, None)

# Example usage
if __name__ == "__main__":
    long_url = "https://www.example.com"
    short_url = shorten_url(long_url)
    print("Short URL:", short_url)
    original_url = expand_url(short_url)
    print("Original URL:", original_url)

