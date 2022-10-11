{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "78dbbd7e-c575-454c-aa3f-a65af37fccf7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4cc8aee6-12e8-49c4-b67e-5cc975a8d1cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8fc2f728-2629-4a6b-8746-0e5e793d085c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0e85ed3e-1205-4bb7-93bc-f34c9d60f927",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set Up the Database\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")\n",
    "\n",
    "#THIS LINE OF CODE ALLOWS ME TO ACCESS THE SQLITE DATABASE SO THAT WE CAN QUERY OUR FILE."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e5024f72-04d7-49e2-84b2-10f0a7d2fc0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# NOW ITS TIME TO REFLECT/COPY OUR DATABASE INTO CLASSES\n",
    "Base = automap_base()\n",
    "# THIS LINE OF CODE REFLECTS THE DATABASE\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ec7bc7e3-6f55-4d96-b6cd-50d965886493",
   "metadata": {},
   "outputs": [],
   "source": [
    "#With the database reflected, we can save our references to each table. Again, they'll be the same references as the ones we wrote earlier \n",
    "#in this module. We'll create a variable for each of the classes so that we can reference them later, as shown below.\n",
    "\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ac3bc05a-943e-473a-b210-06060c67c247",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Finally, create a session link from Python to our database with the following code:\n",
    "\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5bcd2b71-2b25-49d1-814d-b22cfaaff648",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Next, we need to define our app for our Flask application.\n",
    "\n",
    "\n",
    "#app = Flask(\"__name__\")\n",
    "\n",
    "#This will create a Flask application called \"app.\"\n",
    "\n",
    "#NOTE: IF CODE FAILS, ADD \"\" INSIDE THE PARANTHESES.  THIS FIXED MY ERROR EARILIER IN THE MODULE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3c9bbbaa-2882-40b5-8d02-22ec4834ccba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Our first task when creating a Flask route is to define what our route will be. We want our welcome route to be the root,\n",
    "#which in our case is essentially the homepage.\n",
    "\n",
    "#We can define the welcome route using the code below:\n",
    "\n",
    "app = Flask(\"__name__\")\n",
    "\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return(\n",
    "    '''\n",
    "    Welcome to the Climate Analysis API!\n",
    "    Available Routes:\n",
    "    /api/v1.0/precipitation\n",
    "    /api/v1.0/stations\n",
    "    /api/v1.0/tobs\n",
    "    /api/v1.0/temp/start/end\n",
    "    ''')\n",
    "\n",
    "\n",
    "\n",
    "#Now our root, or welcome route, is set up. The next step is to add the routing information for each of the other routes. \n",
    "#or this we'll create a function, and our return statement will have f-strings as a reference to all of the other routes. \n",
    "#This will ensure our investors know where to go to view the results of our data.\n",
    "\n",
    "#First, create a function welcome() with a return statement. Add this line to your code:\n",
    "\n",
    "#Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement.\n",
    "#We'll use f-strings to display them for our investors: THIS IS ALL THE CODE IN RED AFTER THE RETURN STATEMENT\n",
    "\n",
    "#THIS CODE IS MEANT TO RUN ON VSCODE. JUPYTER LAB DOESNT WORK WHEN USING FLASK"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11527f6e-23e1-4fce-8fd0-e65558da0a36",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
