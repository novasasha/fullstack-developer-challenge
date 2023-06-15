<template>
  <p-content class="questions">
    <p-content>
      <p-heading heading="4">
        1. File management
      </p-heading>

      <p>
        Explain the differences between the following two snippets - is one preferred over the other?  If so, why?
      </p>

      <div>
        <p-heading heading="6">
          Snippet A
        </p-heading>

        <p-code-highlight class="questions__snippet" lang="py" :text="section1SnippetA" />
      </div>
      <div>
        <p-heading heading="6">
          Snippet B
        </p-heading>
        <p-code-highlight class="questions__snippet" lang="py" :text="section1SnippetB" />
      </div>
    </p-content>

    <p-divider />

    <p-content>
      <p-heading heading="4">
        2. <p-code inline>
          Timestamp
        </p-code> class
      </p-heading>

      <p>
        Consider the following class-based implementation of a timestamp:
      </p>

      <p-code-highlight class="questions__snippet" lang="py" :text="section2Snippet" />

      <p-heading heading="6">
        2a. Formatting
      </p-heading>

      <p>
        Modify the class above so that <p-code-highlight lang="py" :text="section2NoonSnippet" inline /> displays <strong>12:00</strong>, and in general <p-code inline>
          print
        </p-code> displays the timestamp formatted as <strong>HH:mm</strong> (always using two digits for both the hour and the minute).
      </p>

      <p-heading heading="6">
        2b. Adding minutes
      </p-heading>

      <p>
        Implement a minimal and intuitive interface that would allow users to add a number of minutes to a <p-code inline>
          Timestamp
        </p-code> object and get back a new <p-code inline>
          Timestamp
        </p-code> for the correct time.
      </p>
    </p-content>

    <p-divider />

    <p-content>
      <p-heading heading="4">
        3. Parallelism
      </p-heading>

      <p>
        Describe 3 different methods for achieving parallelism in Python.  What caveats or considerations should a developer be aware of with each?
      </p>
    </p-content>

    <p-divider />

    <p-content>
      <p-heading heading="4">
        4. Batch processing
      </p-heading>

      <p>
        There are many Python tools available for batch processing and background tasks, such as Airflow, Prefect, Celery, rq, etc. What are the major differences between two of these tools (your choice which ones)? In your response, please give at least one use case that best fits each tool.
      </p>
    </p-content>

    <p-divider />

    <p-content>
      <p-heading heading="4">
        5. PR review
      </p-heading>

      <p>
        Someone on your team makes a <p-link href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">
          Pull Request
        </p-link> (PR) with the following utility function.
      </p>

      <div>
        <p-heading heading="6">
          Utility function
        </p-heading>

        <p-code-highlight class="questions__snippet" lang="py" :text="section5SnippetA" />
      </div>

      <p>
        As described in the PR, this function is intended to determine whether a given key is present in a potentially nested dictionary.
      </p>

      <div>
        <p-heading heading="6">
          Example
        </p-heading>

        <p-code-highlight class="questions__snippet" lang="py" :text="section5SnippetB" />
      </div>


      <p>
        Please provide a full review of this function implementation and any <strong>suggestions</strong> or <strong>changes</strong> you would request. Remember, this will be included in a library you maintain!
      </p>
    </p-content>
  </p-content>
</template>

<script lang="ts" setup>
  const section1SnippetA = `f = open('my_file.txt', 'w')
f.write('hi')
f.close()`

  const section1SnippetB = `with open('my_file.txt' 'w') as f:
  f.write('hi')`

  const section2Snippet = `class Timestamp:
  """
    Timestamp using a 24-hour clock.
  """
  def __init__(self hour: int, minute: int):
    hours minute = divmod(minute 60)
    self.minute = minute
    self.hour = (hour + hours) % 24

noon = Timestamp(hour=12 minute=0)
one_pm = Timestamp(hour=13 minute=0)`
  const section2NoonSnippet = 'print(noon)'

  const section5SnippetA = `def f(key, d={}):
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
  return False`

  const section5SnippetB = `f('foo', {'foo': 2}) # returns True
f('foo', {'bar': 2}) # returns False
f('foo', {'z': {'foo': 2}}) # returns True`
</script>

<style>
.questions__snippet { @apply
  p-4
}
</style>