<template>
  <v-dialog :max-width="maxWidth">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn @click="this.$emit('resetBtnActions')" v-bind="activatorProps" :text="btnText" class="mb-2 mr-2"/>
    </template>
    <template v-slot:default="{ isActive }">
      <v-card :title="headerText">
        <v-card-text>
          <slot></slot>
        </v-card-text>
        <v-card-actions>
          <p>{{ actionResultText }}</p>
          <v-spacer/>
          <v-btn text="Закрыть" @click="isActive.value = false; onCloseDialog"/>
          <v-btn v-if="isAdd" text="Добавить" @click="addFunction"/>
          <v-btn v-if="isDelete" text="Удалить" @click="deleteFunction"/>
          <v-btn v-if="isEdit" text="Изменить" @click="editFunction"/>
        </v-card-actions>
      </v-card>
    </template>
  </v-dialog>
</template>

<script>
export default {
  name: 'BtnWithFormDialog',
  props: {
    headerText: {type:String, required: true},
    btnText: { type: String, required: true },
    maxWidth: { type: Number, required: true},
    isAdd: Boolean,
    isDelete: Boolean,
    isEdit: Boolean,
    addFunction: Function,
    deleteFunction: Function,
    editFunction: Function,
    onOpenDialog: Function,
    isAccessAction: Boolean,
    isErrorAction: Boolean,
  },
  computed: {
    actionResultText() {
      if(this.isAccessAction) return 'Успешно!';
      if(this.isErrorAction) return 'Ошибка!';
    }
  },
}
</script>