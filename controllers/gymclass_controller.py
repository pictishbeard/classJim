from flask import Blueprint, Flask, redirect, render_template, request

from models.gymclass import gymClass
import gymclass_repository as gymclass_repository