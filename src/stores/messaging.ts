import { defineStore } from 'pinia'
import { Message } from '@/types/Message'

type MessagingState = {
  loading: boolean,
  count: number,
  offset: number,
  messages: Message[],
}

export const useMessagingStore = defineStore('messaging', {
  state: (): MessagingState => ({
    loading: false,
    count: 0,
    offset: 0,
    messages: [],
  }),
  actions: {
    loadMessages: async function() {
      this.loading = true
      const response = await fetch(`${import.meta.env.VITE_API_URL}/messages`)
      const { messages, count, offset } = await response.json()
      this.messages = messages
      this.count = count
      this.offset = offset
      this.loading = false
    },
  },
})