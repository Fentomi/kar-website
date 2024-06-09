<template>
	<v-dialog activator="#target6" width="600">
			<template v-slot:default="{ isActive }">
				<v-card
					title="Изменение статуса задачи"
				>
					<v-card-text>
						<v-text-field v-model="orderCode" label="Код заказа *"></v-text-field>
					</v-card-text>
					<template v-slot:actions>
						<v-spacer/>
						<v-btn
							text="Закрыть"
							@click="isActive.value = false"
						/>
						<v-btn
							text="Удалить"
							@click="deleteOrder"
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
      orderCode: null
    }
  },
  methods: {
    async deleteOrder() {
      await axios.post('http://127.0.0.1:5000/data/order', {
        method: 'DELETE',
        Kod_zakaza: this.orderCode
      });
      this.$emit('needUpdateOrderData');
    }
  }
}
</script>