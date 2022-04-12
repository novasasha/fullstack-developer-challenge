<template>
  <div class="page-2">
    <h3 class="page-2__title">
      Page 2
    </h3>
    <div>
      <h4>Saved input:</h4>
      <template v-if="savedInputStore.input">
        <div class="page-2__output">
          {{ savedInputStore.input ? savedInputStore.input : 'You have no saved input.' }}
        </div>
      </template>
      <template v-else>
        <div class="page-2__output--empty">
          You have no saved input.
        </div>
      </template>
    </div>
  </div>
</template>

<script lang="ts" setup>
  import { useSavedInput } from '@/stores/savedInput'

  const savedInputStore = useSavedInput()
</script>

<style lang="scss">
.page-2 {
  text-align: center;
}

.page-2__output--empty {
  font-style: italic;
}
</style>