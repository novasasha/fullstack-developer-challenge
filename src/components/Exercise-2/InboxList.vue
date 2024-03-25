<template>
  <div class="inbox-list">
    <div class="inbox-list__top-bar">
      <div class="inbox-list__title">
        {{ selectedMessagesLabel }}
      </div>
      <div class="inbox-list__actions">
        <p-icon icon="MagnifyingGlassIcon" size="large" />
        <p-icon icon="EllipsisVerticalIcon" size="large" />
      </div>
    </div>

    <transition name="fade" mode="out-in">
      <p-loading-icon v-if="loading" />
      <p-message v-else-if="error" class="inbox-list__error" error>
        {{ error }}
      </p-message>
      <div v-else class="inbox-list__messages">
        <MessageItem
          v-for="message in messages"
          :key="message.id"
          :message="message"
          :selected="selectedMessages.includes(message)"
          @update:selected="toggleSelection(message, $event)"
        />
      </div>
    </transition>
  </div>
</template>


<script lang="ts" setup>
  import { computed, reactive } from 'vue'
  import MessageItem from '@/components/Exercise-2/MessageItem.vue'
  import { Message } from '@/types/Message'

  defineProps<{
    loading: boolean,
    error?: string | null,
    messages: Message[],
  }>()

  const selectedMessages: Message[] = reactive([])

  const selectedMessagesLabel = computed(() => selectedMessages.length
    ? `${selectedMessages.length} ${toPlural('message', selectedMessages.length)} selected`
    : 'Inbox')

  function toPlural(word: string, count: number): string {
    return count === 1 ? word : `${word}s`
  }

  function toggleSelection(message: Message, selected: boolean): void {
    unselectMessage(message)

    if (selected) {
      selectMessage(message)
    }
  }

  function selectMessage(message: Message): void {
    selectedMessages.push(message)
  }

  function unselectMessage(message: Message): void {
    const index = selectedMessages.findIndex((_m) => _m.id === message.id)

    if (index > -1) {
      selectedMessages.splice(index, 1)
    }
  }
</script>

<style>
.inbox-list { @apply
  rounded-lg
  overflow-hidden
  shadow-md
  max-h-[600px]
  grid
  grid-rows-[64px,1fr]
}

.inbox-list__top-bar { @apply
  flex
  items-center
  justify-between
  drop-shadow-md
  h-16
  px-6
  bg-teal-600
  text-white
}

.inbox-list__messages { @apply
  overflow-y-auto
}

.inbox-list__actions { @apply
  flex
  gap-6
}

.inbox-list__title { @apply
  text-xl
  font-bold
}

.inbox-list__error { @apply
  rounded-none
  shadow-none
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
