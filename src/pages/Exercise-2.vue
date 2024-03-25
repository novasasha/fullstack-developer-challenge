<template>
  <!-- You may modify any code above this line -->

  <!-- Please do not modify the code between these comments! -->
  <p-content class="exercise-2">
    <p-heading heading="2">
      Exercise 2: Inbox
    </p-heading>

    <p-content>
      <p>
        You're building an application that has an inbox to display email-like messages between users. Someone else on
        your team has scaffolded the feature but you've been asked to extend the component to resolve the following user
        and developer stories, which are stories written from the perspective of someone on your team that might pick up
        the work later.
      </p>

      <p>
        To reset the db to its initial state:
        <p-button dangerous primary small :loading="store.loading" @click="store.resetMessages()">
          Reset messages
        </p-button>
      </p>

      <p-message info>
        There are many ways to achieve these stories. You should read through the source component to get an
        understanding of how it works.
        <br>
      </p-message>

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
          choose to override the styling and contents of the title of the component (for example to change the title
          from "Inbox" to "My Inbox" or to add a user avatar)
        </li>
        <li>
          change the active color of selected messages
        </li>
      </ul>
    </p-content>
    <!-- Please do not modify the code between these comments! -->

    <!-- You may modify any code beneath this line -->
    <InboxList :loading="store.loading" :error="store.error" :messages="store.messages" />
  </p-content>
</template>

<script lang="ts" setup>
  import InboxList from '@/components/Exercise-2/InboxList.vue'
  import { useMessagingStore } from '@/stores/messaging'

  const store = useMessagingStore()

  await store.loadMessages()
</script>