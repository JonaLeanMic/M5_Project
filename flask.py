# #from flask import Flask, render_template, request, redirect, flash, jsonify, make_response
# from flask import redirect
# from flask_classful import FlaskView, route
# import flask
#
# class Flask:
#     def __init__(self):
#
#         global counter
#         counter = 0
#
#         app = Flask(_name_)
#
#         class TestView(FlaskView):
#             @route("/")
#             def index(self):
#                 global counter
#
#                 return "<a href=\"lol\">" + str(counter) + "<//a>"
#
#             @route("/lol")
#             def lol(self):
#                 print("Hallo")
#                 global counter
#                 counter = counter + 1
#                 print(counter)
#                 return redirect("/")
#
#         TestView.register(app, route_base='/')
#
#         app.run(host='0.0.0.0', port=9000, debug=False)