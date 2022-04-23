# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:54:32 2022

@author: Jnino129
"""

#Modulo 1 - construcion de la cadena de bloques 
#importar librerias
import datetime
import hashlib
import json
from flask import Flask, jsonify

#Parte 1 -  Creación de la cadena de bloques
class Blockchain:
    
    #creacion de un nuevo bloque teniendo en cuenta el bloque genesis
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = "0")
    
    #informacion primordial del bloque
    def create_block(self, proof, previous_hash):
        block = {"index" : len(self.chain)+1, 
                 "timestamp" : str(datetime.datetime.now()),
                 "proof" : proof,
                 "previous_hash" : previous_hash
                 }
        self.chain.append(block)
        return block
        
    #para obtener el hash del bloque previo
    def get_previous_block(self):
        return self.chain[-1] 
    
    #Creacion de la funcion proof of work 
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encod()).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    
        
        
        
    
        
#Parte 2 - Minado de un Bloque de la Cadena
        