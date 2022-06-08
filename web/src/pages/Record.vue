<template>
  <form id="signfood" @submit.prevent="processForm">
    <div class="field">
      <label class="label">name</label>
      <input type="text" class="input" name="name" v-model="name" />
    </div>
    <div class="field">
      <label class="label">food</label>
      <input type="text" class="input" name="food" v-model="food" />
    </div>

    <div class="field">
      <label class="label">amount</label>
      <input type="text" class="input" name="amount" v-model="amount" />
    </div>
    <div class="field has-text-right">
      <button @click="record" type="submit">submit</button>
    </div>
    <br />
    <div>Calories you will take: {{ foodInfo.calories }}</div>
    <br />
    <div>Allgergens you need to pay attention to: {{ foodInfo.allergens }}</div>
    <br />
    <div>Nutritions you could get: {{ foodInfo.nutritions }}</div>
  </form>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      name: '',
      food: '',
      amount: '',
      foodInfo: '',
    };
  },
  methods: {
    processForm: function () {
      console.log({ name: this.name, food: this.food, amount: this.amount });
    },
    async record() {
      this.foodInfo = await fetch(
        `/record/${this.name}/${this.food}/${this.amount}`
      ).then((response) => response.json());
      console.log(this.foodInfo);
    },
  },
});
</script>
