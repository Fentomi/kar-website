<template>
	<div class="header">
		<p class="header-text">CA<span style="color: palevioletred;">KE</span></p>
		<v-tabs
			v-model="tabs"
			align-tabs="title"
  	>
			<v-tab v-if="currentRole === roleEnum.menedger" text="Заказчики" value="заказчики"></v-tab>
			<v-tab text="Заказы" value="заказы"></v-tab>
			<v-tab text="Печать отчета" value="печать отчета"></v-tab>
			<v-tab value="выход">
				<span>Выход</span>
				<span style="font-weight: bold; color: palevioletred;">({{ roleName }})</span>
			</v-tab>
  	</v-tabs>
  </div>
	<div v-if="tabs === 'заказчики' && currentRole === roleEnum.menedger" class="wrapper">
		<v-btn 
			text="Добавить заказчика"
			id="target" 
			class="btn mb-4"
		/>
		<add-client-form
			@needUpdateClientData="updateClientData"
		/>
		<v-btn 
			text="Редактировать заказчика"
			id="target2" 
			class="btn mb-4"
		/>
		<edit-client-form
			@needUpdateClientData="updateClientData"
		/>
		<v-btn 
			text="Удалить заказчика"
			id="target3" 
			class="btn mb-4"
		/>
		<delete-client-form
			@needUpdateClientData="updateClientData"
		/>
		<v-btn 
			text="Список заказчиков" 
			class="btn"
			@click="isOpenClientList=!isOpenClientList"
		/>
	</div>
	<div v-if="tabs === 'заказы' && currentRole === roleEnum.menedger" class="wrapper">
		<v-btn 
			id="target4"
			text="Оформить заказ" 
			class="btn mb-4"
		/>
		<add-order
      @needUpdateOrderData="updateOrderData"
		/>
		<v-btn 
			id="target5"
			text="Редактировать заказ" 
			class="btn mb-4"
		/>
		<edit-order
      :current-role="currentRole"
      @needUpdateOrderData="updateOrderData"
    />
		<v-btn 
			id="target6"
			text="Удалить заказ" 
			class="btn mb-4"
		/>
		<delete-order
      @needUpdateOrderData="updateOrderData"
    />
		<v-btn 
			text="Список заказов" 
			class="btn"
      @click="isOpenOrderList=!isOpenOrderList"
		/>
	</div>
  <div v-if="tabs === 'заказы' && currentRole === roleEnum.shef" class="wrapper">
    <v-btn 
			id="target5"
			text="Редактировать заказ" 
			class="btn mb-4"
		/>
		<edit-order
      :current-role="currentRole"
      @needUpdateOrderData="updateOrderData"
    />
  </div>
	<div v-if="tabs === 'заказчики'" style="width: 800px; margin: 0 auto;" class="mt-5">
		<client-list
			ref="clientList" 
			:isOpenClientList="isOpenClientList"
		/>
	</div>
  <div v-if="tabs === 'заказы'" style="width: 800px; margin: 0 auto;" class="mt-5">
		<orders-list
			ref="orderList" 
			:isOpenOrderList="isOpenOrderList"
		/>
	</div>
</template>
  
<script>
import AddClientForm from '@/components/widgets/AddClientForm.vue';
import DeleteClientForm from '@/components/widgets/DeleteClientForm.vue';
import EditClientForm from '@/components/widgets/EditClientForm.vue';
import ClientList from '@/components/widgets/ClientList.vue';
import AddOrder from '@/components/widgets/AddOrder.vue';
import EditOrder from '@/components/widgets/EditOrder.vue';
import DeleteOrder from '@/components/widgets/DeleteOrder.vue';
import OrdersList from './widgets/OrdersList.vue';

export default {
	components: {
		AddClientForm, EditClientForm, DeleteClientForm, ClientList, AddOrder, EditOrder, DeleteOrder, OrdersList
	},
  data: () => ({
    tabs: null,
		roleEnum: {
			menedger: 1,
			shef: 2
		},
		isOpenClientList: false,
    isOpenOrderList: true,
  }),
	props: {
		currentRole: Number,
	},
	computed: {
		roleName() {
			if(this.currentRole === this.roleEnum.menedger) return 'Менеджер по продажам';
			if(this.currentRole === this.roleEnum.shef) return 'Повар-кондитер';
		}
	},
	watch: {
		tabs: {
			handler(newValue) {
				if(newValue === 'выход') return location.reload();
			}
		}
	},
	methods: {
		async updateClientData() {
			return await this.$refs['clientList'].getClientList();
		},
    async updateOrderData() {
      return await this.$refs['orderList'].getOrderList();
    },
	},
}
</script>

<style scoped lang="scss">
.header {
	display: flex;
	justify-content: space-around;
  .header-text {
		display: inline-block;
    margin-left: 120px;
    font-size: 52px;
    font-weight: bold;
  }
	.v-tabs {
		display: inline-block;
	}
}
.wrapper {
	margin-top: 10vh;
	.btn {
		display: block;
		margin: 0 auto;
	}
}
.v-slide-group-item--active {
	color: palevioletred;
}
</style>