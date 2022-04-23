# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:54:32 2022

@author: Jnino129
"""

#Modulo 1 - construcion de la cadena de bloques 
import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = "0")
        