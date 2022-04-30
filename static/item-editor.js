Vue.component("item-editor", {
  template: `
    <div>
      <label for="">Name</label>
      <input class="form-control" type="text" v-model="value.name">

      <label for="">Price</label>
      <input class="form-control" type="number" v-model="value.price">

      <label for="">Amount</label>
      <input class="form-control" type="number" v-model="value.amount">

      <label for="">Calories</label>
      <input class="form-control" type="number" v-model="value.calories">

      <label v-if="supportsDate" for="">Purchase</label>
      <input v-if="supportsDate" class="form-control" type="date" v-model="value.purchase">

      <label v-if="supportsDate" for="">Use By</label>
      <input v-if="supportsDate" class="form-control" type="date" v-model="value.useBy">

      <label for="">Market</label>
      <select class="form-select" v-model="value.mname">
        <option
          v-for="market in allMarkets"
          :key="market.mname"
          :value="market.mname"
        >
          {{ market.mname }}
        </option>
      </select>

      <label for="">Compartment</label>
      <select class="form-select" v-model="value.clevel">
        <option
          v-for="compartment in allCompartments"
          :key="compartment.clevel"
          :value="compartment.clevel"
        >
          {{ compartment.clevel }}
        </option>
      </select>
    </div>
  `,
  props: {
    "value": {
      type: Object,
      default: createDefaultItem()
    },
    supportsDate: {
      type: Boolean,
      default: true,
    }
  },
  data() {
    return {
      allMarkets: [],
      allCompartments: []
    }
  },
  async mounted() {
    fetch("/api/markets")
      .then(response => response.json())
      .then(markets => {
        this.allMarkets = markets;

        if (this.allMarkets.length > 0) {
          if (!this.value.mname) {
            this.value.mname = this.allMarkets[0].mname;
          }
        }
      });

    fetch("/api/compartments")
      .then(response => response.json())
      .then(compartments => {
        this.allCompartments = compartments;

        if (this.allCompartments.length > 0) {
          if (this.value.clevel === -1) {
            this.value.clevel = this.allCompartments[0].clevel;
          }
        }
      });
  }
})

function createDefaultItem() {
  return {
    name: "",
    price: 0,
    amount: 0,
    calories: 0,
    purchase: Date(),
    useBy: Date(),
    mname: "",
    clevel: -1
  }
}
