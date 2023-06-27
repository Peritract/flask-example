# Building Servers

### Terminology

- Client - a role that requests
- Server - a role that responds/listens
- API - Application Programming Interface (how the server interacts with clients)
- Interface - a connection point / how things communicate
- Endpoint - a location on an API
- Request - asking for something
- Response - a reply to a request
- Method - a collection of steps / a way of doing something

## Running Flask

- `app.run()` inside the script
- `flask run` if the script is called app.py
- `flask --app [filename] run` if the script is called something else
- `export` various bits of information to the terminal and `flask run`

## Documentation

Documentation is absolutely vital.

| Route | Method | Response | Parameters
| --- | --- | --- | --- |
| `/` | `GET` | A nice message | | 
| `/company` | `GET` | A list of company information | `country` - filter by location |
| `/company` | `POST`| Create a new company based on JSON data | |