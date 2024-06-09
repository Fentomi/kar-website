<template>
	<v-dialog activator="#target5" width="600">
			<template v-slot:default="{ isActive }">
				<v-card
					title="Изменение статуса задачи"
				>
					<v-card-text>
						<v-text-field v-model="orderCode" label="Код заказа *"></v-text-field>
						<v-select
              v-model="selectedStatus"
              :items="getStatuses"
              label="Выберите статус"
            /> 
					</v-card-text>
					<template v-slot:actions>
						<v-spacer/>
						<v-btn
							text="Закрыть"
							@click="isActive.value = false"
						/>
						<v-btn
							text="Изменить"
							@click="editOrder"
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
			orderCode: null,
			selectedStatus: null,
			roleEnum: {
				menedger: 1,
				shef: 2
			},
		}
	},
	props: {
		currentRole: Number,
	},
	methods: {
		async editOrder() {
			await axios.post('http://127.0.0.1:5000/data/order', {
				method: 'EDIT',
				Kod_zakaza: this.orderCode,
				Naimenovanye_stat: this.selectedStatus
			});
			this.orderCode = null;
			this.selectedStatus = null;
			this.$emit('needUpdateOrderData');
		},
	},
	computed: {
		getStatuses() {
			if(this.currentRole === this.roleEnum.menedger) return ['Отменен', 'Завершен'];
			if(this.currentRole === this.roleEnum.shef) return ['В работе', 'Готов'];
		}
	}
}
</script>