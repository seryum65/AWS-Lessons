#!/bin/bash

read -p "Input your name: " name
read -sp "Input your password: " password

if [[ $name != $(whoami) ]] && [[ $password != Aa1234 ]]
then
    echo -e "\nIt is wrong account"
elif [[ $name != $(whoami) ]]
then
    echo -e "\nYour name is wrong"
elif [[ $password != Aa1234 ]]
then
    echo -e "\nYour password is wrong"

elif [[ $name = $(whoami) ]] && [[ $password = Aa1234 ]]
then
    echo -e "\nWelcome $(whoami)"
    
fi
