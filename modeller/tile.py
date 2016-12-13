
class TileTopicModeller():
    
    def __init__(self):
        pass

    def model_topics(self, terms, tiles):
        #Call the topic modelling system.
        #For now, create a fake result that matches the spec.
        result = {
            "tile": {"x": 5, "y": 4, "level": 12},
            "topic": [{
                "score": 4.315,
                "words": [
                    {"score": 1.23, "word": "food"},
                    {"score": 0.9855, "word": "burger"},
                    {"score": 0.72735, "word": "fries"},
                    {"score": 0.71, "word": "drinks"}
                ]
            }]
        }
        return result