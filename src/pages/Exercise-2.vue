<template>
  <!-- You may modify any code above this line -->
  <div class="exercise-2">
    <!-- Please do not modify the code between these comments! -->
    <div class="exercise-2__instructions">
      <h2>
        Exercise 2
      </h2>
      <p>
        You're building an application that allows users to modify some text via a text input. The user can save their input and persist it for the next time they visit the page. There's just one problem: users have given feedback that they sometimes navigate away from the page unintentionally and lose their work! You've been asked to resolve the following user stories to fix this.
      </p>

      <ul>
        <strong>A user can...</strong>
        <li>
          see a dialog box reminding them to save their work before they navigate away from the in-app page
          <ul>
            <li>
              the dialog should contain both a button that will allow the user to save their work and a button that will allow the user to discard their changes
            </li>
            <li>
              no matter the choice a user makes, they should be navigated to the next page
            </li>
          </ul>
        </li>
        <li>
          see their previously saved work when they navigate to page 1 or page 2
          <ul>
            <li>
              if a user chooses not to save their input, the saved input on the next page should reflect their previously saved work
            </li>
          </ul>
        </li>
      </ul>

      <InfoBox>
        <em>Tip:</em> The "pages" in question are those within the window to the right (or below, depending on screen size); you don't need to implement persistent storage for browser-level navigation (so no need to use <code>localStorage</code> for anything).
      </InfoBox>

      <p>
        Modify the components as you see fit to accomplish the above stories.
      </p>
    </div>
    <!-- Please do not modify the code between these comments! -->

    <!-- You may modify any code beneath this line -->
    <div class="exercise-2__results">
      <div class="exercise-2__navigation">
        <div class="exercise-2__navigation-item">
          <router-link :to="{ name: 'page-1' }">
            page 1
          </router-link>
        </div>
        <div class="exercise-2__navigation-item">
          <router-link :to="{ name: 'page-2' }">
            page 2
          </router-link>
        </div>
      </div>

      <router-view />
    </div>
  </div>
</template>

<script lang="ts" setup>
  import InfoBox from '@/components/InfoBox.vue'
</script>

<style lang="scss">
.exercise-2__navigation {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.exercise-2__navigation-item {
  white-space: nowrap;
  .router-link-active {
    color: #2c3e50;
    text-decoration: none;
  }

  &::after {
    content: "|";
    padding: 0 8px;
  }
  &:last-child::after {
    content: none;
  }
}

.exercise-2__results {
  padding: 24px 0;
  background-color: white;
  border-radius: 4px;
  box-shadow: 0 3px 3px -2px rgba(0, 0, 0, 0.2), 0 3px 4px 0 rgba(0, 0, 0, 0.14),
    0 1px 8px 0 rgba(0, 0, 0, 0.12) !important;
}
</style>