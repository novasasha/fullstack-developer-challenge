<template>
  <div class="info-box">
    <slot />
  </div>
</template>

<style>
.info-box { @apply
  mx-auto
  my-6
  text-sm
  border-l-4
  border-sky-500
  max-w-lg
  px-4
  py-2
  w-fit
}
</style>