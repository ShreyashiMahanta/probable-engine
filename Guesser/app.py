words = [
    {
        "inputs": 9,
        "category": "Team Sports",
        "word": "Football"
    },
    {
        "inputs": 8,
        "category": "Capital of a Central European Country",
        "word": "Budapest"
    },

    {
        "inputs": 7,
        "category": "Oldest programming language",
        "word": "Fortran"
    },

]



from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)
