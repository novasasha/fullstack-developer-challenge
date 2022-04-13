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
    // questions.push(...[{ 'tags':['python', 'selenium', 'selenium-webdriver', 'webdriverwait'], 'owner':{ 'account_id':24165722, 'reputation':35, 'user_id':18128593, 'user_type':'registered', 'profile_image':'https://lh3.googleusercontent.com/a-/AOh14Gi22F-GbiXsXu7D7uf8x9FwuLHsCFo5ZCB16yUo=k-s256', 'display_name':'Auditor', 'link':'https://stackoverflow.com/users/18128593/auditor' }, 'is_answered':false, 'view_count':56, 'answer_count':1, 'score':0, 'last_activity_date':1649801426, 'creation_date':1647020299, 'last_edit_date':1647254475, 'question_id':71442553, 'content_license':'CC BY-SA 4.0', 'link':'https://stackoverflow.com/questions/71442553/selenium-python-webdriverwait-timeoutexception', 'title':'Selenium + Python: WebDriverWait TimeoutException' }, { 'tags':['python', 'multithreading'], 'owner':{ 'account_id':2827370, 'reputation':511, 'user_id':2875917, 'user_type':'registered', 'accept_rate':64, 'profile_image':'https://i.stack.imgur.com/9VM5O.jpg?s=256&g=1', 'display_name':'Wall-E', 'link':'https://stackoverflow.com/users/2875917/wall-e' }, 'is_answered':false, 'view_count':2, 'answer_count':0, 'score':0, 'last_activity_date':1649801410, 'creation_date':1649801410, 'question_id':71849674, 'content_license':'CC BY-SA 4.0', 'link':'https://stackoverflow.com/questions/71849674/parameter-sweep-with-slurm-vs-python-multiprocessing', 'title':'Parameter sweep with SLURM vs Python multiprocessing' }, { 'tags':['c#', 'conditional-statements', 'streamreader', 'write', 'peek'], 'owner':{ 'account_id':143551, 'reputation':5, 'user_id':3937741, 'user_type':'registered', 'accept_rate':33, 'profile_image':'https://graph.facebook.com/1051031844/picture?type=large', 'display_name':'Randy Johnson', 'link':'https://stackoverflow.com/users/3937741/randy-johnson' }, 'is_answered':false, 'view_count':18, 'answer_count':0, 'score':0, 'last_activity_date':1649801403, 'creation_date':1649800463, 'last_edit_date':1649801403, 'question_id':71849551, 'content_license':'CC BY-SA 4.0', 'link':'https://stackoverflow.com/questions/71849551/creating-lines-of-152-characters-and-adjusting-line-endings-at-ends-of-words', 'title':'Creating lines of 152 characters and adjusting line endings at ends of words' }])
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