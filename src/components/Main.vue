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
	<div v-if="tabs === 'заказчики'">
		123
	</div>
	<div v-if="tabs === 'заказы'">
		345
	</div>
</template>
  
  <script>
    export default {
      data: () => ({
        tabs: null,
      }),
			props: {
				currentRole: Number,
			},
			computed: {
				roleName() {
					if(this.currentRole === 1) return 'Менеджер по продажам';
					if(this.currentRole === 2) return 'Повар-кондитер';
				}
			},
			watch: {
				tabs: {
					handler(newValue) {
						if(newValue === 'выход') return location.reload();
					}
				}
			}
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
.v-slide-group-item--active {
	color: palevioletred;
}
</style>