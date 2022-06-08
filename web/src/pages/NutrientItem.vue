<template>
  <div id="prepareItem" class="container">
    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Nutrient</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="nutrient in nutrients" :key="`${nutrient.nname}-${iid}`">
              <td>{{ nutrient.nname }}</td>
              <td>
                <button class="btn btn-danger" @click="delete_(nutrient.nname)">
                  Delete
                </button>
              </td>
            </tr>
            <tr v-for="nutrient in otherNutrients" :key="nutrient.nname">
              <td>{{ nutrient.nname }}</td>
              <td>
                <button class="btn btn-primary" @click="add(nutrient.nname)">
                  Add
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    const id = Number.parseInt(this.$route.params['id']);

    return {
      iid: id,
      nutrients: [],
      allNutrients: [],
      usedNutrients: new Set(),
    };
  },
  computed: {
    otherNutrients() {
      return this.allNutrients.filter(
        (nutrient) => !this.usedNutrients.has(nutrient.nname)
      );
    },
  },
  methods: {
    async add(nname) {
      const request = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          nname: nname,
          iid: this.iid,
        }),
      };

      const response = await fetch('/api/contains_nutrient', request);

      if (response.status === 201) {
        await this.reload();
      } else {
        alert(response.status);
      }
    },
    async delete_(method) {
      const request = {
        method: 'DELETE',
      };

      const response = await fetch(
        `/api/contains_nutrient?iid=${this.iid}&nname=${method}`,
        request
      );

      if (response.status === 201) {
        await this.reload();
      }
    },
    reload() {
      const nutrients = fetch(`/api/nutrients?iid=${this.iid}`)
        .then((response) => response.json())
        .then((nutrients) => {
          this.nutrients = nutrients;

          this.usedNutrients.clear();

          this.nutrients.forEach((n) => {
            this.usedNutrients.add(n.nname);
          });
        });

      return Promise.all([nutrients]);
    },
  },
  mounted() {
    fetch('/api/nutrients')
      .then((response) => response.json())
      .then((nutrients) => (this.allNutrients = nutrients));

    this.reload();
  },
});
</script>
