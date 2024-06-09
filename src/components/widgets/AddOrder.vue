<template>
  <v-dialog activator="#target4" width="600">
      <template v-slot:default="{ isActive }">
        <v-card
          title="Форма оформления заказа"
        >
          <v-card-text>
            <div class="mb-3">Заполните все поля, чтобы сохранить</div>
            <v-select
              v-model="selectedEmployee"
              :items="employeesFirstnameSecondname"
              label="Выберите сотрудника"
            /> 
            <v-text-field v-model="orderDate" label="Дата заказа"></v-text-field>
            <v-text-field v-model="plannedOrderDate" label="Планируемая дата исполнения"></v-text-field>
            <v-select
              v-model="selectedClient"
              :items="clientsFirstnameSecondname"
              label="Выберите клиента"
            /> 
            <h3>Позиции заказа</h3>
            <div v-for="product in selectedProducts">
              <v-select
                v-model="product.productName"
                :items="products"
                label="Выберите товар"
                width="30"
              />
              <v-text-field v-model="product.productCount" label="Количество"></v-text-field>
            </div>
            <v-btn density="compact" icon="mdi-plus" @click="addNewPosition" class="mb-3"></v-btn>
            <h3>Сумма заказа</h3>
            <p>Сумма заказа {{ orderPrice }}</p>
            <p>Сумма предоплаты заказа {{ preOrderPrice }}</p>
          </v-card-text>
          <template v-slot:actions>
            <v-spacer/>
            <v-btn
              text="Закрыть"
              @click="isActive.value = false"
            />
            <v-btn
              :disabled="disabledBtn"
              text="Оформить"
              @click="saveOrder"
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
      selectedEmployee: null,
      selectedClient: null,
      selectedProducts: [{productName: '', productCount: null}],
      employees: [],
      clients: [],
      products: ['Торт "Наполеон"', 'Пирожное "Тирамиссу"']
    }
  },
  methods: {
    async saveOrder() {
      const employeeCode = this.employees.find(item => 
        item.Name_sotr === this.selectedEmployee.split(' ')[0] && item.Fam_sotr === this.selectedEmployee.split(' ')[1]).Kod_sotr;
      const clientCode = this.clients.find(item => 
        item.Name_klienta === this.selectedClient.split(' ')[0] && item.Fam_klienta === this.selectedClient.split(' ')[1]).Kod_klienta;
      await axios.post('http://127.0.0.1:5000/data/order', {
        method: 'ADD',
        Kod_klienta: clientCode,
        Kod_sotr: employeeCode,
        Stoimost_zakaza: this.orderPrice,
        Data_zakaza: this.orderDate,
        Data_vypolnenya: this.plannedOrderDate
      })
    },
    async getEmployees() {
      await axios.get('http://127.0.0.1:5000/data/employee').then(response => {
        console.log('employees', response.data);
        this.employees = response.data;
      });
    },
    async getClients() {
      await axios.get('http://127.0.0.1:5000/data/client').then(response => {
        console.log('clients', response.data);
        this.clients = response.data;
      });
    },
    addNewPosition() {
      this.selectedProducts.push({productName: '', productCount: null});
    }
  },
  computed: {
    employeesFirstnameSecondname() {
      return this.employees.map(item => item.Fam_sotr + ' ' + item.Name_sotr);
    },
    clientsFirstnameSecondname() {
      return this.clients.map(item => item.Fam_klienta + ' ' + item.Name_klienta);
    },
    orderPrice() {
      let price = 0;
      this.selectedProducts.forEach(item => {
        if(item.productName === 'Торт "Наполеон"') price += 600 * item.productCount;
        if(item.productName === 'Пирожное "Тирамиссу"') price += 200 * item.productCount;
      });
      return price;
    },
    preOrderPrice() {
      return this.orderPrice*0.5;
    }
  },
  async created() {
    await this.getEmployees();
    await this.getClients();
  }
}
</script>