import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search.tree import java_tree

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def home():
  return "Hello World"


@app.route("/java/ast", methods=["POST"])
def get_java_ast():
  java_code = request.form["code"]
  ret_obj = {}
  try:
    code_ast = java_tree.parse_content(java_code)
    ret_obj = {
      "status": 200,
      "ast": code_ast
    }
  except Exception as e:
    print(e)
    ret_obj = {
      "status": 500,
      "error_msg": e.message
    }
  return jsonify(ret_obj)


if __name__ == "__main__":
  app.run(port=5000)
