
from __future__ import absolute_import, division, print_function, unicode_literals
# import paypalrestsdk
import logging
import cv2 
# import tensorflow as tf
# tf.enable_eager_execution()
# import mysql.connector

import os
import shutil
import tensorflow as tf
import tensorflow_hub as hub

# Load compressed models from tensorflow_hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'

import IPython.display as display

# import functools

# from tensorflow import keras 
# from tensorflow.keras.layers import Input, Reshape, Dropout, Dense, Flatten, BatchNormalization, Activation, ZeroPadding2D
# from tensorflow.keras.layers import LeakyReLU
# from tensorflow.keras.layers import UpSampling2D, Conv2D
# from tensorflow.keras.models import Sequential, Model, load_model
# from tensorflow.keras.optimizers import Adam

import os 
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import timeit
import requests
# from tqdm import tqdm

import time
import base64
import io
import os 
import numpy as np 
import PIL
from PIL import Image
from PIL import ImageEnhance

import smtplib
from email.message import EmailMessage

from flask import request
from flask import jsonify, make_response
from flask import Flask, url_for, flash  
from flask import render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_user, current_user, logout_user, login_required 
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message

import image_slicer
import uuid
import glob

# import torch
# import torchvision
# from torch.utils.serialization import load_lua
    

# from Dataloader import data_loader
# import Models
# import Utils



# from model.srgan import generator
# from model.edsr import edsr

# from model import resolve_single

# load_image, plot_sample,plot_sample2,plot_sample3,plot_sample4,
# plot_sample5,plot_sample6,plot_sample7,plot_sample8,plot_sample10,
# plot_sample11,plot_sample12,plot_sample13,plot_sample14,
# plot_sample15,plot_sample16,plot_sample17,plot_sample18,plot_sample19,plot_sample20,