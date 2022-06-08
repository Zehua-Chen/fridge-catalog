<template>
  <div>
    <label for="">Name</label>
    <input
      class="form-control"
      type="text"
      :value="modelValue.name"
      @input="set($event, 'name')"
    />

    <label for="">Price</label>
    <input
      class="form-control"
      type="number"
      :value="modelValue.price"
      @input="set($event, 'price', toNumber)"
    />

    <label for="">Amount</label>
    <input
      class="form-control"
      type="number"
      :value="modelValue.amount"
      @input="set($event, 'amount', toNumber)"
    />

    <label for="">Calories</label>
    <input
      class="form-control"
      type="number"
      :value="modelValue.calories"
      @input="set($event, 'calories', toNumber)"
    />

    <label v-if="supportsDate" for="">Purchase</label>
    <input
      v-if="supportsDate"
      class="form-control"
      type="date"
      :value="modelValue.purchase"
      @input="set($event, 'purchase')"
    />

    <label v-if="supportsDate" for="">Use By</label>
    <input
      v-if="supportsDate"
      class="form-control"
      type="date"
      :value="modelValue.useBy"
      @input="set($event, 'useBy')"
    />

    <label for="">Market</label>
    <select
      class="form-select"
      :value="modelValue.mname"
      @input="set($event, 'mname')"
    >
      <option
        v-for="market in allMarkets"
        :key="market.mname"
        :value="market.mname"
      >
        {{ market.mname }}
      </option>
    </select>

    <label for="">Compartment</label>
    <select
      class="form-select"
      :value="modelValue.clevel"
      @input="set($event, 'clevel', toNumber)"
    >
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
import { produce } from 'immer';
import { Item } from 'app/services/item';
import { Market } from 'app/services/market';
import { Compartment } from 'app/services/compartment';

const allMarkets = ref<Market[]>([]);
const allCompartments = ref<Compartment[]>([]);

const props = defineProps({
  modelValue: {
    type: Item,
    default: new Item(),
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

function toNumber(s: string): number {
  return Number.parseFloat(s);
}

function set(
  event: Event,
  property: string,
  convert: (input: string) => any = (x) => x
) {
  const newItem = produce(props.modelValue, (draft) => {
    const value = (event.target as HTMLInputElement).value;
    const converted = convert(value);

    Reflect.set(draft, property, converted);
  });

  emit('update:modelValue', newItem);
}
</script>
