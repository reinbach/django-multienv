django-multienv
===============

Sample Django app that handles multiple envs/databases with same model

The idea is to develop a sort of devops application that can then access the relevant data in Dev, QA and/or Production. The expectation is that the data you are dealing with is relevantly stable between these environments. So you can manage the data in these various environments from a single source/code base.

The objective is to have a selector that can switch between the database instances.