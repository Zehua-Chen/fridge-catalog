<template>
  <div id="prepareItem" class="container">
    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Method</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="preparation in preparations"
              :key="`${preparation.method}-${iid}`"
            >
              <td>{{ preparation.method }}</td>
              <td>
                <button
                  class="btn btn-danger"
                  @click="delete_(preparation.method)"
                >
                  Delete
                </button>
              </td>
            </tr>
            <tr v-for="method in otherMethods" :key="method.method">
              <td>{{ method.method }}</td>
              <td>
                <button class="btn btn-primary" @click="add(method.method)">
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
      preparations: [],
      allMethods: [],
      usedMethods: new Set(),
    };
  },
  computed: {
    otherMethods() {
      return this.allMethods.filter(
        (method) => !this.usedMethods.has(method.method)
      );
    },
  },
  methods: {
    async add(method) {
      const request = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          method: method,
          iid: this.iid,
        }),
      };

      const response = await fetch('/api/preparations', request);

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
        `/api/preparations?iid=${this.iid}&method=${method}`,
        request
      );

      if (response.status === 202) {
        await this.reload();
      }
    },
    reload() {
      const preparations = fetch(`/api/preparations?iid=${this.iid}`)
        .then((response) => response.json())
        .then((preparations) => {
          this.preparations = preparations;

          this.usedMethods.clear();

          this.preparations.forEach((p) => {
            this.usedMethods.add(p.method);
          });
        });

      return Promise.all([preparations]);
    },
  },
  mounted() {
    fetch('/api/methods')
      .then((response) => response.json())
      .then((methods) => (this.allMethods = methods));

    this.reload();
  },
});
</script>
