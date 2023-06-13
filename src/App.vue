<template>
  <div id="app" class="app">
    <div class="app__heading">
      <img alt="Prefect logo" class="app__heading-logo" src="@/assets/logo.svg">
      <h2>
        Full Stack Developer Challenge
      </h2>

      <div class="app__navigation">
        <div class="app__navigation-item">
          <router-link :to="{ name: 'instructions' }" exact>
            Instructions
          </router-link>
        </div>
        <div class="app__navigation-item">
          <router-link :to="{ name: 'exercise-1' }">
            Exercise #1
          </router-link>
        </div>
        <div class="app__navigation-item">
          <router-link :to="{ name: 'exercise-2' }">
            Exercise #2
          </router-link>
        </div>
        <div class="app__navigation-item">
          <router-link :to="{ name: 'exercise-3' }">
            Exercise #3
          </router-link>
        </div>
      </div>
    </div>

    <div class="app__router-view">
      <router-view />
    </div>
  </div>
</template>

<script lang="ts" setup>
  import { useColorTheme } from '@prefecthq/prefect-design'

  useColorTheme()
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app { @apply
  text-foreground
}

.app__heading {
  text-align: center;
}

.app__heading-logo {
  max-width: 200px;
}

.app__navigation {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.app__navigation-item {
  white-space: nowrap;
}

.app__navigation-item .router-link-active {
  color: #2c3e50;
  text-decoration: none;
}

.app__navigation-item::after {
  content: "|";
  padding: 0 8px;
}

.app__navigation-item:last-child::after {
    content: none;
}


.app__router-view {
  max-width: 750px;
  margin-left: auto;
  margin-right: auto;
}

a {
  color: #27b1ff;
  font-weight: bold;
}
</style>