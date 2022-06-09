<template>
  <div id="newCompartment" class="container">
    <div class="row">
      <div class="column">
        <div class="form-group">
          <label for="">Level</label>
          <input
            class="form-control"
            type="number"
            placeholder="Level"
            v-model="level"
          />
          <label for="">Temperature</label>
          <input
            class="form-control"
            type="number"
            placeholder="Temperature"
            v-model="temperature"
          />
          <button class="btn btn-primary mt-2" @click="create">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { createCompartment } from 'app/services/compartment';

const level = ref(0);
const temperature = ref(0);

const router = useRouter();

async function create() {
  try {
    await createCompartment((draft) => {
      draft.level = level.value;
      draft.temperature = temperature.value;
    });
    router.back();
  } catch (e) {
    alert(e);
  }
}
</script>
