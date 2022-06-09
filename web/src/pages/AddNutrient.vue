<template>
  <div id="newNutrient" class="container">
    <div class="row">
      <div class="col">
        <div class="form-group">
          <label for="">Name</label>
          <input class="form-control" type="text" v-model="name" />

          <button class="btn btn-primary" @click="create">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { createNutrient } from 'app/services/nutrients';

const name = ref('');
const router = useRouter();

async function create() {
  await createNutrient((draft) => {
    draft.name = name.value;
  });

  router.back();
}
</script>
