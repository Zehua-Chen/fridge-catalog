<template>
  <div id="demo">
    <ul>
      <li v-for="mainCat in mainCategories" :key="mainCat.id">
        {{ mainCat.name }} <button @click="remove(mainCat.id)">Delete</button>
      </li>
    </ul>
    <br />
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    const id = Number.parseInt(this.$route.params['id']);

    return {
      uid: id,
      checkedCategories: [],
      mainCategories: [],
    };
  },
  async mounted() {
    const id = Number.parseInt(this.$route.params['id']);

    this.mainCategories = await fetch(`/remove/${id}`, {
      method: 'GET',
    }).then((response) => response.json());
  },
  methods: {
    check(e) {
      if (e.target.checked) {
        console.log(e.target.value);
      }
    },
    async remove(id) {
      // const formData = new FormData();
      // formData.append('id', id)
      this.mainCategories = await fetch(`/remove/${this.uid}`, {
        method: 'DELETE',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ foodID: id }),
      }).then((response) => response.json());
    },
  },
});
</script>
