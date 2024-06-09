<template>
  <v-data-table-virtual
    v-if="isOpenClientList"
    height="400"
    item-value="name"
    width="300"
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
    isOpenClientList: Boolean
  },
  computed: {
    headers() {
      return [
        { title: 'id заказчика', align: 'start', key: 'Kod_klienta'},
        { title: 'Имя заказчика', align: 'start', key: 'Name_klienta'},
        { title: 'Фамилия заказчика', align: 'start', key: 'Fam_klienta'},
        { title: 'Отчество заказчика', align: 'start', key: 'Otch_klienta'},
        { title: 'Номер заказчика', align: 'start', key: 'Nomer_tel'},
      ]
    }
  },
  methods: {
    async getClientList() {
      await axios.get('http://127.0.0.1:5000/data/client').then(response => {
        this.items = response.data;
      });
    },
    async deleteClient() {

    },
    async editClient() {

    },
  },
  async created() {
    this.getClientList();
  }
}
</script>