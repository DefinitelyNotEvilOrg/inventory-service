def normalize_metadata(metadata):
    normalized = {}

    for key, value in metadata.items():
        normalized[key.lower()] = value

    return normalized
