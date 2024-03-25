import { defineStore } from 'pinia'
import { Message } from '@/types/Message'

type MessagingState = {
  count: number,
  messages: Message[],
}

export const useMessagingStore = defineStore('messaging', {
  state: (): MessagingState => ({
    count: 0,
    messages: [],
  }),
  actions: {
    loadMessages: async function() {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/messages`)
      const { messages, count } = await response.json()
      this.messages = messages
      this.count = count
    },
  },
})