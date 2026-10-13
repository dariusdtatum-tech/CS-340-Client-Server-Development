# CS-340 Client/Server Development

**Darius Tatum** · Southern New Hampshire University

A full-stack project for Grazioso Salvare, a search-and-rescue dog training company. Project One is a Python CRUD module for a MongoDB database of Austin Animal Center shelter outcomes. Project Two is a Dash web dashboard that uses that module to filter the data by rescue type and show the results in an interactive table, a breed pie chart, and a map.

## Files

| File | What it is |
|---|---|
| `CRUD_Python_Module.py` | Project One. The `AnimalShelter` class with create, read, update, and delete methods for the `aac.animals` collection. |
| `ProjectTwoDashboard.ipynb` | Project Two. The Grazioso Salvare dashboard. |
| `Project_One_README.docx` | Project One documentation. |
| `Project_Two_README.docx` | Project Two documentation, with screenshots of every filter. |

## Reflection

**How do I write programs that are maintainable, readable, and adaptable?**
I keep the database code in one place. The `AnimalShelter` class from Project One is the only code that talks to MongoDB. Each method does one job and returns something simple: a true or false, a list, or a count. The dashboard in Project Two never builds its own connection. It imports the class and calls `read()` with a query. When the login needed `authSource='admin'`, I fixed it once in the class and every notebook picked up the fix. Because the class has no dashboard logic in it, I could reuse it for a report script, a scheduled data cleanup, or a different front end without changing it.

**How do I approach a problem as a computer scientist?**
I start with the client's actual rules and turn them into something I can test. Grazioso Salvare gave a table of breeds, sex, and age ranges for each rescue type. I wrote each row as a MongoDB query and checked the results by hand before wiring them to buttons. For example, a 209-week dog showed up under Disaster but not under Mountain, which confirmed the age ranges were different. This project differed from earlier courses because the work was split into layers: the database, the module, and the dashboard. Each layer had to be working before the next one could be built. For future clients, I would start the same way: get the requirements into a table, build and test the data layer first, and keep the user interface separate.

**What do computer scientists do, and why does it matter?**
Computer scientists turn messy information into tools people can use to make decisions. Grazioso Salvare had thousands of shelter records but no fast way to find the few dogs worth training. This dashboard lets a trainer click one button and see the matching dogs, where they are, and what breeds they are. That saves staff time and helps them find good candidates sooner, which means more trained rescue dogs in the field.

## Built with

- [MongoDB](https://www.mongodb.com/) and [PyMongo](https://pymongo.readthedocs.io/)
- [Dash](https://dash.plotly.com/), [Plotly](https://plotly.com/python/), and [Dash Leaflet](https://dash-leaflet-docs.onrender.com/)
- [pandas](https://pandas.pydata.org/)
