import { defineStore } from 'pinia'
import { Message } from '@/types/Message'

type MessagingState = {
  loading: boolean,
  count: number,
  offset: number,
  error: string | null,
  messages: Message[],
}

export const useMessagingStore = defineStore('messaging', {
  state: (): MessagingState => ({
    loading: false,
    count: 0,
    offset: 0,
    error: null,
    messages: [],
  }),
  actions: {
    loadMessages: async function() {
      try {

        this.loading = true
        const response = await fetch(`${import.meta.env.VITE_API_URL}/messages`)

        if (response.ok) {
          const { messages, count, offset } = await response.json()

          this.messages = messages
          this.count = count
          this.offset = offset
        } else {
          throw new Error(`Error: ${response.statusText}`)
        }

      } catch (error) {
        if (error instanceof Error) {
          console.error(error)

          if (error.message.includes('Failed to fetch')) {
            this.error = 'Failed to fetch messages; is the server running?'
          } else {
            this.error = error.message
          }
        }
      } finally {
        this.loading = false
      }
    },
    resetMessages: async function() {
      try {
        this.loading = true
        const response = await fetch(`${import.meta.env.VITE_API_URL}/reset`, { method: 'POST' })

        if (response.status === 204) {
          await this.loadMessages()
        }
      } catch (error) {
        if (error instanceof Error) {
          console.error(error)

          if (error.message.includes('Failed to fetch')) {
            this.error = 'Failed to reset messages; is the server running?'
          } else {
            this.error = error.message
          }
        }
      } finally {
        this.loading = false
      }
    },
  },
})