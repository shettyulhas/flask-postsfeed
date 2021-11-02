# Figure 1 Backend Feed Challenge

## Overview

Build a simplified 'Figure 1' backend to serve a feed of cases.

A skeleton has been provided in this repository that can be used as a starting point for your solution.  You can use any frameworks, libraries or templates.

We suggest to keep the time spent on this test within 1 hour.


## Requirements

1. Add an endpoint or script to seed the database with cases.  The case data to use has been provided in `data/feed.json`.
1. Add an endpoint that returns a feed of these cases.
1. Pick 1-2 additional improvements from the following list:
    1. Create an alembic migration setup
    1. Add support for tests and add tests for the feed logic
    1. Add pagination support to the get feed endpoint
    1. Introduce a celery configuration
    1. Productionize your backend


## Things to keep in mind

Code quality is more important than features.  Your code will be evaluated based on:
1. Code Structure
1. Best Practices
1. Readability
1. Maintainability

In addition, please consider the following questions as you develop your solution.  These may be discussed more in a later interview.
 - How would you improve the implementation if given more time?
 - Do you think your approach scales well? Where do you think the first failure point would be?
 - Would adding another similar feature take the same amount of time?


# Running the API

This is a simple flask app using sqlite and sqlalchemy. When it is run, it will create a database file if one does not already exist called app.db.

There are some things that are intentionally left out for the sake of simplicity.
* Sqlite is used for ease of setup, it is clearly not a good production database
* Migrations are not used
