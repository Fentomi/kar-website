<template>
  <v-data-table-virtual
    v-if="isOpenOrderList"
    height="400"
    item-value="name"
    width="800"
    :headers="headers"
    :items="items"
  />
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: [],
    }
  },
  props: {
    isOpenOrderList: Boolean
  },
  computed: {
    headers() {
      return [
        { title: 'id заказа', align: 'start', key: 'Kod_zakaza'},
        { title: 'ФИО заказчика', align: 'start', key: 'FIO_zakaza'},
        { title: 'Дата заказа', align: 'start', key: 'Data_zakaza'},
        { title: 'Статус', align: 'start', key: 'Naimenovanye_stat'},
      ]
    }
  },
  methods: {
    async getOrderList() {
      await axios.get('http://127.0.0.1:5000/data/order').then(response => {
        console.log(response.data);
        this.items = response.data;
      });
    },
  },
  async created() {
    this.getOrderList();
  }
}
</script>