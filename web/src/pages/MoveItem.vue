<template>
  <div id="moveItem" class="container">
    <div class="row">
      <div class="col">
        <div class="form-group">
          <select class="form-select" v-model="selectedCompartment">
            <option
              v-for="compartment in compartments"
              :key="compartment.clevel"
              :value="compartment.clevel"
            >
              {{ compartment.clevel }} (Temperature:
              {{ compartment.temperature }})
            </option>
          </select>

          <button class="btn btn-primary" @click="moveItem">Move</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { Compartment, getCompartments } from 'app/services/compartment';

const route = useRoute();
const router = useRouter();

const compartment = computed(() => {
  return Number.parseInt(route.params['compartment'] as string);
});

const itemID = computed(() => {
  return Number.parseInt(route.params['item'] as string);
});

const compartments = ref<Compartment[]>([]);
const selectedCompartment = ref(-1);

onMounted(async () => {
  compartments.value = await getCompartments();

  if (compartments.value.length > 0) {
    if (selectedCompartment.value === -1) {
      for (let i = 0; i < compartments.value.length; i++) {
        if (compartments.value[i].clevel !== compartment.value) {
          selectedCompartment.value = compartments.value[i].clevel;
          break;
        }
      }
    }
  }
});

async function moveItem() {
  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      iid: itemID.value,
      originalCompartment: compartment.value,
      newCompartment: selectedCompartment.value,
    }),
  };

  const response = await fetch('/api/move', request);

  if (response.status === 202) {
    router.back();
  } else {
    alert(response.status);
  }
}
</script>
