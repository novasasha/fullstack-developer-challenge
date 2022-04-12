import { defineStore } from 'pinia'

type SavedInputState = {
  input: string | null,
}

export const useSavedInput = defineStore('savedInput', {
  state: (): SavedInputState => ({
    input: null,
  }),
  actions: {
    save(value: string | null) {
      this.input = value
    },
  },
})