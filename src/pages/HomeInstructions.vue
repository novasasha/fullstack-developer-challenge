<template>
  <div class="home-instructions">
    <h2>
      Instructions
    </h2>

    <div class="home-instructions__block">
      <h3>
        Overview
      </h3>
      <p>
        If you've made it this far you've already completed the first step by installing the project dependencies and starting your Vue development server... good job!
      </p>

      <p>
        <strong>
          Please read all instructions carefully before you begin to work on the exercises.
        </strong>
      </p>

      <p>
        To start, this challenge consists of 3 exercises. The goal is to get a sense for how you solve problems and implement your code - these questions are not designed to trick you.
      </p>

      <InfoBox>
        <em>Tip #1:</em> Comments are a great way to explain your thinking and the choices you make as you work on each exercise, particularly in spots where you're less sure of your solution.
      </InfoBox>

      <p>
        No additional packages or libraries are required to complete this challenge but you may add any that you wish. Please do not modify this instructions component (found at <code>/src/pages/HomeInstructions.vue</code>) or any of the instruction text for the exercise (these will be clearly denoted in the code) until your submission has been graded. Any other code (including router, store, styling, and components) are free for you to modify at your discretion.
      </p>

      <InfoBox>
        <em>Tip #2:</em> Be creative! This is an opportunity to express yourself through code and design.
      </InfoBox>
    </div>

    <div class="home-instructions__block">
      <h3>
        Submission
      </h3>
      <p>
        This project should be submitted by adding <a href="https://github.com/znicholasbrown" target="_blank">@znicholasbrown</a> 
        and <a href="https://github.com/zhen0" target="_blank">@zhen0</a> 
        and <a href="https://github.com/pleek91" target="_blank">@pleek91</a> 
        as collaborators to your cloned repository on GitHub. Once you've done so, 
        please send an email to <a href="mailto:jenny@prefect.io" target="_blank">jenny@prefect.io</a> to confirm your submission.
      </p>
    </div>

    <div class="home-instructions__block">
      <h3>
        Making the repo public
      </h3>
      <p>
        <u>The work you do on this project is your own</u>. As such, you can make it publicly available at your discretion (on your GitHub, as part of a portfolio etc.).
      </p>
      <p>
        However, if you plan to make this repository public, <u>please do not do so until after your submission has been graded</u> (we'll let you know when that is!). In addition, please remove or replace Prefect in the <code>&lt;title&gt;</code> block of the root html file (found in <code>/public/index.html</code>) as well as the <code>&lt;link&gt;</code> and <code>&lt;meta&gt;</code> blocks between the comments in that same file as well as all associated logos. Last, please remove or replace the Prefect logo in the root application file (found in <code>/src/App.vue</code>) and the associated <code>.svg</code> found in the assets folder.
      </p>
      <p>
        If you haven't modified the <code>index.html</code> file as part of your challenge, you can run the following command from the root of the project directory to automatically remove / replace all of the above:
      </p>

      <pre class="home-instructions__replace-script">
        <code>
          <span class="home-instructions__replace-script-prefix">$</span>mv public/index-template.html public/index.html && \
            rm public/{*.png,*.xml,*.ico,*.svg,*.webmanifest} && \
            mv src/assets/vue-logo.svg src/assets/logo.svg
        </code>
      </pre>
    </div>
  </div>
</template>

<script lang="ts" setup>
  import InfoBox from '@/components/InfoBox.vue'
</script>

<style lang="scss">
.home-instructions__replace-script-prefix {
  margin-right: 4px;
}

.home-instructions__block {
  margin-bottom: 12px;
}
</style>
