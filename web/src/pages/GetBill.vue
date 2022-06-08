<template>
  <form id="checkbill" @submit.prevent="processForm">
    <div class="field">
      <label class="label">Type your name: </label>
      <input type="text" class="input" name="name" v-model="name" />
    </div>
    <div class="field">
      <label class="label">Type the person you want to pay to: </label>
      <input type="text" class="input" name="food" v-model="food" />
    </div>
    <div class="field has-text-right">
      <button type="submit">fee:</button>
    </div>
    <div>The fee you need to pay: {{ fee.price }}</div>
    <button @click="resetInput">Reset</button>
  </form>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      name: '',
      food: '',
      fee: '',
    };
  },
  methods: {
    async processForm() {
      this.fee = await fetch(`/checkPay/bill/${this.name}/${this.food}`).then(
        (response) => response.json()
      );
    },

    resetInput() {
      this.name = '';
      this.food = '';
      this.fee = '';
    },
  },
});
</script>
