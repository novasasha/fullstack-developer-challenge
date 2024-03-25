<template>
  <p-layout-default id="app" class="app">
    <template #header>
      <div class="app__heading">
        <p-icon alt="Prefect logo" class="app__heading-logo" icon="Prefect" />

        <p-heading heading="1">
          Full-Stack Developer Challenge
        </p-heading>

        <p-theme-toggle />

        <div class="app__navigation">
          <template v-for="item in navItems" :key="item.to">
            <div class="app__navigation-item">
              <p-link :to="item.to" exact>
                {{ item.title }}
              </p-link>
            </div>
          </template>
        </div>
      </div>
    </template>

    <div class="app__router-view">
      <suspense>
        <router-view />
      </suspense>
    </div>
  </p-layout-default>
</template>

<script lang="ts" setup>
  import { useColorTheme } from '@prefecthq/prefect-design'

  useColorTheme()

  const navItems = [
    { title: 'Instructions', to: '/' },
    { title: 'Exercise #1', to: '/exercise-1' },
    { title: 'Exercise #2', to: '/exercise-2' },
    { title: 'Exercise #3', to: '/exercise-3' },
  ]
</script>

<style>
.app { @apply
  p-6
}

.app__heading { @apply
  flex
  flex-col
  items-center
  justify-center
  gap-2
}

.app__heading-logo { @apply
  mx-auto
  my-4
  h-12
  w-12
}

.app__navigation { @apply
  flex
  justify-center
  flex-wrap
}

.app__navigation-item { @apply
  whitespace-nowrap
}

.app__navigation-item .router-link-active { @apply
  text-subdued
  no-underline
}

.app__navigation-item:not(:last-child)::after {
  content: "|";
  padding: 0 8px;
}

.app__router-view { @apply
  mx-auto
  max-w-4xl
}

ul { @apply
  list-disc
  list-inside
  my-4
}

ul li { @apply
  mb-1
}
</style>