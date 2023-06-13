<template>
  <!-- You may modify any code above this line -->

  <!-- Please do not modify the code between these comments! -->
  <p-content class="exercise-2">
    <p-heading heading="2">
      Exercise 2: Inbox
    </p-heading>

    <p-content>
      <p>
        You're building an application that has an inbox to display email-like messages between users. Someone else on your team has scaffolded the feature but you've been asked to extend the component to resolve the following user and developer stories, which are stories written from the perspective of someone on your team that might pick up the work later.
      </p>

      <InfoBox>
        <em>Tip:</em> There are many ways to achieve these stories. You should read through the source component to get an understanding of how it works.
      </InfoBox>

      <strong>A user can...</strong>
      <ul>
        <li>
          see when a message is <strong>urgent</strong> (these messages contain a top-level key (<p-code inline>
            message.urgent
          </p-code>) to denote this)
        </li>
        <li>
          see previews of messages without opening them
        </li>
        <li>
          delete messages
        </li>
      </ul>

      <strong>A developer can...</strong>
      <ul>
        <li>
          choose to override the styling and contents of the title of the component (for example to change the title from "Inbox" to "My Inbox" or to add a user avatar)
        </li>
        <li>
          change the active color of selected messages
        </li>
      </ul>
    </p-content>

    <p>
      Modify components as you see fit to accomplish the above stories.
    </p>
    <!-- Please do not modify the code between these comments! -->

    <!-- You may modify any code beneath this line -->
    <router-view />
  </p-content>
</template>

<script lang="ts" setup>
  import InfoBox from '@/components/InfoBox.vue'
</script>