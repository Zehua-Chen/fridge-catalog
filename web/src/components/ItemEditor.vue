<template>
  <div>
    <label for="">Name</label>
    <input class="form-control" type="text" v-model="modelValue.name" />

    <label for="">Price</label>
    <input class="form-control" type="number" v-model="modelValue.price" />

    <label for="">Amount</label>
    <input class="form-control" type="number" v-model="modelValue.amount" />

    <label for="">Calories</label>
    <input class="form-control" type="number" v-model="modelValue.calories" />

    <label v-if="supportsDate" for="">Purchase</label>
    <input
      v-if="supportsDate"
      class="form-control"
      type="date"
      v-model="modelValue.purchase"
    />

    <label v-if="supportsDate" for="">Use By</label>
    <input
      v-if="supportsDate"
      class="form-control"
      type="date"
      v-model="modelValue.useBy"
    />

    <label for="">Market</label>
    <select class="form-select" v-model="modelValue.mname">
      <option
        v-for="market in allMarkets"
        :key="market.mname"
        :value="market.mname"
      >
        {{ market.mname }}
      </option>
    </select>

    <label for="">Compartment</label>
    <select class="form-select" v-model="modelValue.clevel">
      <option
        v-for="compartment in allCompartments"
        :key="compartment.clevel"
        :value="compartment.clevel"
      >
        {{ compartment.clevel }}
      </option>
    </select>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { createDefaultItem } from 'app/services/item';
import { Market } from 'app/services/market';
import { Compartment } from 'app/services/compartment';

const allMarkets = ref<Market[]>([]);
const allCompartments = ref<Compartment[]>([]);

const props = defineProps({
  modelValue: {
    type: Object,
    default: createDefaultItem(),
  },
  supportsDate: {
    type: Boolean,
    default: true,
  },
});

const emit = defineEmits(['update:modelValue']);

onMounted(() => {
  fetch('/api/markets')
    .then((response) => response.json())
    .then((markets) => {
      allMarkets.value = markets;

      if (allMarkets.value.length > 0) {
        if (!props.modelValue.mname) {
          props.modelValue.mname = allMarkets.value[0].mname;
        }
      }
    });

  fetch('/api/compartments')
    .then((response) => response.json())
    .then((compartments) => {
      allCompartments.value = compartments;

      if (allCompartments.value.length > 0) {
        if (props.modelValue.clevel === -1) {
          props.modelValue.clevel = allCompartments.value[0].clevel;
        }
      }
    });
});
</script>
