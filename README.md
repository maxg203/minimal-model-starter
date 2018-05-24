# minimal-model-starter
This is a minimal Flask app (so written in Python) that literally just has a function in an `algorithm.py` file where you can swap in any model you like and deploy this to production with minimal effort. This is perfect if you want to leverage the powerful data science tools available in the Python open source community and/or have been testing your model in a Jupyter notebook or similar and now someone actually needs to use what you've made within your business.

When you make a request to run your model, a task is dispatched asynchronously (as it is expected that your model will take a non-trivial amount of time to run) and your model is evaluated. You can get the result(s) return by that job by making another request.
