<template>
  <div class="container">
    <div class="row">
      <div class="column">
        <h1>{{ name }}</h1>
      </div>
    </div>
  </div>

  <div id="dashboard" class="container">
    <!-- Compartments -->

    <div class="row mt-5">
      <div class="col">
        <h2>Compartments</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Level</th>
              <th scope="col">Temperature</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="compartment in compartments" :key="compartment.clevel">
              <td>{{ compartment.clevel }}</td>
              <td>{{ compartment.temperature }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="row">
      <div class="col d-grid gap-2">
        <RouterLink class="btn btn-primary" to="/dashboard/add_compartment">
          Add Compartment
        </RouterLink>
      </div>
    </div>

    <!-- Markets -->

    <div class="row mt-5">
      <div class="col">
        <h2>Markets</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Location</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="market in markets" :key="market.mname">
              <td>{{ market.mname }}</td>
              <td>{{ market.location }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="row">
      <div class="col d-grid gap-2">
        <RouterLink class="btn btn-primary" to="/dashboard/add_market">
          Add Market
        </RouterLink>
      </div>
    </div>

    <!-- Items -->

    <div class="row mt-5">
      <div class="col">
        <h2>Items</h2>
      </div>
      <div class="col">
        Compartment
        <select class="form-select" v-model="searchedCompartment">
          <option value="-1">All</option>
          <option
            v-for="compartment in compartments"
            :key="compartment.clevel"
            :value="compartment.clevel"
          >
            {{ compartment.clevel }}
          </option>
        </select>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Compartment</th>
              <th scope="col">Share</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in itemsInSearchedCompartment" :key="item.iid">
              <td scope="row">{{ item.name }}</td>
              <td>{{ item.clevel }}</td>
              <td>{{ item.share }}</td>
              <td>
                <RouterLink
                  class="btn btn-secondary"
                  :to="`/dashboard/edit_item/${item.iid}`"
                >
                  Edit
                </RouterLink>
                <RouterLink
                  class="btn btn-secondary"
                  :to="`/dashboard/prepare_item/${item.iid}`"
                >
                  Prepare
                </RouterLink>
                <RouterLink
                  class="btn btn-secondary"
                  :to="`/dashboard/share_item/${userId}/${item.iid}`"
                >
                  Share
                </RouterLink>
                <RouterLink
                  class="btn btn-secondary"
                  :to="`/dashboard/move_item/${item.clevel}/${item.iid}`"
                >
                  Move
                </RouterLink>
                <RouterLink
                  class="btn btn-secondary"
                  :to="`/dashboard/nutrient_item/${item.iid}`"
                >
                  Nutrients
                </RouterLink>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="row">
      <div class="col d-grid gap-2">
        <RouterLink
          class="btn btn-primary"
          :to="`/dashboard/add_item/${userId}`"
        >
          Add Item
        </RouterLink>
        <RouterLink class="btn btn-danger" :to="`/dashboard/remove/${userId}`">
          Remove Item
        </RouterLink>
      </div>
    </div>

    <!-- Preparation Methods -->

    <div class="row mt-5">
      <div class="col">
        <h2>Preparation Methods</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Name</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="method in methods" :key="method.method">
              <td>{{ method.method }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="row">
      <div class="col d-grid gap-2">
        <RouterLink
          class="btn btn-primary"
          to="/dashboard/add_preparation_method"
        >
          Add Preparation Method
        </RouterLink>
      </div>
    </div>

    <!-- Nutrient -->

    <div class="row mt-5">
      <div class="col">
        <h2>Nutrients</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Name</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="nutrient in nutrients" :key="nutrient.nname">
              <td>{{ nutrient.nname }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="row">
      <div class="col d-grid gap-2">
        <RouterLink class="btn btn-primary" to="/dashboard/add_nutrient">
          Add Nutrient
        </RouterLink>
      </div>
    </div>

    <div class="row mt-2">
      <div class="col d-grid gap-2">
        <a class="btn btn-primary" href="/record">Record Consumption</a>
        <a class="btn btn-primary" href="/checkPay">Create Bill</a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import type { Compartment } from 'app/services/compartment';
import type { Market } from 'app/services/market';
import type { Item } from 'app/services/item';

const route = useRoute();
const userId = Number.parseInt(route.params['id'] as string);
const name = ref('User');

const compartments = ref<Compartment[]>([]);
const items = ref<Item[]>([]);
const methods = ref([]);
const markets = ref<Market[]>([]);
const nutrients = ref([]);
const searchedCompartment = ref(-1);

const itemsInSearchedCompartment = computed(() => {
  if (searchedCompartment.value == -1) {
    return items.value;
  }

  console.log('filter');

  return items.value.filter((i) => {
    console.log(searchedCompartment.value);
    console.log(i.clevel === searchedCompartment.value);
    return i.clevel === searchedCompartment.value;
  });
});

onMounted(() => {
  fetch(`/api/compartments`)
    .then((response) => response.json())
    .then((value) => {
      compartments.value = value;
    });

  fetch(`/api/items/${userId}`)
    .then((response) => response.json())
    .then((value) => (items.value = value));

  fetch(`/api/methods`)
    .then((response) => response.json())
    .then((value) => (methods.value = value));

  fetch(`/api/markets`)
    .then((response) => response.json())
    .then((value) => (markets.value = value));

  fetch(`/api/nutrients`)
    .then((response) => response.json())
    .then((value) => (nutrients.value = value));
});
</script>
