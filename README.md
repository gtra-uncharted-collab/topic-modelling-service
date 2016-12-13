# topic-modelling-service
Python Flask wrapper for the topic modelling service

## Dependencies

- [Python](https://www.python.org) version 2.7
- [Flask](http://flask.pocoo.org/)

## Development

Clone the repository:

```bash
git clone git@github.com/gtra-uncharted-collab/topic-modelling-service.git
```

Install the dependencies.

## Execution

The simplest way to run it is to start flask.

In Windows:

```bash
set FLASK_APP=app.py
flask run
```

Other:

```bash
export FLASK_APP=app.py
flask run
```

Once running, doing a POST request to `localhost:5000/topics` will execute the code and return the results.