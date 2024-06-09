<template>
    <v-dialog activator="#target2" width="600">
        <template v-slot:default="{ isActive }">
          <v-card
            title="Изменить существующего клиента"
          >
            <v-card-text>
              <v-text-field v-model="clientCode" label="Код заказчика"></v-text-field>
              <v-text-field v-model="clientSurname" label="Фамилия заказчика"></v-text-field>
              <v-text-field v-model="clientFirstname" label="Имя заказчика"></v-text-field>
              <v-text-field v-model="clientLastname" label="Отчество заказчика"></v-text-field>
              <v-text-field v-model="clientNumber" label="Номер телефона заказчика"></v-text-field>
            </v-card-text>
            <template v-slot:actions>
              <v-spacer/>
              <v-btn
                text="Закрыть"
                @click="isActive.value = false"
              />
              <v-btn
                text="Изменить"
                @click="editClient"
              />
            </template>
          </v-card>
        </template>
    </v-dialog>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        clientCode: null,
        clientSurname: '',
        clientFirstname: '',
        clientLastname: '',
        clientNumber: '',
      }
    },
    methods: {
      async editClient() {
        await axios.post('http://127.0.0.1:5000/data/client', {
          method: 'EDIT',
          Kod_klienta: this.clientCode,
          Name_klienta: this.clientFirstname,
          Fam_klienta: this.clientSurname,
          Otch_klienta: this.clientLastname,
          Nomer_tel: this.clientNumber,
        });
        this.clearData();
        this.$emit('needUpdateClientData');
      },
      clearData() {
        this.clientFirstname = '';
        this.clientSurname = '';
        this.clientLastname = '';
        this.clientNumber = '';
      }
    },
  }
  </script>