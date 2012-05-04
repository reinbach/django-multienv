django-multienv
===============

Sample Django app that handles multiple envs/databases with same model

The idea is to develop a sort of devops application that can then access the relevant data in Dev, QA and/or Production. The expectation is that the data you are dealing with is relevantly stable between these environments. So you can manage the data in these various environments from a single source/code base.

The objective is to have a selector that can switch between the database instances.


Example
-------

The sample application is made up as follows;

Profile App: 
Handles the user profile and database access limited to single database instance. So all queries will always be against this database instance.

Orders App:
Able to manage order information across the various environments. User makes a selection as to which environment they would like to work in. Thereafter all queries are directed at that database instance until changed.


Install and Run
---------------

The following should get you up and running;

    python setup.py install
    cd multienv
    python manage.py syncdb

The following extra database instances will need to be created;

    1. multienv_dev
    2. multienv_qa
    3. multienv_prod

Need to setup/create the necessary tables in the extra database instances;

    psql -U <db_user> multienv_dev < sample.sql
    psql -U <db_user> multienv_qa < sample.sql
    psql -U <db_user> multienv_prod < sample.sql