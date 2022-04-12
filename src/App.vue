<template>
  <div id="app" class="app">
    <div class="app__heading">
      <img alt="Prefect logo" class="app__heading-logo" src="./assets/logo.svg">
      <h2 class="text-h2">
        Front End Software Engineer Challenge
      </h2>

      <div class="app__navigation">
        <div class="app__navigation-item">
          <router-link to="/" exact>
            Instructions
          </router-link>
        </div>
        <div class="app__navigation-item">
          <router-link to="/exercise-1">
            Exercise #1
          </router-link>
        </div>
        <div class="app__navigation-item">
          <router-link to="/exercise-2">
            Exercise #2
          </router-link>
        </div>
        <div class="app__navigation-item">
          <router-link to="/exercise-3">
            Exercise #3
          </router-link>
        </div>
      </div>
    </div>

    <transition name="fade" mode="out-in">
      <router-view />
    </transition>
  </div>
</template>

<style lang="scss">
#app {
  color: #2c3e50;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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
}

.app__navigation-item {
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

a {
  color: #27b1ff;
  font-weight: bold;
}
</style>