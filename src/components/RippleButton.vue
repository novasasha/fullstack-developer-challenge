<template>
  <button type="button" class="ripple-button ripple" v-bind="$attrs">
    <slot />
  </button>
</template>

<script lang="ts">
  import { defineComponent } from 'vue'

  export default defineComponent({
    name: 'RippleButton',
    inheritAttrs: false,
    expose: [],
  })
</script>

<style lang="scss">
.ripple-button {
  background-color: #76d7c4;
  background-position: center;
  transition: background 800ms;
  border: none;
  border-radius: 4px;
  color: white;
  cursor: pointer;
  font-weight: bold;
  font-size: 0.9rem;
  letter-spacing: 4px;
  padding: 12px;
  text-transform: uppercase;
  transition: all 150ms;
  width: 150px;

  &:disabled,
  &[disabled] {
    background-color: #ccc;
    color: #666;
    cursor: default;
  }

  &:active {
    background-color: #76d7c4;
    background-size: 100%;
    transition: background 0s;
  }
}
</style>