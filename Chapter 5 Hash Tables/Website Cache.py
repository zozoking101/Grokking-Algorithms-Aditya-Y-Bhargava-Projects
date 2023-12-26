import hashlib

cache = {}

def get_page(url):
    # Use SHA-256 as the hash function
    url_hash = hashlib.sha256(url.encode()).hexdigest()

    if url_hash in cache:
        return cache[url_hash]
    else:
        data = get_data_from_server(url)
        cache[url_hash] = data
        return data

# Example function to simulate getting data from a server
def get_data_from_server(url):
    # Simulated data retrieval from a server
    return f"Data for URL: {url}"

# Example usage
url_1 = "https://example.com/page1"
url_2 = "https://example.com/page2"

result_1 = get_page(url_1)
result_2 = get_page(url_2)

print(result_1)
print(result_2)
