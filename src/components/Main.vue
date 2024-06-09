<template>
	<div class="header">
		<p class="header-text">CA<span style="color: palevioletred;">KE</span></p>
		<v-tabs
			v-model="tabs"
			align-tabs="title"
  	>
			<v-tab text="Заказчики" value="заказчики"></v-tab>
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
			@click="onAddClient"
		/>
		<v-btn 
			text="Список заказчиков" 
			class="btn"
			@click="isOpenClientList=!isOpenClientList"
		/>
	</div>
	<div v-if="tabs === 'заказы' && currentRole === roleEnum.menedger" class="wrapper">
		<v-btn text="Оформить заказ" class="btn mb-4"/>
		<v-btn text="Список заказов" class="btn"/>
	</div>
	<add-client-form
		@needUpdateClientData="updateClientData"
	/>
	<div v-if="tabs === 'заказчики'" style="width: 800px; margin: 0 auto;" class="mt-5">
		<client-list
			ref="clientList" 
			:isOpenClientList="isOpenClientList"
		/>
	</div>
</template>
  
<script>
import AddClientForm from '@/components/widgets/AddClientForm.vue';
import ClientList from '@/components/widgets/ClientList.vue'

export default {
	components: {
		AddClientForm, ClientList
	},
  data: () => ({
    tabs: null,
		roleEnum: {
			menedger: 1,
			shef: 2
		},
		isOpenClientList: false,
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
		}
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