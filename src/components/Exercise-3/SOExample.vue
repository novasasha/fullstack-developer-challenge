<template>
  <div class="so-example">
    <h4 class="so-example__title">
      <p-icon class="so-example__logo" icon="CircleStackIcon" size="large" />
      Stack Overflow (Example)
    </h4>

    <div class="so-example__questions">
      <template v-for="question in questions" :key="question.question_id">
        <div class="so-example__question">
          <!-- eslint-disable-next-line vue/no-v-html -->
          <a class="so-example__question-title" :href="question.link" v-html="question.title" />

          <div class="so-example__question-owner">
            <img class="so-example__owner-image" :src="question.owner.profile_image">
            <a class="so-example__owner-name" :href="question.owner.link" target="_blank">{{ question.owner.display_name }}</a>
            <div class="so-example__owner-reputation">
              {{ question.owner.reputation }}
            </div>
            <template v-if="!question.is_answered">
              <div class="so-example__question-answered">
                <FontAwesomeIcon :icon="['fas', 'circle-check']" />
                Answered
              </div>
            </template>
          </div>

          <div class="so-example__tags">
            <template v-for="tag in question.tags" :key="tag">
              <div class="so-example__tag">
                {{ tag }}
              </div>
            </template>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script lang="ts" setup>
  import { onMounted, reactive } from 'vue'

  type Question = {
    accepted_answer_id?: number,
    answer_count: number,
    content_license: string,
    creation_date: number,
    is_answered: boolean,
    last_activity_date: number,
    last_edit_date?: number,
    link: string,
    owner: Owner,
    question_id: number,
    score: number,
    tags: string[],
    title: string,
    view_count: number,
  }

  type Owner = {
    accept_rate?: number,
    account_id: number,
    display_name: string,
    link: string,
    profile_image: string,
    reputation: number,
    user_id: number,
    user_type: string,
  }

  const questions: Question[] = reactive([])
  const url = 'https://api.stackexchange.com/2.3/questions?pagesize=10&order=desc&sort=activity&site=stackoverflow&tagged=prefect'

  onMounted(async () => {
    const response = await fetch(url)
    const data = await response.json()

    questions.push(...data.items)
  })
</script>

<style>
.so-example__title { @apply
  flex
  items-center
  justify-center
  gap-2
  mb-6
  text-xl
}

.so-example__logo { @apply
  text-amber-500
}

.so-example__questions { @apply
  flex
  flex-wrap
  justify-center
  items-start
  gap-6
}

.so-example__question { @apply
  flex
  flex-col
  gap-4
  px-4
  py-2
  max-w-xs
  bg-slate-50
  text-slate-950
  rounded-lg
}

.so-example__question-owner {
  grid-template-areas:
    'profile name answered'
    'profile reputation answered';
  grid-template-columns: 40px 1fr 1fr;

  @apply
  grid
  text-sm
  items-center
  gap-x-1
}

.so-example__owner-name {
  grid-area: name;

  @apply
  text-sky-500
}

.so-example__owner-image {
  grid-area: profile;

  @apply
  w-full
  rounded
}

.so-example__owner-reputation {
  grid-area: reputation;

  @apply
  text-xs
}

.so-example__question-answered { @apply
  text-emerald-500
}

.so-example__tags { @apply
  flex
  flex-wrap
  gap-1
}

.so-example__tag { @apply
  text-xs
  text-sky-700
  bg-sky-100
  rounded
  px-2
  py-1
}
</style>