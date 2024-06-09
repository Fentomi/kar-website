<template>
  <v-dialog activator="#target" width="600">
      <template v-slot:default="{ isActive }">
        <v-card
          title="Добавить нового клиента"
        >
          <v-card-text>
            <div class="mb-3">Заполните все поля, чтобы сохранить</div>
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
              :disabled="disabledBtn"
              text="Сохранить"
              @click="saveClient"
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
      clientSurname: '',
      clientFirstname: '',
      clientLastname: '',
      clientNumber: '',
    }
  },
  methods: {
    async saveClient() {
      await axios.post('http://127.0.0.1:5000/data/client', {
        method: 'ADD',
        Name_klienta: this.clientFirstname,
        Fam_klienta: this.clientSurname,
        Otch_klienta: this.clientLastname,
        Nomer_tel: this.clientNumber,
      });
      this.clearData();
    },
    clearData() {
      this.clientFirstname = '';
      this.clientSurname = '';
      this.clientLastname = '';
      this.clientNumber = '';
    }
  },
  computed: {
    disabledBtn() {
      return this.clientFirstname === '' || this.clientSurname === '' 
          || this.clientLastname === '' || this.clientNumber === '';
    }
  }
}
</script>