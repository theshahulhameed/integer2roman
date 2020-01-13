# Integer to Roman numeral converter

Give an integer input (0 - 3999) to know the Roman numeral equivalent of the same. Includes a user-friendly web interface built using Python and Django. 

## Usage Instructions

1. To spin up the Docker with production settings, use this single command. 
`` docker-compose -f docker-compose-prod.yml up --build ``

2. Open your browser and visit `localhost:8000` or `127.0.0.1:8000` to try the same. 

To run test cases:
1. `docker-compose exec web python manage.py test`

### Credits
Used Bootstrap4 for styling purposes. Read more about [Roman Numeral System](https://en.wikipedia.org/wiki/Roman_numerals)
