<template>
  <p-content class="home-instructions">
    <p-heading heading="2">
      Instructions
    </p-heading>

    <p-content>
      <p>
        If you've made it this far you've already completed the first step by installing the project dependencies and starting your Vue development server... good job!
      </p>

      <p>
        <strong>
          Please read all instructions carefully before you begin to work on the exercises.
        </strong>
      </p>

      <p>
        This challenge consists of 3 exercises. The goal is to get a sense for how you solve problems and implement your code - these questions are not designed to trick you.
      </p>

      <p>
        No additional packages or libraries are required to complete this challenge but you may add any that you wish. Please do not modify this instructions component (found at <p-code inline>
          /src/pages/HomeInstructions.vue
        </p-code>) or any of the instruction text for the exercise (these will be clearly denoted in the code) until your submission has been graded. Any other code (including router, store, styling, and components) are free for you to modify at your discretion.
      </p>

      <InfoBox>
        <em>Tip #2:</em> The <p-code inline>
          p-
        </p-code> prefixed components in this application come from the <p-link href="https://prefect-design.netlify.app">
          Prefect Design
        </p-link> library. You're free to use these components in your solution if you wish but you're not required to do so.
      </InfoBox>
    </p-content>

    <p-divider />

    <p-content>
      <p-heading heading="4">
        Submission
      </p-heading>
      <p>
        This project should be submitted by adding the following users as collaborators to your cloned repository on GitHub:
        <ul>
          <li>
            <p-link href="https://github.com/znicholasbrown" target="_blank">
              @znicholasbrown
            </p-link>
          </li>
          <li>
            <p-link href="https://github.com/zhen0" target="_blank">
              @zhen0
            </p-link>
          </li>
          <li>
            <p-link href="https://github.com/pleek91" target="_blank">
              @pleek91
            </p-link>
          </li>
          <li>
            <p-link href="https://github.com/abrookins" target="_blank">
              @abrookins
            </p-link>
          </li>
        </ul>

        Once you've done so, please send an email to <p-link href="mailto:jenny@prefect.io" target="_blank">
          jenny@prefect.io
        </p-link> to confirm your submission.
      </p>
    </p-content>

    <p-divider />

    <p-content>
      <p-heading heading="4">
        Making the repo public
      </p-heading>

      <p>
        <strong>The work you do on this project is your own</strong>. As such, you can make it publicly available at your discretion (on your GitHub, as part of a portfolio etc.).
      </p>
      <p>
        However, if you plan to make this repository public, <strong>please do not do so until after your submission has been graded</strong> (we'll let you know when that is!). In addition, please remove or replace Prefect in the <p-code inline>
          &lt;title&gt;
        </p-code> block of the root html file (found in  <p-code inline>
          /public/index.html
        </p-code>) as well as the <p-code inline>
          &lt;link&gt;
        </p-code> and <p-code inline>
          &lt;meta&gt;
        </p-code> blocks between the comments in that same file as well as all associated logos. Last, please remove or replace the Prefect logo in the root application file (found in <p-code inline>
          /src/App.vue
        </p-code>) and the associated <p-code inline>
          .svg
        </p-code> found in the assets folder.
      </p>
      <p>
        If you haven't modified the <p-code inline>
          index.html
        </p-code> file as part of your challenge, you can run the following command from the root of the project directory to automatically remove / replace all of the above:
      </p>

      <p-terminal :command="command" />
    </p-content>
  </p-content>
</template>

<script lang="ts" setup>
  import InfoBox from '@/components/InfoBox.vue'

  const command = 'mv public/index-template.html public/index.html && \
    rm public/{*.png,*.xml,*.ico,*.svg,*.webmanifest} && \
    mv src/assets/vue-logo.svg src/assets/logo.svg'
</script>