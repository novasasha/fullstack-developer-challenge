<template>
  <div class="message-item" :class="classes.item" @click.prevent="toggleActive">
    <div class="message-item__checkbox">
      <p-icon v-if="selected" icon="CheckIcon" class="message-item__checkbox-icon" />
    </div>
    <div>
      <div class="message-item__from">
        {{ message.from }}
      </div>
      <div class="message-item__subject">
        {{ message.subject }}
      </div>
    </div>
    <div class="message-item__timestamp">
      {{ message.timestamp }}
    </div>
  </div>
</template>

<script lang="ts" setup>
  import { computed, PropType } from 'vue'
  import { Message } from '@/types/Message'

  const props = defineProps({
    message: {
      type: Object as PropType<Message>,
      required: true,
    },
    selected: {
      type: Boolean,
    },
  })

  const emit = defineEmits<{
    (event: 'update:selected', value: boolean): void,
  }>()

  const classes = computed(() => ({
    item: {
      'message-item--selected': props.selected,
    },
  }))

  function toggleActive(): void {
    emit('update:selected', !props.selected)
  }
</script>

<style>
.message-item { @apply
  flex
  items-center
  justify-start
  px-6
  py-3
  cursor-pointer
  bg-center
}

.message-item {
  transition: background 800ms;
}

.message-item:hover {
  background: rgba(133, 146, 158, 0.05)
    radial-gradient(circle, transparent 1%, rgba(133, 146, 158, 0.05) 1%)
    center/15000%;
}

.message-item:active { @apply
  bg-slate-800
  bg-opacity-5
}

.message-item:active {
  background-size: 100%;
  transition: background 0s;
}

.message-item--selected .message-item__from { @apply
  text-teal-600
}

.message-item__checkbox-icon { @apply
  h-5
  w-5
}

.message-item__checkbox { @apply
  flex
  items-center
  border
  border-foreground-50
  rounded
  w-5
  h-5
  mr-4
}

.message-item--selected .message-item__checkbox { @apply
  border-teal-600
  bg-teal-600
}

.message-item__from { @apply
  font-medium
}

.message-item__subject { @apply
  text-sm
  text-subdued-300
}

.message-item__timestamp { @apply
  text-xs
  ml-auto
}
</style>
