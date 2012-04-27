def get_penn_locations():
    """Return a list of popular UPenn locations."""
    locations = []
    with open('locations.txt', 'rU') as f:
        for line in f:
            location = {}
            parts = line.strip().split('?')
            name = parts[0].strip()
            address = parts[1].strip()
            location['name'] = name
            location['address'] = address
            locations.append(location) 
    return locations

if __name__ == '__main__':
    print load_locations()
