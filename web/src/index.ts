import { createApp } from 'vue';
import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import App from './App.vue';
import Login from './pages/Login.vue';
import Dashboard from './pages/Dashboard.vue';
import AddMarket from './pages/Addmarket.vue';
import AddCompartment from './pages/AddCompartment.vue';
import AddItem from './pages/AddItem.vue';
import AddNutrient from './pages/AddNutrient.vue';
import AddPreparationMethod from 'app/pages/AddPreparationMethod.vue';
import EditItem from 'app/pages/EditItem.vue';
import MoveItem from 'app/pages/MoveItem.vue';
import ShareItem from 'app/pages/ShareItem.vue';

const routes: RouteRecordRaw[] = [
  { path: '/', component: Login },
  { path: '/dashboard/:id', component: Dashboard },
  { path: '/dashboard/add_market', component: AddMarket },
  { path: '/dashboard/add_compartment', component: AddCompartment },
  { path: '/dashboard/add_item/:id', component: AddItem },
  { path: '/dashboard/add_nutrient', component: AddNutrient },
  {
    path: '/dashboard/add_preparation_method',
    component: AddPreparationMethod,
  },
  {
    path: '/dashboard/edit_item/:id',
    component: EditItem,
  },
  {
    path: '/dashboard/move_item/:compartment/:item',
    component: MoveItem,
  },
  {
    path: '/dashboard/share_item/:owner/:item',
    component: ShareItem,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

const app = createApp(App);

app.use(router);
app.mount('#app');
