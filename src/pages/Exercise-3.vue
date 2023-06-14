<template>
  <!-- You may modify any code above this line -->
  <p-content class="exercise-3">
    <!-- Please do not modify the code between these comments! -->
    <p-heading heading="2">
      Exercise 3: REST API
    </p-heading>

    <p>
      For this exercise, you'll create a component (or components) that query a REST API of your choice and render the data you get back. The <code>SOExample</code> component below has been provided as a brief example.
    </p>

    <p-message info>
      <em>Tip:</em> This exercise is more open-ended than the previous exercises. Use this as an opportunity to show off your design chops!
    </p-message>

    <ul>
      <strong>To complete this exercise, ensure that you have...</strong>
      <li>
        replaced the <code>SOExample</code> component with your own component
      </li>
      <li>pulled some data from a REST API of your choice</li>
      <li>rendered that data in the mode of your choosing</li>
    </ul>

    <p>
      You may use any publicly-available REST API. Here are some ideas to help you get started.
      <ul>
        <li>
          <a href="https://api.stackexchange.com/docs" target="_blank">Stack Exchange API</a>
        </li>
        <li>
          <a href="https://api.nasa.gov/index.html" target="_blank">NASA Open APIs</a>
        </li>
        <li>
          <a href="https://github.com/r-spacex/SpaceX-API" target="_blank">SpaceX API</a>
        </li>
        <li>
          <a href="https://restcountries.com/" target="_blank">Countries API</a>
        </li>
        <li>
          <a href="https://docs.thedogapi.com/" target="_blank">The Dog API</a>
        </li>
        <li>
          <a href="https://docs.thecatapi.com/" target="_blank">The Cat API</a>
        </li>
      </ul>
    </p>

    <p>
      Modify the following component as you see fit to accomplish the above stories.
    </p>
    <!-- Please do not modify the code between these comments! -->

    <!-- You may modify any code beneath this line -->
    <SOExample />
  </p-content>
</template>

<script lang="ts" setup>
  import SOExample from '@/components/Exercise-3/SOExample.vue'
</script>