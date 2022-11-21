*** Settings ***
Documentation       Template robot main suite.

Library             Collections
Library             MyLibrary
Resource            keywords.robot
Resource            Subflow.robot
Variables           variables.py


*** Tasks ***
Example task
    Portal Launching