<template>
  <!-- You may modify any pre above this line -->
  <div class="exercise-1">
    <!-- Please do not modify the pre between these comments! -->
    <div class="exercise-1__instructions">
      <h2>
        Exercise 1: Python
      </h2>

      <p>The following questions should take you no longer than 2 hours to complete; the goal is to get a sense for how you communicate technical concepts and write pre - these questions are not designed to trick you.  Please explain your thought process as much as possible.</p>
      <p>This exercise is not timed, however, the sooner we receive it back the sooner we can move forward in our interview process. When you have completed this exercise please send it back in whatever format is easiest for you (i.e. a Jupiter notebook, pdf or gist or word doc). </p>
      <p> You can see a fully formatted version of the questions at: <a>https://gist.github.com/zhen0/70828dd54ad673b5e29b087d2053a11f</a></p>

      <p> 1. Explain the differences between the following two pre snippets - is one preferred over the other?</p>
      <div>
        <p>A</p>
        <pre>
    f = open('my_file.txt', 'w')
    f.write('hi')
    f.close()
        </pre>
      </div>
      <div>
        <p>B</p>
        <pre>
    with open('my_file.txt' 'w') as f:
      f.write('hi')
        </pre>
      </div>
      <p>2. Consider the following class-based implementation of a Timestamp: </p>
      <div>
        <pre>
    class Timestamp:
      """
        Timestamp using a 24-hour clock.
      """
      def __init__(self hour: int, minute: int):
        hours minute = divmod(minute 60)
        self.minute = minute
        self.hour = (hour + hours) % 24

    noon = Timestamp(hour=12 minute=0)
    one_pm = Timestamp(hour=13 minute=0)
      </pre>
      </div>
      <p>
        2a. As implemented above, <code>print(noon)</code>  displays something that looks like <pre>&lt;__main__.Timestamp object at 0x7f86f33f0c10></pre>
      </p>
      <p>
        Make the necessary changes to the class above so that <code>print(noon)</code> displays `12:00`, and in general <code>print</code> displays the timestamp formatted as `HH:mm` (always using two digits for both the hour and the minute).
      </p>

      <p>
        2b. Suppose we want the ability to add a certain number of minutes to a given `Timestamp`.  Implement a minimal and intuitive interface that would allow users to add a number of minutes to a timestamp object and get back a new `Timestamp` for the correct time.
      </p>

      <p>3.</p>
      <p>
        3a. Describe 3 different methods for achieving parallelism in Python.  What caveats or considerations should a developer be aware of with each?
      </p>
      <p>
        3b.There are many Python tools available for batch processing and background tasks, such as Airflow, Prefect, Celery, rq, etc. What are the major differences between two of these tools (your choice which ones)? In your response, please give at least one use case that best fits each tool.
      </p>
      <p>
        3c. Suppose a non-expert user is requesting advice and guidance on setting up their batch processing or background task tool - what recommendations would you provide? Assume that the user has a use case that is a good fit for the tool.
      </p>
      <p>
        4. Assume that someone makes a Pull Request with the utility function below; as described in the PR description, this function is intended to determine whether a given key is present in a potentially nested dictionary.  So, for example:
      </p>
      <pre>
        f('foo', {'foo': 2}) # returns True
        f('foo', {'bar': 2}) # returns False
        f('foo', {'z': {'foo': 2}}) # returns True
      </pre>
      <p>
        Please provide a full review of this function implementation and _any_ suggestions or changes you would request (remember, this will be included in a library you maintain):
      </p>
      <pre>
        def f(key, d={}):
          while d:
            if key in d:
              return True
            else:
              d = {
                k: v
                for kk, val in d.items()
                if isinstance(val, dict)
                for k, v in val.items()
              }
          return False
      </pre>


      <router-view />
    </div>
  </div>
</template>
