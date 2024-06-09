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
		<add-client-form/>
		<v-btn 
			text="Список заказчиков" 
			class="btn"
			@click="onOpenClientList"
		/>
	</div>
	<div v-if="tabs === 'заказы' && currentRole === roleEnum.menedger" class="wrapper">
		<v-btn text="Оформить заказ" class="btn mb-4"/>
		<v-btn text="Список заказов" class="btn"/>
	</div>
</template>
  
<script>
import AddClientForm from '@/components/widgets/AddClientForm.vue'

export default {
	components: {
		AddClientForm
	},
  data: () => ({
    tabs: null,
		roleEnum: {
			menedger: 1,
			shef: 2
		}
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