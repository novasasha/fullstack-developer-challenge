<template>
  <div class="so-example">
    <h3 class="so-example__title">
      <FontAwesomeIcon class="so-example__logo" :icon="['fab', 'stack-overflow']" />
      Stack Overflow (Example)
    </h3>
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
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
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
  const url = 'https://api.stackexchange.com/2.3/questions?pagesize=6&order=desc&sort=activity&site=stackoverflow&tagged=prefect'

  onMounted(async () => {
    const response = await fetch(url)
    const data = await response.json()

    questions.push(...data.items)
  })
</script>

<style lang="scss">
.so-example {
  padding: 24px 12px;
}

.so-example__logo {
  color: #e68e47;
}

.so-example__title,
.so-example__question-title {
  margin-top: 0;
  text-align: center;
}

.so-example__questions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: start;
  gap: 24px;
}

.so-example__question {
  display: flex;
  flex-direction: column;
  gap: 18px;
  max-width: 300px;
  background-color: #f3f3f3;
  padding: 8px;
}

.so-example__question-title {
  text-decoration: none;
  color: #323232;
}

.so-example__question-owner {
  display: grid;
  column-gap: 4px;
  align-items: center;
  grid-template-areas:
    'profile name answered'
    'profile reputation answered';
  grid-template-columns: 40px 1fr 1fr;
  font-size: 13px;
}

.so-example__owner-name {
  grid-area: name;
  text-decoration: none;
  color: #157fd0;
}

.so-example__owner-image {
  grid-area: profile;
  width: 100%;
}

.so-example__owner-reputation {
  grid-area: reputation;
  font-size: 12px;
}

.so-example__question-answered {
  color: #5a9e70;
}

.so-example__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin: 2px;
}

.so-example__tag {
  font-size: 12px;
  color: #39739d;
  white-space: nowrap;
  border-radius: 4px;
  padding: 4px 8px;
  background-color: #e1ecf4;
}
</style>