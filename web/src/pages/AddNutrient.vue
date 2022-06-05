<template>
  <div id="newNutrient" class="container">
    <div class="row">
      <div class="col">
        <div class="form-group">
          <label for="">Name</label>
          <input class="form-control" type="text" v-model="nname" />

          <button class="btn btn-primary" @click="create">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const nname = ref('');
const router = useRouter();

async function create() {
  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      nname: nname.value,
    }),
  };

  const response = await fetch('/api/nutrients', request);

  if (response.status == 201) {
    router.back();
  } else {
    alert(response.status);
  }
}
</script>
